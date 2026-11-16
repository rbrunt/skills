---
name: Briefing Paper
description: Single-file HTML documents (project plans and findings reports) that read like a printed memo, with interactive extras where the data needs them.
colors:
  archive-paper: "#fbfaf7"
  surface: "#ffffff"
  iron-gall-ink: "#302a24"
  ink-secondary: "#574e44"
  ink-muted: "#706459"
  rule: "#e4e1d9"
  rule-soft: "#efece5"
  table-head: "#f6f4ee"
  control-border: "#c9c0b5"
  saddle-leather: "#805237"
  leather-wash: "#f3eade"
  leather-edge: "#dfcbb9"
  callout-ink: "#513c2d"
  positive: "#1e7a3c"
  positive-wash: "#e4f2e8"
  positive-line: "#bed4c7"
  mixed-ink: "#5d5a1c"
  caution: "#9a5b00"
  caution-wash: "#fbefd6"
  caution-strong: "#7a4d00"
  info: "#2f4fa8"
  info-wash: "#e9eefb"
  diagram-ink: "#1d2330"
  diagram-line: "#4a5262"
  diagram-note-edge: "#c9a15a"
  diagram-note-ink: "#5d3c00"
  scale-0: "#eeeae2"
  scale-1: "#eee0ce"
  scale-2: "#cfad89"
  scale-3: "#a3714e"
  scale-4: "#74472c"
typography:
  display:
    fontFamily: "Iowan Old Style, Charter, Palatino Linotype, Georgia, serif"
    fontSize: "clamp(1.9rem, 4.2vw, 2.7rem)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Iowan Old Style, Charter, Palatino Linotype, Georgia, serif"
    fontSize: "1.625rem"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  title:
    fontFamily: "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 600
    lineHeight: 1.4
  body:
    fontFamily: "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  table:
    fontFamily: "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  small:
    fontFamily: "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "0.04em"
  mono:
    fontFamily: "ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.86em"
    fontWeight: 400
rounded:
  focus: "3px"
  code: "4px"
  control: "5px"
  panel: "8px"
  card: "10px"
  figure: "12px"
  pill: "999px"
spacing:
  paragraph: "1rem"
  subsection: "2rem"
  section: "3rem"
  gutter: "1.5rem"
  gutter-narrow: "1rem"
  cell: "0.75rem"
components:
  callout:
    backgroundColor: "{colors.leather-wash}"
    textColor: "{colors.callout-ink}"
    rounded: "{rounded.card}"
    padding: "1rem 1.25rem"
  callout-good:
    backgroundColor: "{colors.positive-wash}"
    textColor: "{colors.iron-gall-ink}"
    rounded: "{rounded.card}"
    padding: "1rem 1.25rem"
  status-pending:
    backgroundColor: "{colors.caution-wash}"
    textColor: "{colors.caution-strong}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.625rem"
  status-partial:
    backgroundColor: "{colors.info-wash}"
    textColor: "{colors.info}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.625rem"
  status-answered:
    backgroundColor: "{colors.positive-wash}"
    textColor: "{colors.positive}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.625rem"
  table-header:
    backgroundColor: "{colors.table-head}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    padding: "{spacing.cell}"
  table-cell:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.iron-gall-ink}"
    typography: "{typography.table}"
    padding: "{spacing.cell}"
  toc-link:
    textColor: "{colors.ink-secondary}"
    typography: "{typography.small}"
    padding: "0.1rem 0.15rem"
  toc-link-active:
    textColor: "{colors.saddle-leather}"
  button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.iron-gall-ink}"
    rounded: "{rounded.control}"
    padding: "0.45rem 0.7rem"
    height: "2.75rem"
  button-hover:
    backgroundColor: "{colors.leather-wash}"
  button-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.saddle-leather}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: "0.375rem 0.75rem"
    height: "2.25rem"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.iron-gall-ink}"
    rounded: "{rounded.control}"
    padding: "0.45rem 0.7rem"
    height: "2.75rem"
  details-toggle:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.5rem"
    height: "1.75rem"
  code-inline:
    backgroundColor: "{colors.rule-soft}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.mono}"
    rounded: "{rounded.code}"
    padding: "0.08em 0.35em"
---

# Design System: Briefing Paper

## Overview

**Creative North Star: "The Briefing Paper"**

Each document is a single self-contained HTML file. It reads like a well-set printed memo: warm paper, serif section heads, one narrow column of prose, and tables that keep their figures aligned. Interactivity (a filterable explorer, a clickable map, a full-screen diagram) is added only where the data needs it. The page should still make sense printed or with JavaScript off.

The system serves two jobs that share one look. A **project plan** is mostly written by a person for colleagues, with an agent helping on diagrams and layout. A **findings report** is written by an agent for its author to review. Both are read carefully from start to end, so the design favours comprehension over spectacle. It is sized for reading, uses colour sparingly, and puts the structure on show: numbered sections, contents that stay in view, and anchored links.

Colour works like ink on paper. Almost everything is warm neutral. Saddle Leather marks links, the active section, focus, and callouts. Green, amber and blue appear only when they mean something (status, a category, a diagram node), never as decoration.

**Key Characteristics:**
- Single reading column, 56rem wide, with prose capped at 68ch. The column is centred on narrower screens, and on wide screens it is pinned left beside a contents rail.
- Serif display and section heads over a system-sans body; monospace for identifiers.
- Warm neutral palette with a single brown accent and semantic tints.
- Flat: depth comes from white panels on off-white paper and 1px hairlines, never shadows.
- Numbered `h2` sections, each opened by a hairline rule, with contents that track the reader's position: a sticky top bar on narrower screens, a side rail on wide screens.
- Built to print well and to respect reduced motion.

## Colors

Warm, low-chroma paper and ink, with one leather-brown accent and a small set of semantic tints.

### Primary
- **Saddle Leather** (`saddle-leather`): the only accent. Used for links, the active contents-bar entry and its 2px underline, focus outlines, hover borders, the bold lead word in a callout, and the bars in bar charts. It never fills a large area.
- **Leather Wash** (`leather-wash`): callout background, button hover fill, text-selection highlight, the `:target` flash, and flow-diagram blocks.
- **Leather Edge** (`leather-edge`): border for callouts and detail panels; scrollbar thumb.
- **Callout Ink** (`callout-ink`): body text inside a leather callout. A slightly warmer ink so the box reads as a single unit.

### Semantic
- **Positive** / **Positive Wash** (`positive`, `positive-wash`): "answered", "available", good-news callouts (edged with `positive-line`), and the "nodal" category in coded tables. **Mixed Ink** (`mixed-ink`) is the text colour on a half-amber, half-green "mixed" cell.
- **Caution** / **Caution Wash** (`caution`, `caution-wash`): draft status, the "regional" category, and caveats. **Caution Strong** (`caution-strong`) is the text colour on a pending pill, where it needs extra contrast.
- **Info** / **Info Wash** (`info`, `info-wash`): "partial" status, and the node colours in Mermaid diagrams.

### Diagram
Mermaid diagrams run with a custom `themeVariables` block instead of Mermaid's default theme, which is lavender and purple. Nodes use `info-wash` fill with an `info` border and `diagram-ink` text. Lines and signals use `diagram-line`. Notes use `caution-wash` fill with a `diagram-note-edge` border and `diagram-note-ink` text. Keep this block identical in every document.

### Sequential scale
`scale-0` … `scale-4` is a five-step brown ramp for choropleths and heat cells. It runs from empty (`scale-0`) to dense (`scale-4`). Labels switch to white text on `scale-3` and above.

### Neutral
- **Archive Paper** (`archive-paper`): page background; also the background of the sticky contents bar (narrower screens), so it hides content scrolling beneath.
- **Surface** (`surface`): white for tables, figures, detail panels, form controls and code blocks. It is the only "raised" layer.
- **Iron Gall Ink** (`iron-gall-ink`): body text and `h1`/`h2`.
- **Ink Secondary** (`ink-secondary`): `h3`, contents-bar links, inline code text, secondary notes.
- **Ink Muted** (`ink-muted`): meta lines, captions, footers, table headers, list markers.
- **Rule** (`rule`): hairlines above `h2`, around the contents bar, the side rail's link markers, and the borders of tables and figures.
- **Rule Soft** (`rule-soft`): row dividers inside tables, inline code background.
- **Table Head** (`table-head`): table header row.
- **Control Border** (`control-border`): default stroke on buttons, selects and inputs.

### Named Rules
**The One Accent Rule.** Saddle Leather is the only accent colour. In the page chrome, brown means the element can be clicked, is focused, is the current section, or is a callout. Inside a chart frame, brown is the data colour: the first series is Saddle Leather, and further series take the `scale-*` ramp. No other hue is used for data.

**The Colour-Means-Something Rule.** Green, amber and blue are reserved for status, categories, and diagrams. Pair each with a text label or legend; never rely on hue alone.

## Typography

**Display Font:** Iowan Old Style (with Charter, Palatino Linotype, Georgia, serif)
**Body Font:** system UI sans (`ui-sans-serif`, system-ui, -apple-system, Segoe UI, Roboto)
**Label/Mono Font:** system monospace (`ui-monospace`, SF Mono, Menlo, Consolas)

**Character:** A bookish transitional serif sets the document's voice at the top levels. A neutral system sans carries the reading and the data, so the documents load instantly with no web fonts.

### Hierarchy
- **Display** (`h1`): the document title only, balanced across at most two or three lines.
- **Headline** (`h2`): numbered section heads ("3. Now vs later"). Each section starts with a 1px `rule` border and 1.5rem of padding above the heading.
- **Title** (`h3`): sub-sections in sans, coloured `ink-secondary`, so they clearly rank below the serif heads.
- **Body**: prose capped at 68ch (`--measure`), with `text-wrap: pretty`. Use a lead paragraph (1.12rem) once, under the title, when the document opens with a summary.
- **Table**: 0.9375rem with tabular numerals. Numeric columns are right-aligned and do not wrap.
- **Small**: meta line, contents links, captions, footer.
- **Label**: uppercase, 0.04em tracking. Used only for table headers, status pills, and the draft badge.
- **Mono**: inline code, file paths, field names, record IDs.

### Named Rules
**The Two-Voice Rule.** Serif is reserved for `h1`, `h2`, and the occasional large example figure. Everything else is sans. Don't set body copy or `h3` in serif.

**The Measure Rule.** Paragraphs and list items never exceed 68ch, even when the column is wider. Tables and figures may use the full column.

## Layout

One centred column (`max-width: 56rem`) on Archive Paper, with 3.5rem of top padding and 1.5rem gutters. Below 640px the gutters drop to 1rem, the top padding to 2rem, and `h2` spacing to 2.5rem. At 76rem (1216px) and wider, the layout pins to the left of the window instead of centring. The body is 76rem wide with 18.5rem of left padding. The reading column stays 56rem wide, the contents become a side rail 2.5rem from the left edge, and any spare width collects on the right.

Vertical rhythm uses three steps: `paragraph` (1rem), `subsection` (2rem, above `h3`), and `section` (3rem, above `h2`). A document is ordered like this: title, a meta line (author, date, draft badge), an optional lead paragraph, the contents (`nav.toc`), then numbered sections, then a footer above a hairline.

The **contents** have two forms built from the same `nav.toc` markup. Below 76rem, it is a bar that sticks to the top (`position: sticky; top: 0`). Its links wrap onto multiple lines rather than scrolling sideways, and `scroll-padding-top` (about 4.5rem) keeps anchored headings clear of it. At 76rem and wider, it becomes a fixed 13rem side rail. It starts level with the first `h2`, moves up with the page, then sticks 2rem from the top; a small script handles the positioning, and without JavaScript the rail stays 3.5rem from the top. It scrolls on its own if it is taller than the viewport. That suits documents with many sections.

**Tables** sit in a `.table-scroll` wrapper. They keep their reading size (`min-width: 40rem`) and scroll sideways inside the wrapper on narrow screens instead of shrinking.

**Mermaid diagrams** sit in the column at the same width as other figures. The frame matches a chart frame: white Surface, a 1px `rule` border and a 12px radius. The SVG is capped at the column width, at 1.5× its natural width (so small diagrams don't blow up to giant text), and at 68vh tall. Large diagrams rely on the "Full screen" pill button, top-right, to become readable. Without JavaScript, the Mermaid source shows as monospace text.

**Side-by-side layouts** use `.charts` (two columns) or `.charts.three` (three columns), with any number of rows. Both stack into one column below 640px. Use them for small multiples and comparison pairs.

**Wide charts** (heatmaps, full-day line charts) sit in a `.chart-scroll` wrapper. Below 600px they scroll sideways instead of shrinking their text, following the same rule as tables.

**Print:** the contents, controls and full-screen buttons are hidden; tables no longer scroll; collapsed details either expand inline or are dropped; headings avoid page breaks after them; and rows and callouts avoid page breaks inside them.

## Elevation & Depth

Flat. There are no `box-shadow`s for depth anywhere. Layering comes from colour alone. Archive Paper is the base. White Surface is the single raised layer, used for tables, figures, detail panels and controls, and it is always edged by a 1px `rule` or `leather-edge` border. The only shadow in the system is functional: on narrower screens, the contents bar uses `box-shadow: 0 -1rem 0 var(--bg)` to cover content scrolling above it.

### Named Rules
**The Paper Rule.** If it needs to stand out, give it a white surface and a hairline, or a tinted wash. Never a shadow.

## Shapes

Gently softened rectangles, plus capsules for small labels. Inline code uses 4px corners; form controls 5px; detail panels and map frames 8px; tables and callouts 10px; chart and diagram frames 12px. Pills, status tags, `details` toggles and the full-screen button are fully rounded (999px). Borders are always 1px solid hairlines. The exceptions are the 2px marker on the active contents link (an underline in the bar, a left border in the rail) and the 2px focus outline. Tables use `border-collapse: separate` so the 10px outer radius clips cleanly.

## Components

### Buttons
Plain and tactile, like the browser's own controls dressed in paper.
- **Default (form controls):** white surface, 1px `control-border` stroke, 5px radius, at least 2.75rem tall, inheriting body type. On hover the border turns Saddle Leather and the fill turns Leather Wash.
- **Pill (diagram actions):** white, 1px `rule` border, Saddle Leather 600-weight small text, fully rounded, at least 2.25rem tall. On hover the fill turns Leather Wash.
- **Link-button (inside explorer tables):** no chrome. Saddle Leather mono text, underlined.
- **Focus:** every interactive element shows a 2px Saddle Leather outline with a 2px offset and a 3px radius.

### Chips / Status pills
- **Style:** fully rounded, 0.125rem × 0.625rem padding, label type, no border.
- **Variants:** `pending` (caution wash + caution-strong), `partial` (info wash + info), `answered` (positive wash + positive). The draft badge in the meta line uses the caution pair in uppercase.
- **Neutral pill:** `rule-soft` fill with `ink-secondary` text, for counts and tags without a status.

### Callouts
- **Leather callout:** Leather Wash fill, 1px Leather Edge border, 10px radius, 1rem × 1.25rem padding, capped at the 68ch measure. Text is `callout-ink`. A leading bold phrase ("Preference:") takes Saddle Leather.
- **Good callout:** Positive Wash fill with a soft green border, for confirmed findings.
- Use these sparingly. A callout holds a recommendation or a key finding, never ordinary prose.

### Tables
- White surface, 1px `rule` outer border, 10px radius, `rule-soft` row dividers, no divider under the last row.
- Header row: Table Head fill, uppercase label type, Ink Muted text, with a `rule` divider beneath.
- The first column is 600 weight with tabular numerals and does not wrap. Numeric columns are right-aligned.
- **Coded cells:** a Positive Wash or Caution Wash fill with matching 600-weight text marks a category. A 50/50 gradient of both marks "mixed". Always pair these with a legend of small 0.7rem rounded swatches above the table.
- A targeted row (`tr:target`) is tinted Leather Wash.

### Inputs / Fields
- **Style:** same as the default button: white, 1px `control-border` stroke, 5px radius, at least 2.75rem tall. The label sits above the control in 600-weight small text, in a column layout.
- **Focus:** the global 2px Saddle Leather outline.
- **Sliders:** a native `input[type=range]` with `accent-color` set to Saddle Leather, no border, and at least 11rem wide. The current value sits in an `<output>` inside the label text, in 400 weight.
- **Number inputs:** 6rem wide; full width below 640px.
- **Layout:** controls sit in a wrapping flex row aligned to their bottom edge, and go full width below 640px.

### Navigation (contents)
- **Bar (below 76rem):** a wrapping row of section links in small type and `ink-secondary`, between top and bottom `rule` hairlines, sticky on Archive Paper. The active link gets a 2px Saddle Leather underline.
- **Side rail (76rem and up):** an uppercase "Contents" label (label type, Ink Muted) above a vertical list. Each link has a 2px `rule` left border, which turns Saddle Leather on the active section.
- Link text is the heading without its number.
- On hover the link turns Saddle Leather. The active section is tracked by a scroll listener.
- **In-text anchors:** internal `#` links inherit the text colour and get a dotted 1.5px Saddle Leather underline that turns solid and brown on hover. On arrival, the target flashes Leather Wash and fades over 1.8s (`cubic-bezier(0.22, 1, 0.36, 1)`). The flash is turned off under reduced motion.

### Inline details toggle (signature)
Optional depth that costs no vertical space until opened. Inside a list item, `<details>` renders as an inline pill: white fill, `rule` border, label type in Ink Muted, a "+" that becomes "−" when open, at least 1.75rem tall (2.25rem on touch widths). On hover or when open, the text and border turn Saddle Leather. The content opens below as a white panel with an 8px radius, a `rule-soft` border, and table-size text. In print the pill is hidden and the content appears inline.

### Diagram figure (signature)
Mermaid source sits in `<pre class="mermaid">`. A script wraps each block in a framed `figure.diagram` with a "Full screen" pill button and renders it with the shared theme variables (see Colors › Diagram). Fullscreen mode centres the SVG and allows it to fill up to 88vh.

### Code blocks
- `pre.code` is a white surface with a 1px `rule` border and an 8px radius. Text is mono at caption size with 1.6 line height. Wide lines scroll sideways on screen and wrap in print.
- Comments may be wrapped in `.cm` (Ink Muted). There is no other syntax colouring.

### Data figures
Charts are hand-built inline SVG or HTML; there are no chart libraries.
- **Chart frame:** each chart, pair or row sits in `figure.chart-frame`: white Surface, a 1px `rule` border, a 12px radius and 1rem × 1.25rem padding. Each panel has a `.chart-title` (small, 600 weight, `ink-secondary`), and the figure ends with a `figcaption`.
- **Numbering:** figures and tables are numbered ("Figure 2.", "Table 1.") so that prose can refer to them. A table that needs a caption is wrapped in a `figure`. A Mermaid diagram takes a `.caption` paragraph directly after its source block.
- **Axes and labels:** axis lines use `rule`, gridlines `rule-soft`, and reference lines `control-border` dashed. Tick and axis text is Ink Muted at 11–12px with tabular numerals.
- **Series:** the first series is Saddle Leather, and the next ones take `scale-2`, then `scale-4`, then `scale-1` (the `.k1`–`.k4` classes). A context series that the data is read against, such as a price curve, is drawn as an `ink-secondary` line. When two series need telling apart beyond colour, use dashed lines or open versus filled dots, and always add a legend.
- **Bar rows:** a three-column grid (label, track, value). The track is a 0.8rem `rule-soft` bar. Stacked bars place several `.bar` segments in one track. Values are right-aligned with tabular numerals.
- **Heatmaps:** cells take the `scale-0…4` ramp, with a 1px gap between cells and a swatch legend that gives each band's range.
- **Interactive charts:** controls sit at the top of the chart frame and drive both the chart and a `.stats` row of headline figures. Each figure is a serif 1.75rem number above a small Ink Muted label. Render the default state into the HTML, so the page reads the same without JavaScript. Show the controls only from script (set `hidden` in the HTML, then remove it). Mark the stats row `aria-live="polite"`.
- **Choropleth map:** inline SVG regions filled from the `scale-0…4` ramp, with white strokes. Hovering or focusing a region gives it an ink stroke; selecting it gives a 3px Saddle Leather stroke. Regions are keyboard-focusable and expose `aria-pressed`. Include a swatch legend and a caption saying what the map does *not* show.

## Do's and Don'ts

### Do:
- **Do** keep every document a single self-contained HTML file with the `:root` tokens above. The only external dependency is Mermaid, loaded from a CDN, when a document has diagrams.
- **Do** number `h2` sections and list them in `nav.toc`.
- **Do** cap prose at 68ch and let tables, charts and diagrams use the full column width.
- **Do** use tabular numerals and right alignment for every numeric column.
- **Do** give every coloured category or status a text label and a legend.
- **Do** include print and `prefers-reduced-motion` rules in every document.
- **Do** reuse the shared Mermaid `themeVariables` block unchanged.

### Don't:
- **Don't** add shadows, gradients (apart from the "mixed" table cell), or background imagery.
- **Don't** introduce a second accent colour. New categories reuse the semantic tints or the brown scale.
- **Don't** set body text, `h3`, or table text in the serif.
- **Don't** shrink tables to fit narrow screens; let them scroll inside `.table-scroll`.
- **Don't** load web fonts; the font stacks are system-first on purpose.
- **Don't** use a callout for ordinary prose; it marks a recommendation or key finding.
