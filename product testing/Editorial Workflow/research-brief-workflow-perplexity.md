---
name: Research Brief Workflow with Perplexity (Refined 2026-03-16)
description: Two-phase research brief process using Perplexity API for SERP analysis + fact-checking, with decision gates and user approval
type: workflow
---

# RESEARCH BRIEF WORKFLOW (Refined 2026-03-16)

## Overview
Two-phase workflow combining Perplexity API SERP deep-dive + fact-checking to:
1. **Identify SERP consensus** (what factors actually rank now?)
2. **Verify stats independently** (is the cited source real?)
3. **Flag unverifiable claims** upfront (prevent citation issues)

---

## PHASE 1: SERP DEEP-DIVE (Perplexity Consensus)

### Step 1: User Conducts Live SERP Research
- Perform live Google search for target keyword
- Document 3–5 competitor URLs
- Record search intent + observations
- **Share with Claude**

### Step 2: Define Article Strategy (User Approval)
Claude asks **3 questions** — user approves:
- **Content Type** (guide, listicle, framework, tool, etc.)
- **Funnel Stage** (Problem Aware, Solution Aware, Decision, etc.)
- **Related Concerns** (ROI, implementation, measurement, etc.)

**Why:** Strategy clarity prevents wasted research.

### Step 3: Run Perplexity API SERP Analysis
**Perplexity Query (3 sub-queries):**

1. **Query Analysis**
   - "What are the most frequently mentioned factors/best practices for [KEYWORD]?"
   - "What does the SERP consensus say about [TOPIC]?"

2. **Competitor Keywords Analysis**
   - "What keywords are top-ranking pages using to discuss [KEYWORD]?"
   - "What terminology/frameworks dominate this SERP?"
   - Extract: 8–10 consensus factors + frequency (Very Common vs Common)

3. **Extract:**
   - Common factors across SERP
   - Frequency ranking (Very Common / Common / Emerging)
   - Competitor frameworks/models
   - Consensus best practices

**Output:** Perplexity SERP Findings (8–10 factors with frequency)

### Step 4: Compare User Analysis vs Perplexity
**Create comparison:**
```
USER'S ANALYSIS          │ PERPLEXITY FINDINGS      │ ALIGNMENT
─────────────────────────┼──────────────────────────┼──────────
Factor 1: [X]            │ Factor 1: [X] (Very)     │ ✅ Match
Factor 2: [Y]            │ Factor 2: [Y] (Common)   │ ✅ Match
Factor 3: [Z]            │ Factor 3: [Z] (Common)   │ ✅ Match
(etc.)                   │ Factor 4: [NEW] (Very)   │ ❌ Gap
                         │ Factor 5: [NEW] (Common) │ ❌ Gap
```

**Analyze:**
- Which of your factors appear in SERP consensus? ✅
- Which consensus factors did you miss? ❌
- New insights from Perplexity findings?

### Step 5: Narrow to 5–8 Core Factors
**Decision:** Use SERP consensus to finalize the core factors
- Keep high-frequency factors (Very Common / Common)
- Optionally add missed factors if they're "Very Common"
- Drop low-frequency factors (unless user strongly prefers)

**Output:** 5–8 finalized factors for article structure

### Step 6: User Approval (Phase 1)
User confirms:
- ✅ "Yes, these 5–8 factors match our article strategy"
- ✅ "Proceed to Phase 2 (fact-checking)"

**Decision Gate:** Do not proceed to Phase 2 without approval.

---

## PHASE 2: FACT-CHECK STATS (Perplexity Verification)

### Step 4: Fetch & Verify Sources
**For each of the 5–8 finalized factors:**

1. Extract stats from competitor pages
2. Identify primary sources cited (Bain, McKinsey, academic studies, brand reports, etc.)
3. **Run Perplexity API fact-checking:**
   - "Can you verify stat X from [SOURCE Y]?"
   - "Is this finding in [REPORT/STUDY] from [ORG]?"
   - "What is the primary source for the claim: [STAT]?"

**Perplexity Results:**
- ✅ **FOUND** → Verified (include with source attribution)
- ❌ **NOT FOUND** → Flagged (user can manually verify or exclude)
- ❓ **PARTIAL** → Note discrepancy (cite with caveats)

### Step 5: Build Two Tables

**TABLE 1: VERIFIED STATS — USE THESE**
| Stat | Source | Status |
|------|--------|--------|
| 59% cite product quality as loyalty reason | SAP Customer Loyalty Index 2025 | ✅ Verified |
| 5–25x cheaper to retain than acquire | Bain & Company (Reichheld) | ✅ Verified |
| 90% of loyalty programs deliver positive ROI | Capital One Shopping Report 2025 | ✅ Verified |

**TABLE 2: FLAGGED STATS — VERIFY BEFORE USE**
| Stat | Source | Issue |
|------|--------|-------|
| "87% of retailers use loyalty" | Razorfish Research | ❌ Source not found |
| "Loyalty increases CLV by 300%" | McKinsey (unlinked) | ❓ Specific report unclear |
| "Gen Z abandons 60% of programs" | Thompson & Wilson | ❌ Not independently verified |

### Step 6: Build Final Research Brief

**Sections:**
1. **SERP Consensus Factors** (5–8 finalized)
2. **Verified Stats — USE THESE** (primary sources only)
3. **Flagged Stats — VERIFY BEFORE USE** (secondary/unconfirmed)
4. **Content Gaps** (what Joy can fill)
5. **Joy Positioning Opportunity** (competitive advantage)
6. **Competitor Content Structure** (what ranks, why)

**Decision:** User approves research brief → Proceed to outline + writing

---

## KEY PRINCIPLES

| PHASE 1 (SERP FIRST) | PHASE 2 (STATS SECOND) |
|---|---|
| Find SERP consensus | Verify primary sources |
| Identify what ranks NOW | Only include traceable data |
| Structure from rankings | Flag unverifiable claims |
| User + Claude align on factors | Two-table approach |
| Narrow to core insights | Prevent misleading citations |

---

## DECISION GATES (USER APPROVAL REQUIRED)

1. **After Step 2:** ✅ Strategy approval (Content Type, Funnel, Concerns)
2. **After Step 6 (Phase 1):** ✅ Phase 1 approval (5–8 finalized factors)
3. **After Step 6 (Phase 2):** ✅ Research Brief approval (ready to outline)

**Why:** Gates prevent wasted effort and ensure alignment before deep work.

---

## EXAMPLE: factors-affecting-customer-loyalty

**Phase 1 Result:**
- Perplexity found 8 consensus factors
- Your 6 factors aligned ✅
- Gap identified: Customer Service (Very Common) ❌
- Decision: Add 7th factor or keep 6?

**Phase 2 Result:**
- Verified Stats: 4 (SAP Index 2025, Bain, Capital One)
- Flagged Stats: 13 (Razorfish, Thompson/Wilson, McKinsey unlinked)
- Decision: Manually verify flagged or exclude?

---

## When This Applies
**All articles, every time. No exceptions.**

Apply this workflow to:
- Research briefs
- Outline approvals
- Content gap analysis
- Stat verification before writing

---

**Workflow Codified:** 2026-03-16 with full Perplexity integration (Phase 1 + Phase 2)
