# Rewrite Plan: Scale Shopify Store Article

## Issues from manager review that I need to fix

---

### Copywriting punch patterns

**Pattern: "It isn't X. It's Y." (negate assumption, then replace with "real answer")**

Found in current draft (v1):

1. **Line 9:** "The fix isn't more budget. It's figuring out which of those three things is broken and fixing that one first." ← Classic instance. Two sentences, negate-then-replace.
2. **Line 17:** "But the ads are rarely where the money is actually lost, it's the store behind them." ← Softer variant, same underlying pattern.

Count: 2 in the current partial draft (4 sections written out of ~8 total). Style guide allows **one per article**.

**Decision:**
- **Keep #1 (line 9).** This is the article's central thesis. It earns the punch because it reframes the entire piece. Placed in the intro where it carries the most weight.
- **Rewrite #2 (line 17).** This is a secondary point, not the thesis. Rewrite to avoid the negate-replace formula. Instead of contrasting "ads" vs. "store," describe what's actually happening: "But for most stores at this stage, the real cost is in what happens once someone lands on the site: a product page that doesn't convert, a checkout that creates friction, or a customer who buys once and never comes back."
- **For all remaining sections (retention, operations, conclusion, FAQs):** Do not use this pattern again. Zero more instances.

---

### Statistics density

**Current draft stat inventory:**

| Section | Stats used | Consecutive stat paragraphs? |
|---|---|---|
| Intro | 0 | No |
| Why Does More Ad Spend Stop Working? | 1 (1.4% conversion rate, Littledata) | No. One stat paragraph (line 19), preceded and followed by reasoning paragraphs. ✅ |
| How Do You Find What's Holding Your Store Back? | 2 thresholds (1.5% conversion, 20% repeat purchase) | These are diagnostic thresholds, not evidence-stacking. Used as tools the reader checks, not proof. ✅ |
| How Do You Fix Conversion Rate? | 2 (4.6% add-to-cart, Littledata; 0.1s = 8.4% lift, Deloitte/Google) | No. Separated by 5 paragraphs of reasoning and tactics. ✅ |

**Assessment:** The current v1 draft handles density well because we caught this during drafting. No section has 3+ consecutive data-heavy paragraphs.

**Plan for upcoming sections:**

| Section | Stat budget | Breathing plan |
|---|---|---|
| Retention | 1 stat max (repeat purchase rate benchmark from Smile.io). | Open with friction scenario (no data). Introduce the stat after the reader understands the problem. Follow with reasoning paragraph before moving to tactics. |
| Operations | 0 stats. | This section breathes entirely with logic and a concrete scenario (what a day looks like for a $20K/month store owner). Coming after two data-informed sections, the contrast is deliberate. |
| Conclusion | 0 stats. | Action-oriented. No new data. |
| FAQs | 1-2 stats max (reuse benchmarks already cited). | Reference numbers from earlier sections, don't introduce new ones. |

---

### "Example first, concept second" - sections to restructure

**Current draft assessment:**

| Section | Opens with... | Verdict |
|---|---|---|
| Intro | Reader's situation: "You doubled your ad budget last quarter and revenue barely moved" | Friction first ✅ |
| Why Does More Ad Spend Stop Working? | Reader's experience: "When a Shopify store is doing $2K or $5K a month, growth tracks pretty closely with ad spend" | Concrete first ✅ |
| How Do You Find What's Holding You Back? | Action: "You can diagnose this in five minutes with your Shopify analytics open" | Action first ✅ |
| How Do You Fix Conversion Rate? | Common mistake: "Most store owners start by redesigning their homepage" | Concrete first ✅ |

No restructuring needed for written sections. They already follow friction/concrete first.

**Plan for unwritten sections:**

| Section | DON'T open with | DO open with |
|---|---|---|
| Retention | ~~"Conversion fixes stop the leaking, but retention is what fills the bucket."~~ (principle + metaphor) | Friction: a specific customer who bought once and disappeared. The cost of re-acquiring them. Then pull the principle from that. |
| Operations | ~~"Operational drag means the store owner is the bottleneck."~~ (principle + definition) | Friction: what a typical Monday looks like for a store owner doing $20K/month. Wake up to 14 orders to process, 23 customer emails, inventory to update manually. Then name the pattern. |

---

### Headers to sharpen

**Current headers (all pass):**

| Header | Type | Status |
|---|---|---|
| Why Does More Ad Spend Stop Working? | Question-based | ✅ |
| How Do You Find What's Actually Holding Your Store Back? | Question-based | ✅ |
| How Do You Fix a Conversion Rate That's Bleeding Money? | Question-based | ✅ |
| Product Page Changes That Lift Add-to-Cart Rates | Outcome-based | ✅ |
| How to Reduce Drop-Off at Checkout | Outcome-based | ✅ |

**Upcoming headers from outline:**

| Current header | Type | Issue | Replacement |
|---|---|---|---|
| What Does It Cost You When Customers Buy Once and Disappear? | Question-based | Fine as-is | Keep |
| Retention Tactics That Actually Work at This Stage | Informative label | "Tactics that work" is vague. What outcome? | **How to Get a Second Purchase from First-Time Buyers** |
| Are Manual Tasks the Reason You Can't Grow? | Question-based | Fine as-is | Keep |

---

### Transitions to vary

**Current transitions in v1:**

| From → To | Transition type | Pattern |
|---|---|---|
| Intro → Ad Spend section | No explicit transition, H2 heading does the work | Clean break |
| Ad Spend → Diagnostic | "You just need to know which part of the store is broken before you pour more money into getting people there." | Bridge sentence |
| Diagnostic → Conversion | "There's no point improving retention if most visitors bounce, and there's no point speeding up operations if buyers never return." | Logic chain |
| Conversion → Retention (line 57) | "These fixes stop the bleeding on the traffic you already have. But they only work on first-time visitors. The next bottleneck decides whether any of those buyers ever come back." | Direct pivot |

**Variety so far:** Clean break, bridge sentence, logic chain, direct pivot. Four different patterns. ✅

**Plan for upcoming transitions:**

| From → To | Planned transition type | Draft |
|---|---|---|
| Retention → Operations | Question transition | End retention section with a thought about what happens when conversion and retention are working but growth still stalls. Let the reader ask "then what?" |
| Operations → Conclusion | Bridge sentence pulling all three together | "You've found the bottleneck. You know the fix. The only thing left is to actually do it, and to do the right one first." |

**Patterns to avoid:** "At this stage..." (used zero times so far, keep it that way). "The real problem is..." (not used, keep it that way).

---

### Sentences that are too "AI-clean"

**Found in current draft:**

| Line | Sentence | Why it's too clean | Planned rewrite |
|---|---|---|---|
| 15 | "You're paying more per customer, but nothing downstream has improved to justify the extra cost." | "Nothing downstream has improved to justify the extra cost" is very balanced and measured. Sounds like a consultant's slide, not a person talking. | "You're paying more per customer, but your store hasn't gotten any better at converting them or keeping them." |
| 37 | "The drop-off is happening on product pages, and the gap between a page that sells and a page that doesn't usually comes down to three things." | Smooth setup sentence. "The gap between a page that sells and a page that doesn't" is carefully constructed. | "The drop-off is almost always on product pages. And the fixes are more specific than most store owners expect." |
| 55 | "Page speed compounds all of this." | Generic connector. Could be dropped into any article about any topic. | "Speed makes all of these problems worse." |
| 57 | "These fixes stop the bleeding on the traffic you already have. But they only work on first-time visitors. The next bottleneck decides whether any of those buyers ever come back." | Three perfectly balanced sentences in a row. The rhythm is too even. | "These fixes work on the traffic you already have. They won't bring anyone back for a second purchase, though. That's the next problem." |

---

### Retention section

**What the reviewer changed and why:**

1. **Opening: friction first, not principle first.**
   - Old: "Conversion fixes stop the leaking, but retention is what fills the bucket." (metaphor, principle)
   - New: "You paid to acquire the customer once. They bought. Then they disappeared." (specific situation the reader can see)
   - Why: The reader sees the problem before the framework. They don't have to decode a metaphor to understand what's at stake.

2. **Friction before principle.**
   - Old: jumped into retention as a concept, then backed it with data
   - New: showed the costly cycle first (paying to replace customers you already won), THEN named retention as the fix
   - Why: "So the store keeps paying to replace customers it already won once" is grounded in what's actually happening. It earns the principle that follows.

3. **Data supports, doesn't lead.**
   - Old: stacked stats early (64% more likely to buy, 5-7x acquisition cost, CAC risen 60%)
   - New: "The numbers support that." then one stat cluster, AFTER the point is already made
   - Why: Data is backup evidence, not the opening argument. The reader already believes the point before the numbers confirm it.

4. **Less metaphor, more reality.**
   - Old: "retention is what fills the bucket" (crafted line)
   - New: "the store keeps paying to replace customers it already won once" (business reality)
   - Why: Guide prefers direct, specific, honest over performative.

5. **Tactics after logic is clear.**
   - Old: jumped to tactics after data dump
   - New: friction → principle → supporting data → THEN tactics
   - Why: reader needs to understand WHY before they'll act on HOW

**My version (applying same principles, NOT copying reviewer's version):**

Plan for my retention section opening:
- Open with: A customer found your store through an Instagram ad, bought a $45 product, got the shipping confirmation, and never heard from you again. Three months later you paid Meta another $30 to win a completely different customer. That second sale cost you just as much as the first one.
- Then pull the principle: That's what low retention looks like in practice. You're paying full price for every sale instead of earning repeat revenue from people who already bought from you.
- Then one stat for support (Smile.io repeat purchase benchmark), placed after the point is established.
- Then move to tactics (post-purchase emails, loyalty programs, restock reminders) after the "why" is clear.

---

## My rewrite approach

**Keep the structure. Rewrite section by section.**

The outline and section order are solid. The diagnostic framework is the article's unique angle, and the H2 flow (why ads fail → diagnose → fix conversion → fix retention → fix operations) is logical. No structural changes needed.

**What changes:**

1. **Fix the one remaining "It isn't X. It's Y." pattern** (line 17). Keep only the intro instance.
2. **Apply the "AI-clean" sentence rewrites** listed above (4 sentences).
3. **Write the retention section friction-first**, following the principles from the review but using my own opening scenario and structure.
4. **Write the operations section scenario-first**, opening with what a day looks like before naming the bottleneck.
5. **Rename one H3 header** ("Retention Tactics That Actually Work at This Stage" → "How to Get a Second Purchase from First-Time Buyers").
6. **Continue varying transitions** for remaining sections (question transition after retention, bridge sentence after operations).
7. **Hold stat density** to the plan: 1 max for retention, 0 for operations, 0 for conclusion.

**What stays:**
- Intro (approved, works well)
- Ad spend section structure (one stat, breathing paragraphs around it)
- Diagnostic section (conversational prose, friction-first)
- Conversion section structure (bullet fixes under H3s, two stats well-spaced)
- All H2 headers except the one H3 noted above
