# Joy Visual Brand Kit

> Single source of truth for Joy's visual identity: colors, typography, layout patterns, and component library.

---

## Color Palette

| Name | Hex | Role |
|---|---|---|
| **Navy Blue** | `#06038D` | Primary: headlines, card backgrounds |
| **Cerulean** | `#00BCE1` | Accent: badges, numbers, highlights, icons |
| **Bittersweet** | `#FF6D6A` | Warm emphasis: ONE element per image only |
| **Cherokee** | `#FCD299` | Subtle: underlines, dividers, thin accents |
| **White** | `#FFFFFF` | Text on dark cards |
| **Rich Black** | `#000000` | Strong contrast where needed |

**Old wrong colors (NEVER use):** `#01A6EA`, `#DC6578`, `#06048C`, `#FBC80B`

### Tested Color Combinations

| Background | Primary text | Accent | Emphasis | Use for |
|---|---|---|---|---|
| Light gradient | `#06038D` Navy | `#00BCE1` Cerulean | `#FF6D6A` Bittersweet | In-content blog images |
| `#06038D` Navy card | `#FFFFFF` White | `#00BCE1` Cerulean badge | `#FF6D6A` highlight card | Card components |
| `#FF6D6A` Bittersweet card | `#FFFFFF` White | `#FFFFFF` White badge | - | One emphasis card only |
| `#FFFFFF` White | `#06038D` Navy | `#00BCE1` Cerulean | `#FCD299` Cherokee underline | Clean minimal layouts |

### Color Mapping: Dark to Light Background

| Dark version | Light version |
|---|---|
| White headline | `#06038D` Navy headline |
| Cerulean headline line | `#00BCE1` Cerulean (same) |
| Frosted glass cards `rgba(255,255,255,0.08)` | Navy cards `#06038D` |
| White subtext `rgba(255,255,255,0.75)` | Navy subtext `rgba(6,3,141,0.65)` |
| Frosted pills `rgba(255,255,255,0.12)` | Light navy pills `rgba(6,3,141,0.08)` |

### Color Count Rule

**Minimum 2 colors per image** (not counting the background PNG). Before writing HTML, state your color plan:

| Situation | Color count | Rule |
|---|---|---|
| Simple hero, single concept | 2: Navy + Cerulean | No emphasis needed |
| Cards with equal weight items | 2: Navy + Cerulean | All cards same glass variant |
| Cards with a clear winner / most critical item | 3: Navy + Cerulean + Bittersweet | Coral card = qualitatively different item |
| Step flow with outcome step | 3: Navy + Cerulean + Bittersweet | Last step Coral = the destination |

### Color Rules on Light Background

```
Primary text   #06038D  (Navy) - headlines, section titles
Accent text    #00BCE1  (Cerulean) - badges, numbers, icon fills
Emphasis       #FF6D6A  (Bittersweet) - ONE emphasis element per image
Cherokee       #FCD299  - valid uses below (NEVER as text color)
Card fill      white or semi-transparent
Card text      #06038D  (Navy)
```

### Color Rules on Dark Background

```
Primary text   #FFFFFF  (White)
Accent text    #00BCE1  (Cerulean) - badges, numbers, labels
Emphasis       #FF6D6A  (Bittersweet) - ONE element max
Card fill      rgba(255,255,255,0.08-0.12) frosted glass
Badge fill     #00BCE1  (Cerulean)
Badge text     #FFFFFF
Description    rgba(255,255,255,0.75)
```

---

## Typography

**Font:** System sans-serif stack (renders as Inter/Geist Sans visually). No local font files, no Google Fonts, no `@font-face`.

```css
font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
```

**Legacy font files** (DM Sans in `Raw data/Fonts & Colors/`): retained for reference but not used in current image/PDF generation.

| Weight | CSS | Use |
|---|---|---|
| Bold | 700 | Hero stats, primary headlines, card titles |
| Semibold | 600 | Card descriptions, supporting text |
| Medium | 500 | Body labels, overlines, captions |
| Regular | 400 | Do NOT use (too thin at image resolution) |

| Element | Size |
|---|---|
| Hero stat / large number | 140-180px |
| Primary headline | 64-84px |
| Card title | 28px |
| Card description | 22px |
| Overline / caption | 14-16px |

**Typography rules:**
- All body/description text must be `font-weight: 600` minimum
- Max 15 words of visible text per image
- Never use more than 2 font sizes in a single image
- Key stat is always the largest element in data-forward layouts
- Never use serif, italic, or decorative fonts
- 60px minimum padding on all sides
- Headlines: `line-height: 1.15`-`1.3`; descriptions: `line-height: 1.5`

---

## Background Assets

PNG backgrounds with baked-in Joy logo. Pick based on format:

| Name | File | Use |
|---|---|---|
| **Thumbnail** | `Raw data/Backgrounds/thumbnail/thumbnail.png` | Hero / featured images (1526x886) |
| **Content** | `Raw data/Backgrounds/content/1-4.png` | In-content images (1526x779) |
| **PDF Portrait** | `Raw data/Backgrounds/pdf/portrait-a4.webp` | PDF cover & CTA pages (1240x1754, A4 @150DPI) |

Content backgrounds logo positions: 1=top-right, 2=bottom-left, 3=top-left, 4=bottom-right. Pick the position that doesn't overlap main content.

**Rules:**
- NEVER code the Joy logo in HTML/CSS (it comes from the PNG)
- NEVER use CSS gradient as background
- Light layouts (1-7): light background
- Dark Glass Bars (4C): dark background

---

## Layout Patterns

| Layout type | Formula | Example |
|---|---|---|
| Stat callout | `[Number] [What it measures]` | `34.3M Active Starbucks Rewards Members` |
| Cards | `[N] [Power word] [Topic]` | `5 Reasons Starbucks Rewards Dominates` |
| Process | `[Verb] [Outcome] in [N] Steps` | `Build Loyalty in 3 Phases` |
| Grid | `[N] [Topic] [Pillars/Dimensions]` | `4 Pillars of Retention Strategy` |
| Comparison | `[Option A] vs [Option B]` | `Transactional vs Emotional Loyalty` |
| Hero | Shortened H1, max 10 words | `Why 34M Members Choose Starbucks Rewards` |

### Spacing & Structure

| Property | Value |
|---|---|
| Canvas size (body images) | 1500 x 1000px |
| Minimum body padding | 60px all sides |
| Hero padding (text bottom-left) | 80px |
| Card border radius | 24px |
| Badge border radius | 14px (square badge), 100px (pill) |
| Card gap (row) | 16-28px depending on count |
| Grid gap | 20px |
| Headline bottom margin | 20-40px |
| Cherokee underline height | 4-6px |

### Card Row Spacing by Count

| Cards | Gap | Card padding | Font sizes |
|---|---|---|---|
| 3 cards | 24px | 36px 28px | title 28px, desc 20px |
| 4 cards | 20px | 28px 20px | title 24px, desc 18px |
| 5 cards | 16px | 24px 16px | title 22px, desc 16px |

---

## Component Library

**Section badge / pill (light bg):**
```html
<div style="
  display: inline-flex; align-items: center; gap: 8px;
  background: #eaf6fb; color: #06038D;
  border-radius: 100px; padding: 6px 16px;
  font-size: 14px; font-weight: 500;
">[Label text]</div>
```

**Cherokee underline accent:**
```html
<div style="
  width: 100px; height: 5px;
  background: #FCD299; border-radius: 3px;
  margin: 16px 0;
"></div>
```

**Navy card (standard):**
```html
<div style="
  background: #06038D; border-radius: 24px;
  padding: 36px 28px;
  display: flex; flex-direction: column; gap: 14px;
">
  <!-- icon badge -->
  <!-- card-title: color #FFFFFF, 28px, weight 600 -->
  <!-- card-desc: color rgba(255,255,255,0.75), 20px, weight 400 -->
</div>
```

**Bittersweet emphasis card (one per image max):**
```html
<div style="
  background: #FF6D6A; border-radius: 24px;
  padding: 36px 28px;
  display: flex; flex-direction: column; gap: 14px;
">
  <!-- badge: background #FFFFFF, icon color #FF6D6A -->
  <!-- card-title: color #FFFFFF, 28px, weight 600 -->
  <!-- card-desc: color rgba(255,255,255,0.85), 20px, weight 400 -->
</div>
```

**Glassmorphism cards:**
All cards use frosted glass treatment: semi-transparent fill + `backdrop-filter: blur(14px)` + subtle white border. Never use fully opaque solid fills for large card areas.

**Glass equivalents for solid colors:**
- Navy glass: `rgba(6,3,141,0.72)`
- Coral glass: `rgba(255,109,106,0.82)`

---

## Design Principles

1. **Cherokee (4 valid uses only):**
   - Headline underline (min 6px bar)
   - Left border accent (6-8px solid)
   - Icon background (48x48px square)
   - Tinted card fill (`rgba(252,210,153,0.2-0.3)`)
   - NEVER: solid large fill, text color, anything > 8px border

2. **Bittersweet with declared purpose:** State why before using. If all items are equal weight, use Frost glass for all.

3. **Never use color as the only signal:** Pair Coral with a distinct icon or label for color-blind accessibility.

4. **Hero headline structure:** 3 lines tapering (widest to narrowest). `max-width: 1350px`, font 84px, weight 700.

5. **Hero subtitle (optional):** Max 1 line, color `rgba(6,3,141,0.75)` (Navy muted, not Cerulean).

6. **Generous rounded corners:** Cards 24px, badges 14px.

---

## Image Count per Article

| Word count | Total images | Breakdown |
|---|---|---|
| < 1,000 words | 2 | 1 hero + 1 body |
| 1,000-1,800 words | 3-4 | 1 hero + 2-3 body |
| 1,800-3,000 words | 4-5 | 1 hero + 3-4 body |
| > 3,000 words | 5-6 | 1 hero + 4-5 body |

**Rules:**
- Never more than 1 image per H2 section
- Minimum 400 words between body images
- Hero image always generated first

---

## Power Vocabulary (for image overlays)

**Approved:** Crush, Dominate, Conquer, Outperform, Command, Arsenal, Limitless, Battle-tested, Unrestricted, Superior

**Banned:** Help, Boost, Might, Could, Easy, Great, Nice, Small business, Try
