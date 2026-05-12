---
name: corporate-governance-engine
description: |
  Use when mapping existing corporate entities, understanding multi-state structures (California, Nevada, New York),
  deciding whether to form new entities, managing S-corp elections and tax filings, planning estimated taxes,
  optimizing deductions, or executing corporate governance. Start by mapping what you have, then get strategic
  recommendations on where/when/why/how to launch new entities. Covers formation decisions, liability isolation,
  tax optimization through entity stacking, asset protection through collateral strategies, and state-specific
  compliance. Essential for multi-entity strategy, creditor shielding, tax deferral, and understanding your
  socio-economic corporate footprint.
mode: all
model: ollama/qwen3:14b
tools:
  write: true
  edit: true
  bash: true
  read: true
  webfetch: true
---

# Corporate Governance Engine

Comprehensive multi-state corporate structure, tax optimization, and entity formation framework for S-corps across California, Nevada, and New York.

## Master Workflow

The engine operates in this sequence:

```
1. MAP EXISTING ENTITIES
   └─ What corporations do you have?
      └─ See: corporate-footprint-mapping.md

2. ANALYZE YOUR FOOTPRINT
   └─ Assets, liabilities, public records, data exposure
   └─ Tax position (current state, missed opportunities)
   └─ Liability exposure and creditor shielding gaps
   └─ See: corporate-footprint-mapping.md (section: Footprint Analysis)

3. GET STRATEGIC RECOMMENDATIONS
   └─ Where/when/why should I form new entities?
   └─ See: should-i-form-new-entity.md (Decision Framework)
   └─ See: multi-entity-strategies.md (Strategic Structures)

4. FORM NEW ENTITIES (if recommended)
   └─ State-specific formation procedures
   └─ Timeline, cost, requirements
   └─ See: entity-formation.md → state-specific guides

5. EXECUTE GOVERNANCE
   └─ Elections, meetings, resolutions, filings
   └─ Tax compliance across states
   └─ See: specific governance guides below
```

---

## Quick Navigation by Task

### "I need to understand what I currently have"
→ **corporate-footprint-mapping.md** — Map entities, assets, liabilities, public footprint

### "Should I form a new entity?"
→ **should-i-form-new-entity.md** — Decision framework with 8 reasons + red flags

### "I know I need new entities. What structure should I use?"
→ **multi-entity-strategies.md** — Operating + Holding models, vertical stacking, tax year separation

### "I want to form a new entity. How?"
→ **entity-formation.md** (overview) → **california-formation.md** / **nevada-formation.md** / **newyork-formation.md** (state-specific)

### "I need to understand entity types and tax treatment across states"
→ **state-comparison.md** → **california.md** / **nevada.md** / **newyork.md** (deep dives)

### "I need to elect S-corp status or manage multiple S-corp elections"
→ **form-2553-elections.md** — Federal + state election procedures

### "I need to handle corporate meetings, voting, or resolutions"
→ **corporate-meetings.md** / **board-resolutions.md** — Procedures and templates

### "I need to optimize taxes: estimated payments, deductions, credits"
→ **estimated-taxes.md** / **tax-deductions-strategies.md** / **s-corp-taxation.md**

### "I need to understand compliance deadlines"
→ **compliance-calendar.md** — Master deadline calendar (state-by-state)

### "I need to protect assets through entity structuring and collateral strategies"
→ **asset-protection-strategies.md** — Entity stacking, liens, charging orders

---

## Decision Tree: What Do I Need?

```
START: What's your current situation?

A) I don't know what I have
   ↓
   → corporate-footprint-mapping.md
   → (after mapping) continue to B

B) I know my entities. Do I need to do something with them NOW?
   ↓
   ├─ No, but I want to understand if I should form more
   │  ↓
   │  → should-i-form-new-entity.md
   │  → (if yes) multi-entity-strategies.md
   │  → (if ready to form) entity-formation.md
   │
   ├─ Yes, I need to handle an S-corp election
   │  ↓
   │  → form-2553-elections.md
   │  → (then) s-corp-taxation.md for multi-state implications
   │
   ├─ Yes, I need to hold a meeting or pass resolutions
   │  ↓
   │  → corporate-meetings.md (if annual/special meeting)
   │  → board-resolutions.md (if resolutions/banking/officer changes)
   │
   ├─ Yes, I need to optimize taxes
   │  ↓
   │  → estimated-taxes.md (quarterly planning)
   │  → tax-deductions-strategies.md (optimization)
   │  → s-corp-taxation.md (multi-state structure)
   │
   ├─ Yes, I need to understand my compliance obligations
   │  ↓
   │  → compliance-calendar.md (state-by-state master calendar)
   │  → state-comparison.md → state-specific guides
   │
   └─ Yes, I need to protect assets or restructure for creditor shielding
      ↓
      → asset-protection-strategies.md
      → multi-entity-strategies.md (entity stacking)
```

---

## Recommended Starting Point (New Users)

If you're new to multi-entity management:

1. **Map what you have** (5-10 min)
   - Read: corporate-footprint-mapping.md (section: Entity Mapping)
   - Output: Spreadsheet of entities, assets, liabilities

2. **Analyze your footprint** (10-15 min)
   - Read: corporate-footprint-mapping.md (section: Footprint Analysis)
   - Output: Understanding of what's public, what's protected, gaps in structure

3. **Get strategic recommendations** (15-20 min)
   - Read: should-i-form-new-entity.md (Decision Framework)
   - Output: 1-3 recommendations for new entities

4. **Deep dive into recommended structures** (30-45 min)
   - Read: multi-entity-strategies.md (sections relevant to your recommendations)
   - Read: state-comparison.md (state-specific tax implications)
   - Output: Clear understanding of which entities to form where

5. **Plan formation** (20-30 min)
   - Read: entity-formation.md
   - Read: state-specific formation guides
   - Output: Formation checklist, timeline, costs

---

## Core Concepts

### Entity Types (Quick Reference)

| Type | Fed Tax Default | CA Tax | NV Tax | NY Tax | Liability | Best For |
|------|-----------------|--------|---------|---------|-----------|----------|
| **C-Corp** | Entity-level tax | Yes (8.84% rate) | No | Yes | Limited | Retained earnings, reinvestment |
| **S-Corp** | Pass-through (1120-S) | Yes (elect Form 100-S) | No corp tax | Yes (elect Form CT-3-S) | Limited | Active business, salary + distributions |
| **LLC** | Pass-through (default) | Yes (treated as corp if elect) | No corp tax | Yes (depends on tax election) | Limited | Flexibility, asset protection, operations |
| **NV Holding Co** | S-corp (elect) | Yes (if operating in CA) | No corp tax | No (if not operating in NY) | Limited + charging order | Privacy, asset protection, IP holding |

### Multi-State Key Principle

**Form in most advantageous state, operate where customers/revenue are.**

- **Nevada holding company:** No corporate income tax, strong charging order protection, privacy
- **California operating company:** Where you generate revenue (required nexus = file CA)
- **New York:** Combined reporting may apply; carefully structure to avoid multi-state tax

---

## State Filing Agencies (Quick Reference)

| State | Entity Records | UCC Filing | Property Records |
|-------|----------------|-----------|-----------------|
| **California** | Secretary of State | Secretary of State | County assessor/recorder |
| **Nevada** | Secretary of State | Secretary of State | County assessor/recorder |
| **New York** | Department of State | Department of State | County assessor/recorder |

---

## Common Multi-Entity Scenarios (at a glance)

**Scenario 1: Service business in CA, want tax/liability protection**
- Operating LLC in CA (S-corp election for tax)
- Holding company in NV (owns IP, contracts with operating LLC)
- Result: Operating liability isolated, passive income (IP royalties) in NV (no corp tax)

**Scenario 2: Multiple business lines (consulting + products + real estate)**
- Entity 1: Consulting LLC (CA, S-corp election)
- Entity 2: Product/SaaS company (CA or NV, depending on IP strategy)
- Entity 3: Real estate holding LLC (CA or NV, depending on asset location)
- Result: Tax year stacking, separate profit centers, liability isolation by business line

**Scenario 3: Investment/acquisition vehicle**
- NV holding company (acquisition vehicle, owns target)
- Target company (remains separate or merged based on deal structure)
- Result: Asset protection, clean cap table, exit flexibility

**Scenario 4: Bankruptcy isolation**
- Operating company (takes all liability/risk)
- Clean holding company (owns valuable assets: IP, real estate, cash)
- Charging order protection in NV if structured correctly
- Result: If operating company fails, assets protected

---

## References (Navigation to Detailed Guides)

### Mapping & Analysis
- [corporate-footprint-mapping.md](references/corporate-footprint-mapping.md)

### Formation & Strategy
- [should-i-form-new-entity.md](references/should-i-form-new-entity.md)
- [multi-entity-strategies.md](references/multi-entity-strategies.md)
- [entity-formation.md](references/entity-formation.md)
- [california-formation.md](references/california-formation.md)
- [nevada-formation.md](references/nevada-formation.md)
- [newyork-formation.md](references/newyork-formation.md)

### State-Specific Tax & Compliance
- [state-comparison.md](references/state-comparison.md)
- [california.md](references/california.md)
- [nevada.md](references/nevada.md)
- [newyork.md](references/newyork.md)

### Tax Planning
- [s-corp-taxation.md](references/s-corp-taxation.md)
- [estimated-taxes.md](references/estimated-taxes.md)
- [tax-deductions-strategies.md](references/tax-deductions-strategies.md)

### Governance & Compliance
- [form-2553-elections.md](references/form-2553-elections.md)
- [corporate-meetings.md](references/corporate-meetings.md)
- [board-resolutions.md](references/board-resolutions.md)
- [compliance-calendar.md](references/compliance-calendar.md)

### Asset Protection
- [asset-protection-strategies.md](references/asset-protection-strategies.md)

---

## Key Principles

1. **Map first, decide second.**
2. **Multi-state intentionality.**
3. **Liability isolation.**
4. **Tax optimization.**
5. **Public records awareness.**
6. **Compliance by state.**

---

## Poly-Agentic Design

This skill is built to work across multiple AI agents:
- **Claude Code** — Full implementation, can write code to automate footprint mapping
- **Copilot CLI** — Reference access for planning and decision-making
- **Gemini CLI** — Asset discovery and analysis workflows
- **Custom agents** — Can reference asset-grabber logic and public records queries

---

*Last updated: 2026-04-23*
*Built for Handsome Gato Inc. and poly-agentic deployment*
