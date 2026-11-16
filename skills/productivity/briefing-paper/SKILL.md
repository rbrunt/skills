---
name: briefing-paper
description: Single-file HTML documents in the Briefing Paper house style. Use when writing a project plan, a findings report, or any review document as HTML, or when restyling one to match.
---

# Briefing Paper documents

Two document types share this style:
- **Project plans:** the user writes most of the prose; you help with diagrams and layout.
- **Findings reports:** you write them for the user to review.

[`DESIGN.md`](DESIGN.md) is the source of truth for tokens, components and rules. [`template.html`](template.html) implements it: the full stylesheet, the Mermaid setup, the contents script (active section, and side-rail positioning on wide screens), and one example of each component.

## Building a document

1. Read `DESIGN.md`, then copy `template.html` to the output path.
2. Fill the body in this order: `h1`, then a `.meta` line (author, date, and a `.status` badge while the document is a draft), then the `.lead` summary, then `nav.toc`, then numbered `h2` sections, then the `footer`.
   - Give each `h2` an `id`, and add a `nav.toc` link to it using the heading text without the number. The active-section script matches links to headings by `href`.
   - **Plans** run Intro → Motivation → changes → Open questions. The open questions go in a table with `.st` status pills.
   - **Reports**: the `.lead` gives the answer in one paragraph. Section 1 is a "Readout" of numbered findings plus a recommendation callout. The report closes with caveats and scope or calculation notes.
3. Keep only the template components the content uses, and delete the example content. If the document has no diagrams, delete the Mermaid `<script type="module">` block. Write diagrams as `<pre class="mermaid">`, each followed by a `.caption`, and keep the theme block unchanged. Diagrams sit at column width; large ones rely on the Full screen button, so a diagram that's dense at column width is fine.
4. Build charts as inline SVG or HTML using the template's chart classes (`chart-frame`, `.charts` / `.charts.three`, `svg.chart`, `.k1`–`.k4`). Compute values in inline JS or embed them as JSON; use no chart libraries. Interactive charts render their default state into the HTML, and the script redraws them (see `#explorer` in the template).
5. Give any new component a colour from the `:root` tokens and follow `DESIGN.md`'s rules for it. Interactive extras go in reports only where the data needs them.

The document is done when:
- it is one file with no local assets;
- it fits a 375px viewport, with wide tables scrolling inside `.table-scroll`;
- it reads correctly with JavaScript disabled;
- at 1280px the contents sit in the side rail, starting level with the first `h2`;
- print preview hides the contents and controls;
- every colour in it is a `:root` token or a value listed in `DESIGN.md`.

## Writing findings reports

Put the answer first. Every number traces to a source, a query, or a calculation stated in the scope notes. Each table, chart or map gets a caption saying what it covers and what it leaves out. A callout holds a recommendation or key finding; everything else is prose.
