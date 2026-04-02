# Fact-Check: Scale Shopify Store Article

## Statistics Verified

### Claims used in the current draft (v1)

| Claim | Source | Status | Notes |
|---|---|---|---|
| Average Shopify conversion rate: 1.4% | Littledata | ✅ Confirmed | Littledata's current benchmark confirms 1.4% average across all devices. Top 20% at 3.2%+, top 10% at 4.7%+. Mobile drops to 1.2%, desktop rises to 1.9%. |
| Add-to-cart rate below 8% = product page problem | Littledata | ❌ Wrong | **The average Shopify add-to-cart rate is 4.6%, not 8%.** Top 20% is 7.5%, top 10% is 9.6%. Using "below 8%" as a diagnostic threshold would flag nearly every Shopify store as broken. The draft needs to be corrected. Use ~4.6% as the average or reframe the threshold. |
| 0.1-second speed improvement = 8.4% conversion lift for retail | Deloitte + Google, "Milliseconds Make Millions" (2020) | ✅ Confirmed | The study is real, published March 2020. The 8.4% figure is specifically for retail. Study covered 37 brand sites, 30M+ user sessions. Minor nuance: the study was a three-way effort between Google, Deloitte, and Fifty-Five (a data consultancy), not just "Deloitte and Google." |

### Claims in research notes (for upcoming sections)

| Claim | Source | Status | Notes |
|---|---|---|---|
| Acquiring a new customer costs 5-7x more than retaining one | Bain & Company / Amy Gallo, HBR 2014 | ⚠️ Wrong range | Amy Gallo's HBR article says **"5 to 25 times"**, not 5-7x. The "7x" variant traces to a 2014 White House Office of Consumer Affairs report. The original Bain/Reichheld research gives no single multiplier. **Fix: cite as "5 to 25 times" per Gallo's HBR article, or describe directionally without a specific number.** |
| 5% retention increase = 25-95% profit increase | Reichheld & Sasser, HBR 1990 | ⚠️ Usable with caveat | The 1990 article "Zero Defections" is real but gives **industry-specific figures** (85% banking, 50% insurance, 30% auto-service, 125% credit cards). The "25-95%" range is a later generalization from Reichheld's subsequent Bain work and Gallo's 2014 article. Directionally valid. **Fix: cite the full range (25-95%), attribute to Reichheld/Bain via Gallo's HBR article, and note the data is from the 1990s.** |
| Average repeat purchase rate: ~27% overall; smaller stores trend 15-20% | Smile.io | ⚠️ Partially correct | Smile.io data (100K+ merchants) reports a **27% probability of returning after a single purchase**, not an overall store repeat purchase rate. These are slightly different metrics. The "15-20% for stores under $1M/yr" breakdown by revenue tier **could not be found** in any Smile.io source. **Fix: use 27% as the return probability, drop the small-store claim, or find the original source.** |
| Post-purchase email open rates: 40-50% | Klaviyo | ⚠️ Conservative | Klaviyo benchmarks confirm strong post-purchase open rates, but current data suggests the average is closer to **~60%**, higher than the 40-50% claimed. The 40-50% range may reflect older data. **Fix: update to ~60% or cite as "over 40%" to stay conservative.** |
| Loyalty program members spend 12-18% more per year | Bond Brand Loyalty, "The Loyalty Report" | ❌ Wrong attribution | The 12-18% figure traces to **Accenture**, not Bond Brand Loyalty. Bond's "Loyalty Report" contains different metrics (members spend up to 40% more, or 164% more when redeeming rewards). **Fix: re-attribute to Accenture, or use Bond's actual figures with correct attribution.** |
| Loyalty program members have 2-3x higher repeat purchase rate | Smile.io | ⚠️ Vendor data | Smile.io does report this based on their own platform data. Directionally useful but inherently biased as vendor data. **Use with "according to Smile.io's platform data" qualifier.** |
| CAC increases 30-60% when scaling from $10K to $50K+ ad spend | Common Thread Collective | ❌ Cannot verify | The specific "30-60%" figure tied to the "$10K to $50K" range **does not appear in any CTC article or report**. CTC writes about diminishing returns and rising CAC broadly, but this specific stat may be fabricated. **Fix: drop the specific percentage. Describe the pattern (CAC rises as you exhaust warm audiences) without citing a number, or find the exact CTC source.** |
| CAC for small Shopify stores: ~$30-$75 via paid social | Triple Whale | ⚠️ No clean source | No single clean source for Shopify CAC by revenue tier. Triple Whale publishes benchmarks but the specific range is not easily verifiable. **Fix: frame as general range, not a hard stat, or drop it.** |

---

## Case Studies Verified

| Case Study | Original Source Found? | Notes |
|---|---|---|
| No case studies in current draft (v1) | N/A | The draft uses benchmarks and diagnostic thresholds instead of named case studies. No fabricated case studies present. |

---

## Product/Tool Claims Verified

| Tool | Claim in Article | Current Reality | Needs Update? |
|---|---|---|---|
| Shop Pay / Apple Pay / PayPal | Listed as preferred payment methods buyers look for at checkout | These are the three most common alternative payment methods on Shopify. Shop Pay is Shopify's native accelerated checkout. Claim is accurate. | No |
| Shopify Analytics | Used as the diagnostic tool (check conversion rate, repeat purchase rate) | Shopify analytics dashboard does show conversion rate and returning customer rate. Claim is accurate. | No |

---

## Critical Fixes Needed in the Draft

### 1. Add-to-cart rate threshold (MUST FIX)

**Current draft (line 41):** "If your add-to-cart rate is below 8%, the product page is where visitors are deciding to leave."

**Problem:** The average Shopify add-to-cart rate is 4.6%. Using 8% as a "problem" threshold would flag almost every store. 8% is actually above the top-20% benchmark (7.5%).

**Fix options:**
- Change to: "If your add-to-cart rate is below 5%..." (slightly above the 4.6% average, flags underperformers)
- Or reframe: "The average Shopify add-to-cart rate is 4.6% according to Littledata. If yours is below that, the product page is the first place to look."

### 2. CAC 30-60% claim (already removed from draft)

This stat was used in an earlier draft version but was removed during the review process. It does not appear in the current draft. No action needed, but flag it in the research notes as unverifiable.

---

## What I Learned

Three things stood out from this fact-check:

**1. The add-to-cart rate was the biggest miss.** The research notes listed "Average add-to-cart rate for Shopify stores is ~8%" with a [VERIFY] tag, sourced to Littledata. The actual number is 4.6%. This is not a rounding error; it's nearly double the real figure. The draft used this wrong number as a diagnostic threshold, which would have told readers their store has a problem when it's actually performing at or above average. This is exactly the kind of error that sounds plausible but misleads the reader.

**2. Attribution errors are easy to miss.** The loyalty spending stat (12-18%) was attributed to Bond Brand Loyalty when it actually comes from Accenture. The acquisition cost multiplier was cited as "5-7x" when the HBR source says "5-25x." These aren't made-up numbers, but misattributed or narrowed versions of real data. AI generates these "close but wrong" citations confidently, and they pass a surface-level check because the general idea is correct.

**3. Vendor data needs a qualifier.** Smile.io, Klaviyo, and Bond all publish benchmarks based on their own platform users, not the full Shopify ecosystem. Their numbers skew toward stores that already use loyalty programs, email marketing, or specific analytics tools. Citing them without noting the bias makes the data sound more universal than it is.

**The lesson:** Every stat with a [VERIFY] tag in the research notes existed for a reason. The ones that turned out wrong were the ones where the AI-generated research sounded most confident. The more specific and precise a number looks, the more important it is to check the actual source page, not just trust that the number matches the attribution.
