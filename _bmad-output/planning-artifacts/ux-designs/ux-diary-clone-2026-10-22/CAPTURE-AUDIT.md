# Stoic capture evidence index

This index is the reusable source map for the DiaryClone [visual spine](DESIGN.md) and [experience spine](EXPERIENCE.md). It records what the whole reference corpus shows; it does **not** expand this phase's implementation scope.

## Audit method and limits

All **369 of 369 screenshots in 64 flows** were visually reviewed in numbered order, using contact sheets and individual enlargements where needed. Counts were checked against the [flow manifest](../../../../docs/Stoic/flows/MANIFEST.md) and the image files. The three working reports preserve fuller observations: [01–21](.working/audit-01-21.md), [22–42](.working/audit-22-42.md), [43–64](.working/audit-43-64.md). Flow/screen references such as `42/03` mean `docs/Stoic/flows/42-journey/screenshots/screen-03.webp`; the flow links below open its README, from which each numbered screenshot is available. Representative evidence links in the rule table open exact images directly.

The comparison target is the captured **393 × 852 iOS app composition**. Files have varying exported pixel dimensions. The dark `stoic. / curated by Mobbin` strip, watermark, iOS status bar, home indicator, native keyboard, and OS alerts are not Stoic app-designed UI. Platform UI is described only where it affects behavior.

Flat-color counting method: decode each original WebP to RGB with Pillow; omit the top 6% (mostly status chrome) and bottom 8% (home-indicator/Mobbin region); count occurrences of **exact RGB triplets** in the remaining rectangular image, then visually confirm that a frequent color occupies a flat canvas/card region. For example, `04/01` has `#F3F3F5` canvas (332,119 counted pixels) and `#FFFDFE` card (191,804); `04/02` has `#F1F3F4` canvas (633,325) and `#FFFFFF` card (222,546); `42/03` has `#FFFFFF` card (372,743) and `#F1F3F4` canvas (202,948). These are evidence of **two captured light-surface families**, including a difference *within Today*. Counts are from the export's decoded pixels, not original design files. Compression, antialiasing, shadows, photos and overlapping controls affect counts; pixel frequency cannot identify semantic role alone or prove exact typography, corner radius, spacing or gradients. Such numeric tokens in DESIGN.md remain provisional until compared to the selected individual capture.

## Complete flow inventory

| No. | Flow and source | Images reviewed | Scope for this clone |
|---:|---|---:|---|
| 01 | [Onboarding](../../../../docs/Stoic/flows/01-onboarding/README.md) | 13/13 | Selected 01–12; 13 excluded (paywall) |
| 02 | [Subscribing to premium](../../../../docs/Stoic/flows/02-subscribing-to-premium/README.md) | 13/13 | Reference only |
| 03 | [Premium + AI features](../../../../docs/Stoic/flows/03-premium-ai-features/README.md) | 4/4 | Reference only |
| 04 | [Today](../../../../docs/Stoic/flows/04-today/README.md) | 6/6 | Selected; omit reviews/Get Inspired |
| 05 | [Logging a daily reflection (morning)](../../../../docs/Stoic/flows/05-logging-a-daily-reflection-morning/README.md) | 18/18 | Selected 01–10, 16–18; AI 11–15 excluded |
| 06 | [Recording a voice note](../../../../docs/Stoic/flows/06-recording-a-voice-note/README.md) | 6/6 | Reference only |
| 07 | [Drawing a sketch](../../../../docs/Stoic/flows/07-drawing-a-sketch/README.md) | 4/4 | Reference only |
| 08 | [Editing text format](../../../../docs/Stoic/flows/08-editing-text-format/README.md) | 4/4 | Reference only |
| 09 | [Asking AI for insights](../../../../docs/Stoic/flows/09-asking-ai-for-insights/README.md) | 5/5 | Reference only |
| 10 | [Logging a daily reflection (evening)](../../../../docs/Stoic/flows/10-logging-a-daily-reflection-evening/README.md) | 12/12 | Selected |
| 11 | [Quote journal](../../../../docs/Stoic/flows/11-quote-journal/README.md) | 2/2 | Reference only |
| 12 | [Personalizing page content](../../../../docs/Stoic/flows/12-personalizing-page-content/README.md) | 4/4 | Reference only |
| 13 | [Adding prompts to daily reflections](../../../../docs/Stoic/flows/13-adding-prompts-to-daily-reflections/README.md) | 15/15 | Reference only |
| 14 | [Adding a focus](../../../../docs/Stoic/flows/14-adding-a-focus/README.md) | 8/8 | Reference only |
| 15 | [Hiding a focus](../../../../docs/Stoic/flows/15-hiding-a-focus/README.md) | 4/4 | Reference only |
| 16 | [Adding a metric to daily reflections](../../../../docs/Stoic/flows/16-adding-a-metric-to-daily-reflections/README.md) | 8/8 | Reference only |
| 17 | [Tomorrow](../../../../docs/Stoic/flows/17-tomorrow/README.md) | 2/2 | Selected |
| 18 | [Inspirations](../../../../docs/Stoic/flows/18-inspirations/README.md) | 8/8 | Reference only |
| 19 | [Share a prompt](../../../../docs/Stoic/flows/19-share-a-prompt/README.md) | 4/4 | Reference only |
| 20 | [Favoriting a prompt](../../../../docs/Stoic/flows/20-favoriting-a-prompt/README.md) | 2/2 | Reference only |
| 21 | [Choosing a card theme](../../../../docs/Stoic/flows/21-choosing-a-card-theme/README.md) | 3/3 | Reference only |
| 22 | [Choosing a prompt category](../../../../docs/Stoic/flows/22-choosing-a-prompt-category/README.md) | 4/4 | Reference only |
| 23 | [Favoriting exercises](../../../../docs/Stoic/flows/23-favoriting-exercises/README.md) | 5/5 | Reference only |
| 24 | [Logging a journal entry](../../../../docs/Stoic/flows/24-logging-a-journal-entry/README.md) | 4/4 | Reference only |
| 25 | [Logging a mood check-in](../../../../docs/Stoic/flows/25-logging-a-mood-check-in/README.md) | 12/12 | Reference only |
| 26 | [Giving a feedback](../../../../docs/Stoic/flows/26-giving-a-feedback/README.md) | 2/2 | Reference only |
| 27 | [Library](../../../../docs/Stoic/flows/27-library/README.md) | 5/5 | Reference only |
| 28 | [Collections](../../../../docs/Stoic/flows/28-collections/README.md) | 2/2 | Reference only |
| 29 | [Collection detail](../../../../docs/Stoic/flows/29-collection-detail/README.md) | 4/4 | Reference only |
| 30 | [Completing a lesson](../../../../docs/Stoic/flows/30-completing-a-lesson/README.md) | 6/6 | Reference only |
| 31 | [Weekly themes](../../../../docs/Stoic/flows/31-weekly-themes/README.md) | 5/5 | Reference only |
| 32 | [Breathe](../../../../docs/Stoic/flows/32-breathe/README.md) | 4/4 | Reference only |
| 33 | [Completing an exercise (breathing)](../../../../docs/Stoic/flows/33-completing-an-exercise-breathing/README.md) | 7/7 | Reference only |
| 34 | [Setting up exercise preferences](../../../../docs/Stoic/flows/34-setting-up-exercise-preferences/README.md) | 9/9 | Reference only |
| 35 | [Lesson detail](../../../../docs/Stoic/flows/35-lesson-detail/README.md) | 3/3 | Reference only |
| 36 | [Meditate](../../../../docs/Stoic/flows/36-meditate/README.md) | 4/4 | Reference only |
| 37 | [Completing an exercise (meditation)](../../../../docs/Stoic/flows/37-completing-an-exercise-meditation/README.md) | 6/6 | Reference only |
| 38 | [Customizing background sounds](../../../../docs/Stoic/flows/38-customizing-background-sounds/README.md) | 7/7 | Reference only |
| 39 | [Pausing an exercise](../../../../docs/Stoic/flows/39-pausing-an-exercise/README.md) | 3/3 | Reference only |
| 40 | [Completing an exercise (walking meditation)](../../../../docs/Stoic/flows/40-completing-an-exercise-walking-meditation/README.md) | 12/12 | Reference only |
| 41 | [Searching stoic.](../../../../docs/Stoic/flows/41-searching-stoic/README.md) | 7/7 | Reference only |
| 42 | [Journey](../../../../docs/Stoic/flows/42-journey/README.md) | 6/6 | Selected; scoped records only |
| 43 | [Trends & insights](../../../../docs/Stoic/flows/43-trends-insights/README.md) | 12/12 | Selected; scoped data only |
| 44 | [Mood calendar](../../../../docs/Stoic/flows/44-mood-calendar/README.md) | 2/2 | Selected; evening feelings only |
| 45 | [Switching data views](../../../../docs/Stoic/flows/45-switching-data-views/README.md) | 3/3 | Reference only |
| 46 | [Hiding a chart](../../../../docs/Stoic/flows/46-hiding-a-chart/README.md) | 3/3 | Reference only |
| 47 | [Excluding words](../../../../docs/Stoic/flows/47-excluding-words/README.md) | 7/7 | Reference only |
| 48 | [Removing an excluded word](../../../../docs/Stoic/flows/48-removing-an-excluded-word/README.md) | 3/3 | Reference only |
| 49 | [Sorting by months](../../../../docs/Stoic/flows/49-sorting-by-months/README.md) | 6/6 | Selected |
| 50 | [Entry detail](../../../../docs/Stoic/flows/50-entry-detail/README.md) | 4/4 | Selected; morning/evening only |
| 51 | [Listening to a voice recording](../../../../docs/Stoic/flows/51-listening-to-a-voice-recording/README.md) | 2/2 | Reference only |
| 52 | [Daily entries](../../../../docs/Stoic/flows/52-daily-entries/README.md) | 2/2 | Selected; scoped entries only |
| 53 | [Filtering entries](../../../../docs/Stoic/flows/53-filtering-entries/README.md) | 4/4 | Reference only |
| 54 | [Sorting entries](../../../../docs/Stoic/flows/54-sorting-entries/README.md) | 4/4 | Reference only |
| 55 | [Badges](../../../../docs/Stoic/flows/55-badges/README.md) | 5/5 | Reference only |
| 56 | [Unlocked badges](../../../../docs/Stoic/flows/56-unlocked-badges/README.md) | 4/4 | Reference only |
| 57 | [All badges](../../../../docs/Stoic/flows/57-all-badges/README.md) | 2/2 | Reference only |
| 58 | [Stats](../../../../docs/Stoic/flows/58-stats/README.md) | 4/4 | Reference only |
| 59 | [Profile](../../../../docs/Stoic/flows/59-profile/README.md) | 5/5 | Selected; scoped destinations only |
| 60 | [Switching to dark mode](../../../../docs/Stoic/flows/60-switching-to-dark-mode/README.md) | 8/8 | Reference only |
| 61 | [Setting up stoic shield](../../../../docs/Stoic/flows/61-setting-up-stoic-shield/README.md) | 14/14 | Reference only |
| 62 | [Updating a blocking schedule](../../../../docs/Stoic/flows/62-updating-a-blocking-schedule/README.md) | 7/7 | Reference only |
| 63 | [Turning on notifications](../../../../docs/Stoic/flows/63-turning-on-notifications/README.md) | 4/4 | Selected visual reference; implement only the two PRD-scoped morning/evening reminder rows |
| 64 | [Privacy policy](../../../../docs/Stoic/flows/64-privacy-policy/README.md) | 2/2 | Selected; visible wording only |

**Inventory total: 64 flows, 369 images.** "Selected" can still have omitted screens, records, rows or controls as stated above. The brief is the authority for what survives.

## Rule → evidence → exception

These are reusable **families**, not universal layouts. The screen IDs in each row trace the rule to original captures; linked examples open exact screenshots. `Selected` examples govern the corresponding included screen. Reference-only examples help define a new component when no selected capture exists.

| System rule | Flow/screen evidence | Variant or exception to retain |
|---|---|---|
| **Surface roles:** light gray canvas, white or warm-white content, black primary text, restrained gray secondary text. Two exact flat-color families occur: `#F3F3F5`/`#FFFDFE` and `#F1F3F4`/`#FFFFFF`. | [04/01](../../../../docs/Stoic/flows/04-today/screenshots/screen-01.webp), [04/02](../../../../docs/Stoic/flows/04-today/screenshots/screen-02.webp), [42/03](../../../../docs/Stoic/flows/42-journey/screenshots/screen-03.webp), 43/05, 59/02 | Today itself switches families. Dark hero, black Insights and reference-only dark mode (60/03–08) are intentional variants. Never pick a flat color without identifying its host screen. |
| **Type hierarchy:** heavy rounded-looking sans for major heading, compact bold card heading, small gray support copy, tracked uppercase eyebrow for type/section. Some editorial route titles are lowercase with a period. | 01/01–12, [28/02](../../../../docs/Stoic/flows/28-collections/screenshots/screen-02.webp), 32/02, 36/02, [42/03](../../../../docs/Stoic/flows/42-journey/screenshots/screen-03.webp), 43/02, 52/02, 59/02 | Sentence-case questions and date headings do not follow the lowercase-period treatment. Typeface/metrics have not been identified from screenshots. |
| **Spacing/composition:** about 16 source-screen pixels of side inset in many 393-wide layouts, groups of tightly spaced cards, larger whitespace between conceptual sections, fixed controls above safe area. | 04/01–06, [27/04](../../../../docs/Stoic/flows/27-library/screenshots/screen-04.webp), 29/02, 42/02–06, 43/05–12, 59/02–05 | Full-width plots, media and carousel-peek cards break that inset. The approximate number is an observation, not a global token. |
| **Card grammar:** rounded content islands with little depth; anatomy changes by job: tall Today hero, small list row, two-column catalog, horizontal carousel, dense diary entry, chart module. | [04/01](../../../../docs/Stoic/flows/04-today/screenshots/screen-01.webp), 04/03, 27/02–05, 29/02–04, 31/03–05, [42/05](../../../../docs/Stoic/flows/42-journey/screenshots/screen-05.webp), 43/05–12 | Do not impose one radius/padding or white fill. Today has black and completed/outlined states; Library and exercise panels are reference only. |
| **Primary and secondary actions:** primary is black rounded capsule with white label; bordered/light capsule is secondary; disabled is pale/gray. Dark heroes invert the CTA to a white capsule. | 01/02–12, 05/02, 10/11, 22/04, [33/02](../../../../docs/Stoic/flows/33-completing-an-exercise-breathing/screenshots/screen-02.webp), 37/02, 40/04, 61/06–12 | Reflection steps 05/03–10 and 10/02–10 use a **circular black forward arrow**, a separate primitive. Source-only exercise CTAs do not add exercises to scope. |
| **Choice states share semantics, not shape:** tap changes visual fill/check/underline; single or multiple selection depends on the question. | [01/04](../../../../docs/Stoic/flows/01-onboarding/screenshots/screen-04.webp), 05/06–08, [10/04](../../../../docs/Stoic/flows/10-logging-a-daily-reflection-evening/screenshots/screen-04.webp), 16/02–04, 23/03–04, 25/03–04, 34/06–07, 41/02–07 | Variants are pill answers, circular focus icons, rectangular emotion tiles, segmented control, radio row, favorite star and underlined tab. Evening emotions are multi-select; age is single-select. |
| **Switches and selectors:** settings row puts label/value left and switch/chevron right; time input invokes native picker. Selected switch color is contextual. | 01/06–10, 12/02–03, 19/04, 34/04–09, [63/02](../../../../docs/Stoic/flows/63-turning-on-notifications/screenshots/screen-02.webp) | Onboarding notification switch appears blue; later profile/settings switch appears black. OS permission dialog is platform UI, and effective state must reflect actual permission. |
| **Date strip and Today state:** greeting/streak/profile above week strip; selected date is outlined vertical capsule. Morning/Evening cards change composition and wording after recorded completion. | [04/01](../../../../docs/Stoic/flows/04-today/screenshots/screen-01.webp)→[04/02](../../../../docs/Stoic/flows/04-today/screenshots/screen-02.webp)→04/03, 10/12, 17/01–02 | Tomorrow uses bird/countdown/read-only state. Source review and inspiration cards in Today are excluded. |
| **Reflection wizard:** Back + short segmented progress + Close at top; question and generous whitespace; keyboard-safe editor and right circular advance. | [05/03](../../../../docs/Stoic/flows/05-logging-a-daily-reflection-morning/screenshots/screen-03.webp)–10, [10/03](../../../../docs/Stoic/flows/10-logging-a-daily-reflection-evening/screenshots/screen-03.webp)–10, 25/02–11, 30/02–03 | 05/11–15 AI screens are excluded; retained progress must be renumbered. Emotion expansion 10/03–06 is a state within one step. Independent mood wizard 25 is reference only. |
| **Writing canvas:** borderless long-form field below prompt, visible placeholder before typing, bottom accessory/advance above native keyboard; long content scrolls. | 05/09–10, [10/07](../../../../docs/Stoic/flows/10-logging-a-daily-reflection-evening/screenshots/screen-07.webp)–10, 24/03, 25/05–06, 30/03, 40/05/10 | Source `+`, `Aa`, AI sparkle, voice, drawing, photos and standalone journal tools are not implied functions for the clone. Show media only if retained captured authoring produces it. |
| **Sheets have distinct variants:** dim original route, rounded upper corners and handle for some; root title can be large and collapse on scroll; nested pages use Back/parent label. | 11/02, 13/01–15, 22/02, 23/02–03, 33/02, 34/01–04, [59/02](../../../../docs/Stoic/flows/59-profile/screenshots/screen-02.webp)→59/03–05, [64/02](../../../../docs/Stoic/flows/64-privacy-policy/screenshots/screen-02.webp) | Curved creation drawer 23/02, prompt picker 24/02, exercise setup 33/02 and Profile/Privacy are different sheet anatomies. Do not flatten into one fixed title/height. |
| **Empty/loading/disabled states stay structured:** icon or chart placeholder, concise explanation, available action; loading/permission state remains visibly distinct. | [17/02](../../../../docs/Stoic/flows/17-tomorrow/screenshots/screen-02.webp), 41/06, [43/02](../../../../docs/Stoic/flows/43-trends-insights/screenshots/screen-02.webp)–03/05/07, 55/02–04, 61/06–12 | Journey 42/02 has an excluded first-journal CTA and Life Event, **not** captured `No entries yet` copy. New scoped Journey empty copy is a derived state, not a quoted screenshot. No sample chart values. |
| **Completion family:** sparse central monochrome motif, large `Good job!`, dynamic metric capsules and optional lower feedback/next step. | [05/16](../../../../docs/Stoic/flows/05-logging-a-daily-reflection-morning/screenshots/screen-16.webp)–18, 10/11, 24/04, 25/12, 30/04–05, 33/06–07, 37/06, 40/11 | Stats vary by activity; feedback is not universal. Only selected reflection completion screens and their retained controls are implemented. |
| **Illustration/icon language:** bespoke black/white silhouettes and thin decorative linework; small section icons are simple filled glyphs. | 01/01/11–12, 05/02–05/16–18, 17/02, 27/02–05, 32/02–03, 36/02–03, [42/02](../../../../docs/Stoic/flows/42-journey/screenshots/screen-02.webp) | User photos in 42/04/06 are content, not system assets. Reproduce surviving illustrations as SVG; reference-only motifs may guide genuinely new art. |
| **Navigation:** source bottom bar uses icon+label with black active item, gray inactive items and raised central `+`, above home indicator. | 04/01–06, 22/01, 27/01–05, [42/03](../../../../docs/Stoic/flows/42-journey/screenshots/screen-03.webp) | Scoped clone has Today/Journey only; five-slot arrangement and creation `+` are excluded. The two-target arrangement is an explicit adaptation, while weight/placement come from source. |
| **Journey record stream:** top Filter/Days pills, black Insights banner, relative-day/date heading with chevron, white entry cards with glyph, tracked type, bold title, time, prompt and answer; optional outlined tags. | [42/02](../../../../docs/Stoic/flows/42-journey/screenshots/screen-02.webp)–[42/06](../../../../docs/Stoic/flows/42-journey/screenshots/screen-06.webp), 50/01–03, [52/02](../../../../docs/Stoic/flows/52-daily-entries/screenshots/screen-02.webp) | Source cards also contain independent Journal, Life Event, Mood Check-In, exercises, voice and photos. Only actual in-scope morning/evening records render; filter/period affordances survive only where destination is included. |
| **Entry detail:** pale reading page; Back/More chrome, timestamp/category, large title, vertically separated prompt/answer blocks; long content scrolls. | [50/02](../../../../docs/Stoic/flows/50-entry-detail/screenshots/screen-02.webp)–03, 52/02 | 50/04 Quote Journal excluded. `More` menu/edit mode is not pictured; editing is brief-required, so its exact control UI is a documented inference, not a copied screenshot. |
| **Insight/chart modules:** rounded white chart card, bold title, gray descriptor, subtle axes and status, optional `View All Days`; blue current series, gray comparator, rose mood marks. | [43/05](../../../../docs/Stoic/flows/43-trends-insights/screenshots/screen-05.webp)–12, [44/02](../../../../docs/Stoic/flows/44-mood-calendar/screenshots/screen-02.webp), 49/03–06 | No-data and insufficient-data cards replace invented curves. Source mood derives from app openings/check-ins; clone maps in-scope evening feeling values only. HealthKit and unrelated meditation metrics excluded. |
| **Period control is coupled to data:** top Weeks/Months/Years popover, fixed lower period pager, chart axis/labels/calendar/date range update together. | [49/01](../../../../docs/Stoic/flows/49-sorting-by-months/screenshots/screen-01.webp)→[49/02](../../../../docs/Stoic/flows/49-sorting-by-months/screenshots/screen-02.webp)→49/03–06, 43/02–12 | Chart-view switching, hiding and word exclusion (45–48) are reference only; no extra control may remain active from them. |
| **Profile/settings and privacy:** section eyebrow, grouped rows with separator/right value or switch; root sheet large title collapses on scroll; nested Privacy page has parent Back, title, lead and prose. | [59/02](../../../../docs/Stoic/flows/59-profile/screenshots/screen-02.webp)–05, [63/02](../../../../docs/Stoic/flows/63-turning-on-notifications/screenshots/screen-02.webp)–04, [64/02](../../../../docs/Stoic/flows/64-privacy-policy/screenshots/screen-02.webp) | Profile retains only Notifications/Privacy; the source shows more reminder rows, while the approved clone retains only Morning Preparation and Evening Reflection. Privacy visible copy ends at `Error logs`. Its source claims about iCloud/AI/analytics are reproduced only for internal screen comparison and are not facts about the clone. |
| **Search/favorites/exercise controls:** category-underlined search and empty result; hollow-to-filled favorite; duration/chime/player/pause states show reusable control semantics. | [41/02](../../../../docs/Stoic/flows/41-searching-stoic/screenshots/screen-02.webp)–07, 23/03–05, 33/02–07, 34/01–09, 37/02–06, 38/04–07, [39/02](../../../../docs/Stoic/flows/39-pausing-an-exercise/screenshots/screen-02.webp)–03, 40/06–11 | All are **reference-only** in this phase. They give later designers a ready evidence trail if a future feature requires them; they do not authorize routes or controls now. |

## Reuse protocol for a later screen

1. Read the current [brief](../../briefs/brief-diary-clone-2026-10-22/brief.md), [DESIGN.md](DESIGN.md), and [EXPERIENCE.md](EXPERIENCE.md). The brief determines scope; the two spines specify the reusable visual and behavior system.
2. If the requested screen is one of the selected captures, reproduce **that screen's own images** first, including its state variants. Use shared tokens only where the screenshot leaves a gap. A source control leading outside the brief is removed, even if visible in the capture.
3. For a genuinely new screen or component, choose the closest anatomy and state family in the table above. Apply the spines; use this index to open **only the cited screenshots needed for an uncertain detail**. There is no routine need to re-audit all 369 images.
4. Record a new rule or exception with an exact `flow/screen` link and mark uncaptured behavior as a design decision. Keep source-only features out of implementation unless the future brief explicitly adds them. Use real persisted records for data states, not source sample content.

This appendix is an evidence locator. Its rules and image links support the two spines; the selected capture remains the final visual authority for its own screen.
