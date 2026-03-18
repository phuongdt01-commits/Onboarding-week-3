# Outline Generator Prompt

Paste this prompt into Claude Code, then provide your topic. Claude will handle the rest.

---

## The Prompt

```
Before generating anything, read these two files:
1. style-guide/writing-style-guide-v3(final).md
2. templates/blog-post-outline-template.md

Now generate a complete blog post outline using the template structure.

Here is the content brief:

- **Topic:** [your topic here]
- **Target keyword:** [your keyword, or leave blank and I'll suggest one]
- **Audience:** [who the reader is, or leave blank and I'll infer from the topic]
- **Angle:** [your angle, or leave blank and I'll propose one]
- **Target word count:** [total target, or leave blank for a default ~1,500 words]

---

Follow these rules when generating the outline:

**Meta section:**
- Write a working title that signals the angle, not just the topic. "How to Start Dropshipping" is generic. "Why Most Dropshipping Advice Sets You Up to Fail" has a point of view.
- Write a meta description that leads with tension or value. No "In this article" or "Learn how to."
- If the user left keyword, audience, or angle blank, fill them in based on the topic and flag your assumptions so the user can correct them.

**Introduction:**
- Pick the hook type that best fits the angle. Default to problem-first or reframe-first unless the topic clearly calls for something else.
- Write a one-sentence problem statement with real stakes. Not "Most people struggle with X." Something the reader recognizes from their own experience.
- Write a preview line that tells the reader what changes for them. Not what the article covers.

**Body sections:**
- Create 3-6 H2 sections depending on the topic's complexity and the target word count.
- Every H2 heading must be question-based ("What Makes X Different?") or outcome-based ("Choosing the Right X for Your Store"). No generic labels like "Overview," "Key Findings," or "Benefits."
- For each section, fill in: purpose, key points, evidence needed, and transition out.
- Assign a word count estimate to each section. The total should match the target word count.
- Give your strongest argument the most space. At least one section should get a full evidence breakdown (data, named sources, concrete examples). Secondary points get 1-2 paragraphs.
- Vary transition types across sections. Use a mix of bridge sentences, questions, and direct pivots. Do not repeat the same transition pattern more than twice.
- Use H3 subsections only when a section genuinely covers two or more distinct subtopics.
- Mark any section that requires specific data, case studies, or source verification with [NEEDS RESEARCH] next to the heading.

**Conclusion:**
- Pick the closing type that fits the piece. Default to "here's what I'd do" recommendation unless the topic calls for a reframe or callback.
- Write a specific final thought. Not a summary, not general advice.
- Include a CTA placeholder with a note on what type of action fits (e.g., "try the tool," "read the next piece," "audit your current setup").

**Pre-draft checklist:**
- After the outline, run through the checklist from the template and confirm each item passes. If any item fails, fix the outline before presenting it.

**Style Guide compliance:**
- All heading choices, tone hints, and structural decisions must follow the Writing Style Guide. If anything in the brief conflicts with the Style Guide, flag it and ask before proceeding.
- Do not use any banned vocabulary from the Style Guide in headings, key points, or transition notes.
- Evidence notes should follow concrete-before-abstract order.

Present the completed outline, then ask: "Want to adjust anything before I start drafting?"
```

---

## Quick-Start Examples

**Minimal input (topic only):**
```
Generate an outline.

- **Topic:** Shopify review apps for small stores
```

**Full brief:**
```
Generate an outline.

- **Topic:** Why most Shopify merchants pick the wrong loyalty app
- **Target keyword:** best shopify loyalty app
- **Audience:** Shopify store owners doing $10K-$50K/month, evaluating loyalty apps for the first time
- **Angle:** Debunking — most comparison articles rank apps by feature count, but the real differentiator is integration depth with your existing stack
- **Target word count:** 2,000
```
