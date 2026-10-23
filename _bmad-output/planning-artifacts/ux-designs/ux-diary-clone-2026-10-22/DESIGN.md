---
name: DiaryClone
description: Visual system distilled from all 369 Stoic flow captures for the selected mobile clone and later new components.
status: final
created: 2026-10-22
updated: 2026-10-23
sources:
  - ../../initiative-diary-clone.md
  - ../../briefs/brief-diary-clone-2026-10-22/brief.md
  - ../../../../docs/Stoic/flows/MANIFEST.md
  - CAPTURE-AUDIT.md
colors:
  canvas-warm: '#F3F3F5'
  surface-warm: '#FFFDFE'
  canvas-cool: '#F1F3F4'
  surface-cool: '#FFFFFF'
  ink-primary: '#161616'
  ink-muted: '#626164'
  ink-inverse: '#FFFFFF'
  action-black: '#111111'
  divider: '#EBEBEB'
  chart-blue: '#82A8C2'
  chart-rose: '#E9A8AD'
  switch-on-blue: '#8195D7'
  dark-canvas: '#000000'
  dark-surface: '#111111'
  dark-ink: '#FFFFFF'
typography:
  display:
    note: 'Heavy rounded-looking sans; source typeface and exact metrics unidentified'
  heading:
    note: 'Bold sans for prompts, card titles, and date headings; match each selected capture'
  body:
    note: 'Readable sans for prose and saved journal text; match selected capture wrapping'
  eyebrow:
    note: 'Small uppercase sans with wide tracking for section and record type labels'
  meta:
    note: 'Smaller muted sans for dates, times, hints, chart axes, and secondary copy'
rounded:
  card: 16px
  sheet: 24px
  small: 8px
  full: 9999px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
  '5': 24px
  '6': 32px
components:
  pill-action:
    background: '{colors.action-black}'
    foreground: '{colors.ink-inverse}'
    radius: '{rounded.full}'
  circular-forward:
    background: '{colors.action-black}'
    foreground: '{colors.ink-inverse}'
    radius: '{rounded.full}'
  answer-pill:
    background: '{colors.surface-warm}'
    foreground: '{colors.ink-primary}'
    selected-background: '{colors.action-black}'
    selected-foreground: '{colors.ink-inverse}'
    radius: '{rounded.full}'
  focus-option:
    background: '{colors.surface-warm}'
    foreground: '{colors.ink-primary}'
    selected-background: '{colors.action-black}'
    radius: '{rounded.full}'
  feeling-tile:
    background: '{colors.surface-cool}'
    foreground: '{colors.ink-primary}'
    selected-background: '{colors.action-black}'
    selected-foreground: '{colors.ink-inverse}'
    radius: '{rounded.card}'
  today-card:
    surface: '{colors.surface-cool}'
    hero-surface: '{colors.action-black}'
    foreground: '{colors.ink-primary}'
    hero-foreground: '{colors.ink-inverse}'
    radius: '{rounded.card}'
  entry-card:
    surface: '{colors.surface-cool}'
    foreground: '{colors.ink-primary}'
    radius: '{rounded.card}'
  insight-card:
    surface: '{colors.surface-cool}'
    foreground: '{colors.ink-primary}'
    radius: '{rounded.card}'
  profile-row:
    surface: '{colors.surface-cool}'
    foreground: '{colors.ink-primary}'
    divider: '{colors.divider}'
  reflection-progress:
    active: '{colors.ink-primary}'
    pending: '{colors.divider}'
  bottom-navigation:
    surface: '{colors.canvas-cool}'
    active: '{colors.ink-primary}'
    inactive: '{colors.ink-muted}'
  profile-sheet:
    surface: '{colors.canvas-cool}'
    radius: '{rounded.sheet}'
---

# DiaryClone — Visual System

## Brand & Style

The current task is a faithful transcription of the **selected** Stoic screens, with the brief's excluded controls removed. The same body of 64 flows also supplies a visual grammar for later, genuinely new screens. The [capture evidence index](CAPTURE-AUDIT.md) inventories all 369 reviewed images and maps each rule to exact flow/screen references. A cited reference-only flow is evidence of a reusable pattern, not permission to add that feature now.

**Application rule:** for an included screen, its own capture determines visible geometry, color, typography, illustration and state. Tokens below describe recurring roles and help fill gaps. For a new component without its own selected capture, choose the closest component family and state here, then use the cited examples and exceptions. Do not flatten screen-specific differences into one universal template. The capture's black Mobbin footer/watermark is attribution outside the app, and OS bars, keyboard, picker and permission dialog remain platform UI.

The visual posture is sparse and editorial: a nearly white gray field, bold black headings, restrained gray support copy, white content islands, large unfilled space and clear black or white actions. The surviving bird and other simple motifs should be reproduced as SVG. The onboarding `AI Mentors` card remains visible because the brief explicitly names it; it does not create an AI interaction. Out-of-scope menus, tabs, cards and routes disappear.

## Colors

| Role | Rule | Evidence and exception |
|---|---|---|
| Light canvas and surface | Two **measured flat-color pairs** occur: {colors.canvas-warm}/{colors.surface-warm} and {colors.canvas-cool}/{colors.surface-cool}. Use the pair seen on the host selected screen. | 01/01, 05/02 and 18/02 use the warm family; 04/02–04, 10/02–11, 42/03 and 43/05 use the cool family. **04/01 versus 04/02** differs within Today, so a single global background is incorrect. See [04/01](../../../../docs/Stoic/flows/04-today/screenshots/screen-01.webp) and [04/02](../../../../docs/Stoic/flows/04-today/screenshots/screen-02.webp). |
| Primary and secondary ink | Nearly black for content and action hierarchy; subdued neutral gray for explanations, dates, section markers and disabled labels. | 42/03, 43/05, 59/02, 63/02. The exact {colors.ink-primary}, {colors.ink-muted} and {colors.divider} values are **approximate**, not proven font/border samples. |
| Inverse field | Black/near-black hero or summary with white text. A primary action inside it can reverse to a white pill. | Today hero 04/01, Journey Insights 42/02–03, reference editorial tiles 27/04–05. Black is a purposeful component variant, not a dark global theme. |
| Data and status | Blue current-series/recorded marks, rose mood marks, gray comparison or unavailable data. A blue notification-on state is distinct from black settings switches. | 43/04–12, 44/02, 49/03–06, onboarding 01/06–10, notifications 63/02. {colors.chart-blue}, {colors.chart-rose} and {colors.switch-on-blue} are **approximate sampled roles**; no precise chart legend mapping is inferred from color alone. |
| Future Black mode | Reference-only 60/03–08 swaps canvas to {colors.dark-canvas}, raised surface to {colors.dark-surface} and text to {colors.dark-ink}; blue data remains recognizable. | [60/04](../../../../docs/Stoic/flows/60-switching-to-dark-mode/screenshots/screen-04.webp) and 60/07–08. This describes a later variant; Appearance and dark-mode switching are outside this clone stage. Graphite/Blue options lack complete visual samples. |

Only the two light canvas/surface pairs above were confirmed as recurring **exact RGB flats** in the decoded exports. The remaining hex values are working approximations; verify them against the relevant selected image during implementation. Compression, antialiasing and transparency prevent a frequency count from proving a semantic token. Maintain readable text and control contrast; chart meaning must also appear in labels or accessible descriptions.

## Typography

| Role | Anatomy and use | Evidence / exception |
|---|---|---|
| {typography.display} | Heavy, rounded-looking, often lowercase route title with a terminal period. Use large scale and generous whitespace. | 28/02 `collections.`, 43/02 `trends.`, 44/02 `mood calendar.`, 59/02 `your profile.`. 52/02 has an uppercase date plus `Saturday`; do not force lowercase everywhere. |
| {typography.heading} | Bold prompts, Today card headlines, record titles and completion messages. | 01/01–12, 05/02–08, 10/02–03, 42/03–06. Sentence-case questions stay sentence case. |
| {typography.body} | Regular, comfortable long-form reflection answers and policy paragraphs; wraps and scrolls. | 05/09–10, 10/07–10, 50/02–03, 64/02. Do not rasterize personal writing. |
| {typography.eyebrow} | Small tracked uppercase object or section label, often outside a card or above its title. | 42/03 `REFLECTION`, 43/05 chart sections, 59/02 `ACCOUNT`, 63/02 `DAILY REFLECTIONS`. |
| {typography.meta} | Muted timestamps, subtitles, small chart axes, instructional hints. | 42/03–06, 43/05–12, 63/02. Preserve hierarchy when enlarged by system text settings. |

The capture set does not identify the original font file or provide exact type metrics. The frontmatter roles are deliberate semantic notes, **not** measured font sizes. For selected screens compare rendered line breaks, weight and baseline at 393 × 852 with the image; support dynamic text by reflowing and scrolling instead of clipping.

## Layout & Spacing

Most light screens use a portrait single column with approximately 16 source-screen pixels of side inset, tight gaps between related cards and much larger breathing space between sections. A centered title or illustration can occupy the wide middle field. Bottom navigation and primary actions sit above the safe area. This is a recurring **relationship**, not a universal pixel grid: plots may reach the sides (43/04), media fills a card (50/01), a carousel reveals a neighboring card (13/02–07), and the mood calendar is a broad dot grid (44/02). See 04/01–06, 42/02–06, 43/05–12, 59/02–05.

{spacing.1}–{spacing.6} are provisional implementation steps, **not measured Stoic spacing**. For a selected screen, its capture overrides them. For a new screen, start with close spacing inside one component, a larger gap between cards and the largest gap between conceptual sections; compare the nearest cited family. Longer text, small device heights and native keyboards must allow scrolling rather than hiding content or controls. The 393 × 852 iOS viewport is the comparison baseline, not a clipping box on Android.

## Elevation & Depth

Light cards separate chiefly through white-on-gray tone; hairline borders and very soft shadows are occasional. The source does not support a heavy floating-card shadow as the default. A profile or task sheet uses a visibly darkened underlying route, with a rounded upper edge. A black Today hero or Journey banner is a filled region, not a raised modal. See 04/01–03, 42/02–06, 59/02–05. Shadow radius/opacity are not measured; compare the selected image before implementing an effect.

## Shapes

The shared language is rounded but has distinct families: full capsules for major actions, circles for reflection forward controls and Focus icons, rounded rectangles for emotional choices, varied white cards, and large-radius near-full-height sheets. The {rounded.card}, {rounded.small} and {rounded.sheet} numbers are **starting estimates**; the selected silhouette wins. Evidence: 01/04–05 answer pills, 05/06–08 circular Focus choices, 10/03–06 two-column feeling tiles, 42/03 entry cards, 43/05 chart cards, 59/02 Profile sheet.

Use clean, flat SVG for surviving bird, sun/moon, feather and similar line/silhouette assets, matched to each selected screen's size and position (01/01, 05/02–05, 17/02, 42/02). The broader corpus adds motifs such as birds/balloons (27/02–05) and book stacks (40/02/06/12) as **style evidence only** for a later new asset. User photos or recorded media in 42/04–06 are content, not design-system art.

## Components

The components below name visual anatomy and states. `EXPERIENCE.md` owns their behavior. Frontmatter component values are reusable defaults; a selected capture's exact variant takes precedence. Source IDs and their paths are indexed in [CAPTURE-AUDIT.md](CAPTURE-AUDIT.md).

| Component | Visual anatomy and state | Evidence / exception |
|---|---|---|
| Pill action | Filled near-black capsule with centered white short label; light/outlined secondary; pale gray disabled. On a black hero use white fill and black label. | 01/02–12, 04/01, 22/04, 33/02. A reflection step usually uses a circular control instead. |
| Circular forward | Black disk with white right arrow, parked near lower trailing edge above safe area/keyboard. Its active/disabled treatment is separate from pill geometry. | 05/03–10, 10/02–10. Do not turn 05/02's intro Continue pill into a disk. |
| Answer pill | Horizontal white/outlined capsule for onboarding choices, reversing to dark fill/light label when selected. | 01/02–05. Single/multi choice follows the question, not the pill appearance. |
| Focus option | White circular icon target with black monochrome glyph and caption below; selected state becomes visibly filled or checked. | 05/06–08; 14/02–05 is reference-only customization. Keep its circular anatomy apart from answer pills. |
| Feeling tile | Two-column rounded rectangular choice; selected dark fill with inverse text/icon, unselected white/light. Expanded list keeps the same tile grammar. | 10/03–06; standalone mood tiles 25/03–06 are reference-only. |
| Slider / scale | Thin horizontal track, dark filled portion and round thumb; qualitative readout changes with position. | 05/03–04, 10/02. Do not use the segmented metric creation selector from reference flow 16 as this slider. |
| Reflection progress and editor | Back left, thin segmented progress center, Close right; borderless prompt/answer canvas; `+`/`Aa`/other source accessories only where retained by scope; forward action above keyboard. | 05/02–10, 10/02–10. Remove AI sparkle and excluded attachment paths. Morning 05/11–15 are omitted and progress counts retained steps. |
| Today card | Distinct source states: a dark single Morning hero with inverse action (04/01), paired light tall Morning/Evening cards (04/03), subdued/outlined completed card with saved answer chips (04/02, 10/12). Label, central message and bottom action/summary keep the source hierarchy. | A single white `content-card` is insufficient. `on glowing reviews` and `Get Inspired` are removed. |
| Quote block | Centered quote/attribution with generous vertical space on Today's light surface. | 04/04–06. Favorite, Share and Quote Journal controls from 11/19/20 are excluded. |
| Journey banner and day group | Wide black rounded Insights banner with white title and subdued trailing link; below it a bold relative day plus muted date and chevron. Figures appear only when backed by saved data. | 42/02–06. Source first-journal/Life Event cards and sample figures are excluded. |
| Entry card | Dense white rounded tile: compact glyph and tracked type, bold title, right time; gray prompt over black answer. Long answer wraps. Only actually authored in-scope chips or media may appear. | 42/03–06, 52/02. Journal, mood check-in, exercise, photo and audio source cards are reference-only unless a retained reflection produces that field. |
| Entry detail | Pale full reading page: Back/More chrome, timestamp/type, oversized title, widely spaced prompt/answer blocks; content scrolls. | 50/02–03. More-menu contents/edit screen are uncaptured; `More → Edit` with `Save`/`Cancel` is an owner-approved adaptation, not source transcription. |
| Insight card and chart | Rounded white module with title/gray description, data plot or explicit no-data body, optional scoped drill-down; fine guides, pale axes. Blue current marks, gray comparison, rose mood values have distinct semantic roles. | 43/02–12, 44/01–02, 49/03–06. Hide source-only HealthKit/overflow/chart-customization controls. |
| Period controls | Outlined top period capsule, checked popover, and white floating bottom pager. Weekly/monthly title, axis, dots, labels and pager change as one state. | 49/01–06. Reference chart-view switching 45/01–03 is a different control. |
| Profile row | Uppercase tracked section marker outside grouped white rows; label left, divider between siblings, right chevron/value/switch. Notification rows add two-line muted description, vertical divider, editable time and switch. | 59/02–05, 63/02–04. Keep only Notifications, Privacy and the two scoped morning/evening reminders. |
| Profile sheet | Near-full-height pale root over dark scrim; large root title and top-right Close, title compacts to centered navigation label while scrolling. Nested pages show Back plus parent label and their own title. | 59/02→03–05, 63/02–04, 64/02. Other sheets (22/02, 23/02, 33/02) are distinct future variants, not this fixed geometry. |
| Bottom navigation | Source active item is dark filled icon/label; inactive item is gray outline. Preserve safe-area placement and scale but adapt to **two** destinations, Today and Journey. | 04/01–06, 42/02–06. Source five slots and raised `+` are excluded; the two-item arrangement is a derived scope adaptation. |
| Empty / disabled / completion | No-data chart: pale ring/empty dots and explanatory text (43/02–03/05/07); disabled primary turns gray (61/06); completion uses sparse centered monochrome motif, large heading and next action (05/16–18, 10/11). | Journey's source 42/02 has an excluded journal CTA, so a scoped first-use empty state is newly derived and must not be claimed as a copied image. Reference feedback and achievements remain excluded. |

## Do's and Don'ts

| Do | Don't |
|---|---|
| Compare every included screen with its own image and reproduce its surviving content hierarchy, colors, SVG, dimensions and state. | Replace a selected capture with a generic system card or one of the reference-only screen layouts. |
| For a new component, choose the closest anatomy/state above and inspect the cited few images only if detail remains uncertain. | Re-audit 369 screenshots for every later screen or add a reference-only feature because its example exists. |
| Keep the two light surface families, Today card variants, choice geometries and chart semantic roles distinct. | Treat all white cards, black switches, selection chips or blue marks as interchangeable. |
| Use real saved data for Journey, charts and calendar; expose empty/disabled states honestly. | Copy Mobbin attribution, native iOS chrome, reference sample personal history or dead out-of-scope controls into the app. |
| Mark unmeasured font, spacing, radius and non-flat color values as estimates until per-screen visual QA. | Present a provisional number as an exact Stoic design token. |

The selected source captures govern included screens. For future uncaptured surfaces, this visual spine, `EXPERIENCE.md` and the evidence index form the reusable system; a newly discovered exception should be added with an exact screen citation.
