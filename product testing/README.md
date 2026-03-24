# Joy Content Workspace

Content production system for Joy Loyalty (joy.so/blog).

---

## Workspace Structure

```
joy-content/
|
|-- agents/                       Standalone orchestrators (6 agents)
|   |-- content-production-manager.md
|   |-- joy-super-content-agent.md
|   |-- research-agent.md
|   |-- article-refresh-agent.md
|   |-- humanizer-agent.md
|   +-- joy-glossary-agent.md
|
|-- subagents/                    Pipeline workers (6 subagents)
|   |-- research-subagent.md
|   |-- outline-subagent.md
|   |-- writer-subagent.md
|   |-- image-brief-subagent.md
|   |-- review-subagent.md
|   +-- rewriter-subagent.md
|
|-- skills/                       Claude Code .skill files
|   |-- joy-loyalty-content-writer.skill
|   +-- joy-article-editor.skill
|
|-- workflows/                    Editorial pipeline
|   +-- editorial/
|       |-- inbox/                Raw articles waiting for review
|       |-- in-review/            Articles being edited
|       +-- done/                 Approved, ready to publish
|
|-- settings/                     Shared config for all agents
|   +-- paths.md                  Central path registry
|
|-- Blog Posts/                   91 published articles by topic
|   |-- BFCM & Seasonal/
|   |-- Program Types/
|   |-- Industry Specific/
|   |-- Shopify & Tech/
|   |-- Strategy & Analytics/
|   +-- Foundations & Guides/
|
|-- Brand & Resources/            Brand assets and reference materials
|   |-- 01 - Company Overview/
|   |-- 02 - Brand Positioning/
|   |-- 03 - Target Audience/
|   |-- 04 - Competitive Landscape/
|   |-- 05 - Brand Personality/
|   |-- 06 - Brand Voice & Tone/
|   |-- 07 - Core Values/
|   |-- 08 - Product & Features/
|   |-- 09 - Product Vision 2026/
|   +-- 10 - Business Context/
|
|-- Content Calendar 2026/        Monthly content plans
|-- Glossary/                     Definition articles
|-- Posts/                        Production-ready posts by slug
|-- Raw data/                     Keywords, templates, fonts, checklists
+-- Scripts/                      Python scripts (image gen, Reddit monitor)
```

---

## Agent System

### Full Pipeline

Invoke the **Content Production Manager** with a keyword + funnel stage. It runs 5 subagents in sequence:

```
Research -> Outline -> Writer -> Image Brief -> Review -> [Rewriter if needed]
```

Output: publish-ready article + image briefs + editorial report.

### Standalone Agents

| Agent | What it does |
|-------|-------------|
| Super Content Agent | Write / Edit / Refine / Rewrite (all-in-one) |
| Research Agent | Deep research, returns Research Brief |
| Article Refresh Agent | Audit + refresh stale published articles |
| Humanizer Agent | Eliminate AI patterns from finished articles |
| Glossary Agent | Write/refresh glossary definition articles |

### Subagents

Called by the Content Production Manager. See `subagents/README.md` for the full pipeline diagram.

---

## Quick Start

**New article from keyword:**
```
Use agents/content-production-manager.md
Keyword: [keyword]
Funnel stage: [Unaware / Problem Aware / Solution Aware]
```

**Research only:**
```
Use agents/research-agent.md
Keyword: [keyword]
```

**Edit/review existing article:**
```
Use agents/joy-super-content-agent.md (EDIT mode)
```

**Refresh a stale article:**
```
Use agents/article-refresh-agent.md
Article: [path or text]
Keyword: [keyword]
```

---

## Shared Config

All agents reference `settings/paths.md` for brand resource locations, keyword database paths, and editorial workflow folders. Update paths there when resources move.
