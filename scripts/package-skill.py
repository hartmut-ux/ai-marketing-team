#!/usr/bin/env python3
"""Package a skill into platform-specific ZIP files.

Usage:
    python scripts/package-skill.py <skill-name>

Produces in dist/:
    <skill-name>-all.zip
    <skill-name>-kimi.zip
    <skill-name>-claude.zip
    <skill-name>-codex.zip
"""

from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"


def package_skill(skill_name: str) -> None:
    skill_dir = SKILLS_DIR / skill_name
    if not skill_dir.exists():
        print(f"Skill not found: {skill_dir}")
        raise SystemExit(1)

    DIST_DIR.mkdir(exist_ok=True)

    variants = {
        "all": [".kimi", ".claude", ".codex", "shared", "README.md"],
        "kimi": [".kimi", "shared", "README.md"],
        "claude": [".claude", "shared", "README.md"],
        "codex": [".codex", "shared", "README.md"],
    }

    for variant, includes in variants.items():
        zip_path = DIST_DIR / f"{skill_name}-{variant}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for include in includes:
                source = skill_dir / include
                if not source.exists():
                    continue
                if source.is_dir():
                    for file in source.rglob("*"):
                        if file.is_file():
                            arcname = f"{skill_name}/{file.relative_to(skill_dir)}"
                            zf.write(file, arcname)
                else:
                    arcname = f"{skill_name}/{source.name}"
                    zf.write(source, arcname)
        print(f"Created {zip_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/package-skill.py <skill-name>")
        raise SystemExit(1)

    package_skill(sys.argv[1])
