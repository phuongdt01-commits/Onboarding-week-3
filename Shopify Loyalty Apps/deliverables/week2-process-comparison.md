# Week 2 Process Comparison: Claude.ai vs Claude Code

**Writer:** Dao Thu Phuong
**Date:** March 13, 2026

---

## Side-by-Side Comparison

| Aspect | Week 1 (Claude.ai) | Week 2 (Claude Code) |
|--------|---------------------|----------------------|
| Time to create outline | ~30 min — had to prompt, copy the output, paste into a doc, then re-prompt for revisions | ~10 min — one prompt created the outline file directly; edits happened in place |
| Ease of editing | Moderate — copied sections back into Claude.ai, prompted for changes, then pasted the result back into my doc | Easy — asked Claude Code to edit specific paragraphs in the file; changes appeared instantly without copy-paste |
| File management | Manual — all files lived in separate browser tabs or Google Docs; had to name and organize everything myself | Built-in — research, outlines, drafts, and final versions each had a dedicated folder; Claude Code created and organized them automatically |
| Consistency across sections | Hit or miss — each new chat could drift in tone because Claude.ai doesn't see previous sections unless I paste them in | Strong — Claude Code reads the full draft and CLAUDE.md before writing, so tone and structure stayed consistent from intro to conclusion |
| Fact-checking workflow | No system — I had to remember which stats needed verification and check them manually | Structured — research file used [VERIFY] tags for unverified claims, making it clear exactly what still needed checking |
| Overall satisfaction (1-10) | 6 | 8 |

---

## Reflection Questions

### 1. Which tool did you prefer for brainstorming? Why?

**Claude.ai.** When I'm still figuring out what angle to take or which topic to write about, the browser chat feels faster and lower-commitment. I can throw out half-formed ideas, ask "what do you think about X vs Y," and explore without worrying about file structure. The Artifacts panel is also nice for seeing outlines rendered visually while I'm still deciding on direction.

### 2. Which tool did you prefer for drafting? Why?

**Claude Code.** Once I knew what I was writing, Claude Code was significantly faster. Instead of prompting for a section, copying it, pasting it into my document, and then going back for the next section, I could just say "write the next section and append it to the draft." Everything stayed in one file, and I didn't lose formatting or context between prompts. The pipeline approach — research first, then outline, then draft — also forced me to think more systematically about structure before jumping into writing.

### 3. Which tool did you prefer for editing? Why?

**Claude Code.** This is where the difference was most obvious. In Week 1, editing meant copying a paragraph into Claude.ai, explaining what I wanted changed, waiting for the response, and pasting it back. With Claude Code, I could say "in drafts/shopify-reviews-v1.md, rewrite the hook to follow the Pain → Shock → Proof → Promise pattern" and it would update the file directly. The fact that Claude Code could read my CLAUDE.md and the blog writing skill file while editing meant the revisions already matched the brand voice — I didn't have to re-explain the tone every time.

### 4. What's your ideal workflow using both tools?

**Brainstorm in Claude.ai, produce in Claude Code.** My ideal flow looks like this:

1. **Claude.ai** — Explore the topic, test different angles, generate rough ideas
2. **Claude Code** — Create the research file with [VERIFY] tags
3. **Claude Code** — Build the outline based on research
4. **Claude Code** — Draft v1, v2, and final through the pipeline
5. **Claude.ai** — Paste tricky sections (like hooks or conclusions) for focused feedback using Artifacts
6. **Claude Code** — Final polish, review scoring, and social media repurposing

The key insight is that Claude.ai is better for thinking and Claude Code is better for producing.

### 5. What would you change about your CLAUDE.md after this week's experience?

Two things:

1. **Add more "don't" examples.** The current CLAUDE.md tells Claude what to do, but I noticed Claude Code still occasionally produced generic transitions or vague phrasing. Adding specific "bad vs good" examples — like the ones in the blog writing skill's Section 3 — would catch these issues earlier.

2. **Add a content pipeline checklist.** Right now the CLAUDE.md covers voice and formatting, but it doesn't describe the research → outline → draft → final workflow. If I included that, Claude Code would automatically follow the pipeline for any new article without me having to explain the steps each time.
