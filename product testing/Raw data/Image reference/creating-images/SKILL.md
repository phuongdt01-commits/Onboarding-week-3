---
name: creating-images
description: Generate branded blog/article illustrations for Chatty using multiple methods (HTML/CSS, stock images, screenshots, and hybrid approaches). Use when the user needs visuals for blog posts or articles.
argument-hint: "[article-file.md] or custom prompt"
---

## Auto-read mode

When invoked with an article file path, this skill will:
1. Read the article content automatically
2. Analyze structure and suggest image opportunities
3. Wait for user approval before generating

### Usage
```
/creating-images articles/customer-service.md
```

### Step 1: Add markers to article

After reading the article, **ALWAYS insert markers directly into the article file** before asking user which images to create:

1. Analyze article structure
2. **Insert `<!-- IMAGE: thumbnail -->` marker at the very top of the file** (before H1) — always suggest this first
3. Find suitable H2/H3 sections for body images
4. **Insert `<!-- IMAGE: type -->` markers** using Edit tool
5. Add `<!-- Content: ... -->` comment below each marker to describe what will be in the image
6. Show summary to user

**Example markers to insert:**
```markdown
## Types of customer service operations
<!-- IMAGE: infographic -->
<!-- Content: 6 types - Reactive, Proactive, Self-service, Omnichannel, Tiered, Outsourced -->

Customer service operations take different forms...
```

**Then show summary:**
```
Đã thêm markers vào bài viết:

1. **"Types of customer service operations"** (line 25)
   → Type: infographic
   → Content: 6 types (Reactive, Proactive, Self-service...)

2. **"Why important for business growth?"** (line 46)
   → Type: infographic
   → Content: 6 reasons with stats

Bạn muốn tạo ảnh cho phần nào? (all / 1,2 / none)
```

### Step 2: Generate approved images

After user approves, generate images and update article (replace markers with image references).

### What to look for in articles:
- **H2 with numbered lists** → infographic
- **H2 with 2-4 statistics** → stats
- **H2 with comparison/table** → comparison
- **H2 with process steps** → process
- **H2 with key quote** → quote

**Do NOT suggest images for:**
- Intro section (first paragraphs before first H2)
- Sections that are mostly prose without clear data points

**Always suggest thumbnail for:**
- Title/H1 → use `<!-- IMAGE: thumbnail -->` marker (placed before H1)

### Image markers format

If article already has `<!-- IMAGE: type -->` markers, skip Step 1 and generate directly:

```markdown
# Customer service statistics you need to know
<!-- IMAGE: banner -->

## Why customer service matters
<!-- IMAGE: infographic -->
1. Products are easier to copy
2. Support affects reputation at scale
3. Retention pays more than acquisition

## Key statistics
<!-- IMAGE: stats -->
- 89% of customers switch after bad service
- 5x more expensive to acquire than retain
```

**Available marker types:**
| Marker | Creates |
|--------|---------|
| `<!-- IMAGE: thumbnail -->` | Article thumbnail (hero image above title, 1474×907) |
| `<!-- IMAGE: infographic -->` | Infographic from list/points below |
| `<!-- IMAGE: stats -->` | Statistics highlight image |
| `<!-- IMAGE: comparison -->` | Comparison chart/table |
| `<!-- IMAGE: process -->` | Process/flow diagram |
| `<!-- IMAGE: quote -->` | Quote highlight image |

**Note:** Do not use markers in title (H1) or intro section. Only use within H2/H3 content sections.

### Image URL base

All image URLs must use the GitHub raw base URL:
```
https://thulmservice.github.io/thu-chatyy-ava/.claude/skills/creating-images/
```

Full URL format:
```
https://thulmservice.github.io/thu-chatyy-ava/.claude/skills/creating-images/images/[article-slug]/[filename].webp
```

### Generation rules:

**If article already has markers:**
1. Find all `<!-- IMAGE: type -->` markers
2. Extract content from surrounding context (H2 title + list items below)
3. Generate images using the specified type
4. Save to `images/[article-slug]/` folder
5. Replace marker with image reference format below (using full GitHub URL)

**If article has no markers (ALWAYS do this first):**
1. Analyze article structure
2. **INSERT markers into the article file** using Edit tool (NOT just list them in chat)
3. Add `<!-- Content: ... -->` below each marker
4. Show summary with line numbers to user
5. Wait for user selection (all / specific numbers / none)
6. Generate selected images
7. Replace markers with image references

### Image reference format in articles

After generating images, replace markers with this format (using full GitHub URL):
```
[[IMG_1]]: https://thulmservice.github.io/thu-chatyy-ava/.claude/skills/creating-images/images/article-slug/filename.webp
Alt text: Four types of customer service benchmarking: internal, competitive, industry, and best in class
```

**Important:** `[[IMG_N]]:` and `Alt text:` must be on separate lines.

**Rules:**
- `IMG_` number is sequential (1, 2, 3...) from top to bottom of article
- Always use the full GitHub raw URL (not relative path)
- Alt text describes the **content** of the image, not the design
- Alt text should be a clear, concise description of what the image illustrates

**Examples:**
```
[[IMG_1]]: https://thulmservice.github.io/thu-chatyy-ava/.claude/skills/creating-images/images/customer-service/why-cs-matters.webp
Alt text: Four reasons why customer service matters: products are easier to copy, support affects reputation, retention pays more than acquisition, trust decides loyalty

[[IMG_2]]: https://thulmservice.github.io/thu-chatyy-ava/.claude/skills/creating-images/images/customer-service/cs-statistics.webp
Alt text: Key customer service statistics showing 89% switch rate after bad service and 5x acquisition cost
```

### Custom prompt mode
If user provides specific instructions instead of file path, follow those instructions:
```
/creating-images
Title: Why customer service matters?
Items:
1. Products are easier to copy
2. Support affects reputation
```

---

This skill creates branded blog/article illustrations for Chatty using multiple approaches:
1. **HTML/CSS → Image** (Infographics with custom layouts)
2. **Stock Images** (Curated from stock photo providers)
3. **Screenshots** (Real product screenshots or mockups)
4. **Hybrid Approach** (Stock image/screenshot + branded text + icons overlay)

## Image Types & When to Use Each

| Type | Best For | Examples |
|------|----------|----------|
| **Infographic (HTML/CSS)** | Custom layouts, process steps, statistics, comparisons | Numbered lists, pillars, timelines, charts |
| **Stock Images** | Real-world scenarios, people, environments, concepts | Customer journey mockups, office scenes, tech illustrations |
| **Screenshots** | Actual product features, real UI, software demos | Platform walkthroughs, feature highlights |
| **Hybrid (Stock + Overlay)** | Combining real images with branded text & icons | Customer behavior callouts, feature highlights, stat overlays |

## Design Philosophy

**Fixed brand elements + Creative freedom for layout.**

### For Thumbnail Images:
**FIXED (không thay đổi):**
- **Background**: `data/templates/background_thumbnail.png` (auto-embedded via `{{BACKGROUND_THUMBNAIL_BASE64}}`)
- **Canvas size**: 1474 x 907 px
- **Output**: WebP, < 100KB
- **Text color**: White only (no yellow cards, no black)
- **Font**: Clash Display
- **Logo**: Already in background template (top-right)
- **Layout structure** (từ 3 ảnh mẫu):
  - Text block: bottom-left, padding ~80px
  - Line 1 (title): large bold — ~96px, font-weight 700
  - Line 2 (subtitle): smaller, regular/medium — ~50px, font-weight 400–500
  - 1 decorative inline icon/symbol kèm theo text (spark ✦, circle ◯, chat bubble, etc.)
  - Minimal — chỉ text + icon, không có card/shape phụ

**FLEXIBLE:**
- Font size (scale theo độ dài text)
- Line break của title (split chiến lược để đẹp)
- Loại icon đi kèm (phù hợp với topic bài viết)
- Icon đặt sau title dòng 1 hay sau subtitle dòng 2

---

### For HTML/CSS Infographics:
**FIXED (không thay đổi):**
- **Background**: `data/templates/background.png` (auto-embedded via placeholder)
- **Canvas size**: 1500 x 1000 px
- **Output**: WebP, < 100KB
- **Colors**: Yellow #FBC80B, White #FFFFFF, Black #000000
- **Font**: Clash Display (auto-embedded via placeholder)
- **Logo**: Already in background template (top-right)

**FLEXIBLE (Claude tự do sáng tạo):**
- Layout (flexbox, grid, absolute positioning)
- Shapes (pills, cards, circles, badges, etc.)
- Icons (inline SVG)
- Font sizes and weights
- Spacing and positioning
- Any CSS styling that fits brand colors

### For Stock/Screenshot Images:
**FIXED:**
- **Canvas size**: 1500 x 1000 px
- **Output**: WebP or original format
- **Brand integration**: Optional Chatty logo/watermark placement
- **Colors**: Should align with Chatty brand when possible

**FLEXIBLE:**
- Source image selection
- Cropping/framing
- Overlay elements (callouts, badges, text)
- Filter adjustments (brightness, contrast)

## Content Rules

**DO NOT generate or make up content.** All text must be provided by the user.

- **If user provides content**: Use it exactly as given
- **If content is missing**: Ask user to provide the specific text needed

**For Stock/Screenshot Images:**
- Always ask user what specific scenario/product they want
- Specify which services to use (Unsplash, Pexels, screenshot from actual platform)
- Do not describe or assume what the image should look like

## Placeholders

Script tự động replace các placeholders:

| Placeholder | Description |
|-------------|-------------|
| `{{BACKGROUND_BASE64}}` | Background image (infographic) embedded as base64 |
| `{{BACKGROUND_THUMBNAIL_BASE64}}` | Thumbnail background image embedded as base64 |
| `{{FONT_CLASH_DISPLAY}}` | @font-face declarations for Clash Display |

## Creating Images

### Step 1: Claude generates HTML

Claude tạo HTML file với placeholders và creative layout.

**IMPORTANT — File save location:** Always save temp HTML files to `.claude/skills/creating-images/temp/` folder, NOT the root. Use descriptive names: `temp_[article-slug]_[image-type].html`

Example: `.claude/skills/creating-images/temp/temp_saas-retention_thumbnail.html`

### Step 2: Run script

```bash
python .claude/skills/creating-images/scripts/html_to_image.py \
  --file .claude/skills/creating-images/temp/temp.html \
  images/output.webp
```

## HTML Template Structure

### Thumbnail Template (1474×907)

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    {{FONT_CLASH_DISPLAY}}

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      width: 1474px;
      height: 907px;
      font-family: 'Clash Display', sans-serif;
      background-image: url('{{BACKGROUND_THUMBNAIL_BASE64}}');
      background-size: cover;
      background-position: center;
      position: relative;
      overflow: hidden;
    }

    .text-block {
      position: absolute;
      bottom: 80px;
      left: 80px;
    }

    .title {
      color: #FFFFFF;
      font-size: 96px;
      font-weight: 700;
      line-height: 1.05;
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .subtitle {
      color: #FFFFFF;
      font-size: 50px;
      font-weight: 400;
      line-height: 1.2;
      margin-top: 8px;
      display: flex;
      align-items: center;
      gap: 14px;
    }

    /* Inline icon — dùng inline SVG hoặc unicode symbol */
    .icon {
      display: inline-flex;
      align-items: center;
      opacity: 0.85;
    }
  </style>
</head>
<body>
  <div class="text-block">
    <div class="title">
      Free chatbot
      <!-- Optional: add icon here -->
    </div>
    <div class="subtitle">
      for Shopify stores
      <!-- Optional: add icon here -->
    </div>
  </div>
</body>
</html>
```

**Icon examples (inline SVG, white, ~48px):**
```html
<!-- Spark / AI ✦ -->
<span class="icon">
  <svg width="48" height="48" viewBox="0 0 24 24" fill="white"><path d="M12 2l2.4 7.4H22l-6.2 4.5 2.4 7.4L12 17l-6.2 4.3 2.4-7.4L2 9.4h7.6z"/></svg>
</span>

<!-- Chat bubble ◯ -->
<span class="icon">
  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
</span>

<!-- Circle outline -->
<span class="icon">
  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><circle cx="12" cy="12" r="10"/></svg>
</span>
```

---

### Infographic Template (1500×1000)

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    {{FONT_CLASH_DISPLAY}}

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      width: 1500px;
      height: 1000px;
      font-family: 'Clash Display', sans-serif;
      background-image: url('{{BACKGROUND_BASE64}}');
      background-size: cover;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 80px 60px;
    }

    /* Brand colors */
    .yellow { background: #FBC80B; }
    .white { color: #FFFFFF; }
    .black { color: #000000; }
  </style>
</head>
<body>
  <!-- Claude adds creative content here -->
</body>
</html>
```

## Example: Pills with Icons

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    {{FONT_CLASH_DISPLAY}}

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      width: 1500px;
      height: 1000px;
      font-family: 'Clash Display', sans-serif;
      background-image: url('{{BACKGROUND_BASE64}}');
      background-size: cover;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 80px 60px;
    }

    h1 {
      color: #FFFFFF;
      font-size: 72px;
      font-weight: 600;
      text-align: center;
      margin-bottom: 50px;
    }

    .pills {
      display: flex;
      flex-direction: column;
      gap: 22px;
      width: 96%;
    }

    .pill {
      background: #FBC80B;
      border-radius: 100px;
      padding: 24px 40px;
      display: flex;
      align-items: center;
      gap: 25px;
    }

    .number {
      background: #000000;
      color: #FFFFFF;
      min-width: 60px;
      height: 60px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      font-weight: 600;
    }

    .text {
      color: #000000;
      font-size: 34px;
      font-weight: 500;
      flex: 1;
      text-align: center;
    }

    .icon {
      width: 50px;
      height: 50px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .icon svg {
      width: 40px;
      height: 40px;
      fill: #000000;
    }
  </style>
</head>
<body>
  <h1>Why customer service matters?</h1>
  <div class="pills">
    <div class="pill">
      <span class="number">1</span>
      <span class="text">Products are easier to copy</span>
      <span class="icon">
        <svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
      </span>
    </div>
    <!-- More pills... -->
  </div>
</body>
</html>
```

## Creating Different Image Types

### 1. HTML/CSS Infographics (Branded custom layouts)

**When to use:** Custom process flows, numbered steps, statistics, comparisons, custom illustrations

**Process:**
- Claude generates HTML with brand colors (#FBC80B, #FFFFFF, #000000)
- Uses placeholders: `{{BACKGROUND_BASE64}}`, `{{FONT_CLASH_DISPLAY}}`
- Run: `python .claude/skills/creating-images/scripts/html_to_image.py --file .claude/skills/creating-images/temp/temp.html images/output.webp`

**Examples:** Pills layout, numbered items, grid layouts, timelines

---

### 2. Stock Images (Real-world photos)

**When to use:** Generic scenarios, people interactions, office environments, concepts

**Process:**
1. **Identify need:** Ask user what scenario is needed
2. **Search stock providers:**
   - Unsplash (free, high quality) - unsplash.com
   - Pexels (free, curated) - pexels.com
   - Shutterstock (paid premium) - shutterstock.com
   - iStock (paid) - istockphoto.com

3. **Download & Place:** Save to `images/` folder with descriptive name
4. **Brand it:** Optional - add Chatty watermark or logo placement

**Example:** If user needs "customer collaboration image" → search Unsplash for "team collaboration" or "customer service"

---

### 3. Screenshots (Real product features)

**When to use:** Actual product UI, feature walkthroughs, real platform demonstrations

**Process:**
1. **Source:** Take screenshot from actual product/platform
2. **Capture:** Use browser dev tools or screenshot tool to capture at 1500x1000px
3. **Enhance:** Optional - add Chatty branding, crop, or frame design
4. **Save:** Store in `images/` folder

**Example:** For "Salesforce CRM" article → capture actual Salesforce interface screenshot

---

### 4. Hybrid Approach (Stock/Screenshot + Branded Overlay)

**When to use:** Adding context to images with branded text, callouts, icons, or stat overlays

**Like example images:**
- Image 1: Infographic with quote box + illustration
- Image 3: Dashboard screenshot with "Customer behavior" callout box

**Process:**

**Method A: HTML/CSS with Background Image**
```html
<body>
  <!-- Use stock image or screenshot as background -->
  <style>
    body {
      background-image: url('data:image/...'); /* stock image as base64 */
      background-size: cover;
      background-position: center;
    }
    
    /* Add overlay text/icons/callouts on top */
    .overlay-box {
      background: rgba(91, 33, 182, 0.95);
      border: 3px solid #FFFFFF;
      border-radius: 20px;
      padding: 40px;
      color: #FFFFFF;
    }
  </style>
  
  <div class="overlay-box">
    <h2>Key Insight</h2>
    <p>Your text here</p>
  </div>
</body>
```

**Method B: Design Tool + Export**
1. Use Figma/Canva to place stock image
2. Add branded text boxes, callout badges, icons
3. Export as 1500x1000px WebP
4. Save to `images/` folder

---

## Creative Layout Ideas

Claude có thể tự do sáng tạo với CSS:

| Layout | CSS Approach |
|--------|--------------|
| Pills | flexbox column, border-radius: 100px |
| Grid | display: grid, grid-template-columns |
| Cards | flexbox wrap, box-shadow |
| Zigzag | grid with alternating alignment |
| Timeline | flexbox with connecting lines |
| Comparison | two-column grid |
| Overlay | absolute positioned boxes on background image |
| Callout boxes | semi-transparent background with icons |

## Icons

Use inline SVG for icons. Common icons:

```html
<!-- Copy/Duplicate -->
<svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>

<!-- Checkmark -->
<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>

<!-- Money/Dollar -->
<svg viewBox="0 0 24 24"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z"/></svg>

<!-- Heart/Love -->
<svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>

<!-- Star -->
<svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>

<!-- Chart/Growth -->
<svg viewBox="0 0 24 24"><path d="M3.5 18.49l6-6.01 4 4L22 6.92l-1.41-1.41-7.09 7.97-4-4L2 16.99z"/></svg>
```

## Output Requirements by Image Type

### Thumbnail Images
- **Format**: WebP
- **Size**: 1474 x 907 px
- **File size**: < 100KB
- **Location**: `images/[article-slug]/thumbnail.webp`
- **Process**: Generate HTML with `{{BACKGROUND_THUMBNAIL_BASE64}}` → Run script → Output
- **Script**: `python .claude/skills/creating-images/scripts/html_to_image.py --file .claude/skills/creating-images/temp/temp_thumbnail.html images/[slug]/thumbnail.webp`

### HTML/CSS Infographics
- **Format**: WebP
- **Size**: 1500 x 1000 px
- **File size**: < 100KB
- **Location**: `images/` folder
- **Process**: Generate HTML → Run script → Output

### Stock Images
- **Format**: WebP or JPEG (optimized)
- **Size**: 1500 x 1000 px (crop/resize as needed)
- **File size**: < 150KB
- **Location**: `images/` folder (organized by topic)
- **Source**: Unsplash, Pexels, or other stock providers
- **Attribution**: Include attribution comment if required by license

### Screenshots
- **Format**: WebP or PNG (transparency if needed)
- **Size**: 1500 x 1000 px (or actual capture size)
- **File size**: < 200KB
- **Location**: `images/` folder
- **Note**: Capture from real products/platforms

### Hybrid (Stock + Overlay)
- **Format**: WebP
- **Size**: 1500 x 1000 px
- **File size**: < 150KB
- **Location**: `images/` folder
- **Process**: Base image + HTML/CSS overlay OR Design tool (Figma/Canva) → Export

## Stock Image Resources

### Free Stock Photo Providers

| Provider | URL | Quality | Keywords |
|----------|-----|---------|----------|
| **Unsplash** | unsplash.com | High | Search by keyword, no attribution needed |
| **Pexels** | pexels.com | High | Curated collections, free license |
| **Pixabay** | pixabay.com | Good | Thousands of images, free for commercial use |

### Search Keywords for Common Scenarios

| Topic | Keywords to Search |
|-------|-------------------|
| Customer Service | "customer support", "headset call center", "help desk", "customer care" |
| Team Collaboration | "team meeting", "brainstorming", "collaboration", "remote team" |
| Technology/CRM | "dashboard analytics", "software interface", "computer screen", "data" |
| Business Growth | "startup", "growth chart", "success", "team building" |
| Communication | "chat", "messaging", "conversation", "discussion" |

### How to Use Stock Images:
1. Visit Unsplash/Pexels with relevant keyword
2. Find high-quality image that fits the blog topic
3. Download full-size version
4. Resize/crop to 1500x1000px if needed
5. Save to `images/` folder with descriptive name
6. Use in blog post

---

## Clash Display Font Weights

| Weight | CSS Value | Usage |
|--------|-----------|-------|
| Extralight | 200 | - |
| Light | 300 | Subtle text |
| Regular | 400 | Body text |
| Medium | 500 | Item text |
| Semibold | 600 | Headlines |
| Bold | 700 | Strong emphasis |

---

## Example Interactions by Image Type

### Example 1: Create an Infographic

**User provides:**
```
/creating-images
Title: Why customer service matters?
Items:
1. Products are easier to copy
2. Support affects reputation at scale
3. Retention pays more than acquisition
4. Trust decides long-term loyalty
```

**Claude should:**
1. Create creative HTML/CSS layout with pillars/pills
2. Add relevant icons as inline SVG
3. Save as temp HTML file
4. Run html_to_image.py script
5. Output to images/ folder

---

### Example 2: Use Stock Image

**User provides:**
```
I need an image showing "team collaboration" for the customer service article
```

**Claude should:**
1. Guide user to search Unsplash/Pexels with keywords like "team collaboration", "customer service team"
2. Recommend downloading a specific image
3. Ask: "Should I help resize it to 1500x1000px and save to images/ folder?"
4. Confirm filename and placement

---

### Example 3: Hybrid Approach (Stock + Overlay)

**User provides:**
```
Take a screenshot of our platform's dashboard and add a text callout box explaining the customer behavior tracking feature
```

**Claude should:**
1. Ask where/how to get the screenshot (from actual platform or user provides)
2. Generate HTML with base image + overlay callout boxes
3. Use semi-transparent backgrounds with Chatty brand colors
4. Include icons and key insights
5. Render to WebP and save

---

## Decision Tree: Which Image Type to Use?

```
User needs an image
    ├─ Has custom text/steps/process?
    │   └─ YES → HTML/CSS Infographic
    │
    ├─ Is it a real-world scenario (people, office, etc.)?
    │   └─ YES → Stock Image
    │
    ├─ Is it actual software/product UI?
    │   └─ YES → Screenshot
    │
    └─ Is it stock image + branded callouts/text?
        └─ YES → Hybrid Approach
```

---

## Image Naming Convention

Save images with descriptive names following this pattern:

```
images/[article-topic]/[description]-[type].webp

Examples:
images/crm-marketing/why-crm-marketing-infographic.webp
images/customer-service/team-collaboration-stock.webp
images/dashboards/analytics-dashboard-screenshot.webp
images/features/customer-behavior-hybrid.webp
```

---
