# Hartmut's AI Marketing Team

**Hartmut's AI Marketing Team — 11 specialists**

Built for SMEs, financial services firms, and purpose-driven organizations that need full marketing & communications capability without a 20-person department.

Created by [Hartmut Hübner, PhD](https://linkedin.com/in/hartmuthuebner) — AI Marketing Strategist, Co-Founder MMIND.ai.

## What This Is

11 specialized Claude Skills that together cover the complete marketing and communications function of a mid-sized organization. Each skill is a "team member" with deep expertise in their domain.

Unlike generic AI marketing tools, this team also covers **internal communications, change management, stakeholder governance, and government affairs** — the areas where quality matters most and where most AI tools fall short.

## The Team

| # | Role | Skill | What It Does |
|---|------|-------|--------------|
| 1 | Content Strategist | `content-strategist` | LinkedIn posts, thought leadership, content calendars (7 post types) |
| 2 | Newsletter Editor | `newsletter-editor` | Complete newsletter editions with SEO metadata and audio briefings |
| 3 | Performance Marketer | `performance-marketer` | Ad copy, Google Ads RSA, A/B testing, campaign optimization |
| 4 | Brand Guardian | `brand-guardian` | Visual identity, AI image prompts, design system enforcement |
| 5 | PR & Media Manager | `pr-media-manager` | Press releases, media pitches, crisis comms, spokesperson prep |
| 6 | Internal Comms Lead | `internal-comms-lead` | Employee newsletters, change announcements, town halls |
| 7 | Change & CI Coach | `change-ci-coach` | AI adoption, Marginal Gains sprints, resistance management |
| 8 | Stakeholder Communicator | `stakeholder-comms` | Board reports, investor updates, impact reporting (B Corp aligned) |
| 9 | Government Affairs Advisor | `government-affairs` | Policy papers, lobbying transparency, EU AI Act compliance |
| 10 | Analytics & Reporting | `analytics-reporting` | KPI dashboards, campaign ROI, weekly/monthly reports |
| 11 | Marketing Operations | `marketing-ops` | Budget planning, meeting management, vendor admin, SOPs |

## Why This Exists

In February 2026, it became public that [Anthropic's entire growth marketing was run by one person for 10 months](https://claude.com/blog/how-anthropic-uses-claude-marketing). The IPR study showed 95.4% of comms professionals use GenAI — but only 36% have a strategy.

The gap isn't tools. It's systems.

This skill set closes that gap. Not with theory, but with production-ready workflows that any marketing professional can use immediately.

## How It's Different

**Most AI marketing tools** handle content creation — social posts, emails, ad copy.

**This team** also handles:
- **Internal Communications**: Because AI transformation fails without internal alignment
- **Change Management**: Because adoption is the bottleneck, not technology
- **Stakeholder Governance**: Because B Corp and ESG reporting require systematic communications
- **Government Affairs**: Because the EU AI Act and CSRD affect every European company
- **Marketing Operations**: Because budgets, meetings, and admin eat 30%+ of a leader's time

The Marginal Gains philosophy (1% improvements that compound) runs through everything. No big-bang transformations. 2-week sprints. Measurable progress.

## Installation

### For Claude.ai (Individual)

1. Download the skill folder(s) you need
2. Go to Claude.ai → Settings → Capabilities → Skills
3. Upload the skill folder (zip if needed)
4. Enable the skill

### For Claude Code

Place skill folders in your Claude Code skills directory:
```
~/.claude/skills/content-strategist/
~/.claude/skills/newsletter-editor/
...
```

### Full Team Installation

Clone this repo and install all 11 skills:
```bash
git clone https://github.com/hartmut-ux/ai-marketing-team.git
```

## Customization

These skills are designed to be customized for your organization:

1. **Brand Voice**: Replace the MMIND.ai brand guidelines with your own in the Brand Guardian skill
2. **Post Types**: Adapt the 7 LinkedIn post types in the Content Strategist to your audience
3. **Reporting**: Adjust KPI benchmarks in Analytics & Reporting for your industry
4. **B Corp**: If you're not B Corp certified, the governance frameworks still apply — just remove certification-specific language
5. **Language**: Skills default to DE/EN bilingual (Swiss German). Adapt to your market.

## Architecture

Each skill follows Claude's standard skill structure:
```
skill-name/
├── SKILL.md          # Main instructions (YAML frontmatter + Markdown)
├── references/       # Additional documentation loaded on demand
└── assets/           # Templates, examples, brand files
```

Skills are **composable** — they reference each other's expertise and hand off tasks when appropriate. The Content Strategist works with the Brand Guardian for visuals. The Internal Comms Lead works with the Change & CI Coach for transformation narratives. The Stakeholder Communicator works with Government Affairs for policy updates.

## B Corp Standards Integration

Two B Lab standards are embedded throughout:

- **PSG** (Purpose & Stakeholder Governance): Ensures responsible marketing, stakeholder consideration, transparent reporting
- **GACA** (Government Affairs & Collective Action): Ensures responsible lobbying, collective impact, tax transparency

These standards apply whether or not your organization pursues B Corp certification. They represent best practices for purpose-driven business.

## Contributing

Improvements welcome. Please:
1. Keep skills focused (one role, one responsibility)
2. Follow Claude's skill format (SKILL.md with YAML frontmatter)
3. Include quality checklists
4. Reference B Corp standards where relevant
5. Test with real use cases before submitting

## License

MIT — Use freely. Customize for your organization. Credit appreciated.

## About the Author

**Hartmut Hübner, PhD** combines 20 years of corporate communications in large enterprises (Siemens, financial services) with 10 years of experience in transformation, digitalisation and AI. Co-founder of several startups, including MMIND.ai. Academic background at LMU Munich and PhD from the University of Salford (thesis: *The Communicating Company*).

This AI Marketing Team represents his methodology for building agentic teams that integrate AI into communication workflows — while maintaining brand consistency, strategic alignment, and stakeholder governance.

- 🌐 [mmind.ai](https://mmind.ai) · [MMIND.ai Marketplace](https://mmind.ai/marketplace)
- 💼 [LinkedIn](https://linkedin.com/in/hartmutplass)
- 🐙 [GitHub](https://github.com/hartmut-ux)
