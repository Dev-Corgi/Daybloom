---
name: DiaryClone
description: Behavior, navigation, states, and journeys for selected Stoic diary flows; full-corpus pattern reference for later screens.
status: final
created: 2026-10-22
updated: 2026-10-23
sources:
  - ../../initiative-diary-clone.md
  - ../../briefs/brief-diary-clone-2026-10-22/brief.md
  - ../../../../docs/Stoic/flows/MANIFEST.md
---

# DiaryClone — Experience Spine

## Foundation

DiaryClone is one portrait mobile app on iOS and Android. The [product brief](../../briefs/brief-diary-clone-2026-10-22/brief.md) fixes this phase's scope. The iOS 393 × 852 [Stoic corpus](../../../../docs/Stoic/flows/MANIFEST.md) is the comparison source. `DESIGN.md` governs visual tokens and anatomy; this document governs navigation, behavior, data, states, and accessibility. English is the screen language. Native status bars, keyboards, time pickers, permission alerts, and gesture regions follow each OS.

**Source hierarchy for future work:** (1) For a selected screen, reproduce its own captured layout and interaction, minus explicit scope exclusions. (2) For a genuinely new or uncaptured component, apply the evidence-backed rules below and the paired `DESIGN.md` system. (3) Open an individual capture only to resolve an ambiguity, variant, or pixel detail; the full corpus need not be re-audited. Citations such as `05/06` mean `docs/Stoic/flows/05-…/screenshots/screen-06.webp`. The [capture evidence index](CAPTURE-AUDIT.md) maps rules and exceptions to the source screens after visual inspection of **all 369 screenshots**; its linked working reports contain fuller observations. Flow numbers 01–64 are an evidence index, not a feature backlog. The black Mobbin footer in each capture is not app UI.

This internal clone authors only morning and evening reflections and stores them locally. It does not create an independent journal entry, mood check-in, account, cloud sync, translation, or AI function. The sole preserved source-only display exception is the onboarding `AI Mentors` card (01/11–12), without an AI destination. A source control leading only outside the brief disappears; it must not be a dead button.

## Information Architecture

| Surface | Entry → exit | Scoped job and source |
|---|---|---|
| Onboarding | First launch → Today | Captured 01/01–12; exclude source 01/13 and keep `AI Mentors` display only. |
| Today | App open / bottom navigation | Date strip, morning/evening state cards, Quote display, route to Tomorrow; 04/01–06 and 10/12. Omit `on glowing reviews` and `Get Inspired`. |
| Morning reflection | Today card → Today/Journey | Sleep, focus, plan, completion/streak; 05/01–10 then 05/16–18. Exclude AI 05/11–15. |
| Evening reflection | Today card → Today/Journey | Rest, feelings, summary and completion; 10/01–12. |
| Tomorrow | Today date strip → Today | Read-only countdown, 17/01–02. |
| Quote display | Today content | Text and attribution only; no Quote Journal/Favorite/Share, 04/04–06. |
| Journey | Bottom navigation | Actual dated reflection cards, insight banner, links to Entry detail, Daily entries, Trends; 42/02–06. |
| Entry detail | Journey card / Daily entries → originating list | Read and edit saved morning/evening answers; captured read layout 50/02–03. Edit UI itself is uncaptured. |
| Daily entries | Journey day heading → Journey | Entries for one local calendar day; 52/02. |
| Trends & insights | Journey banner → Journey | Period-dependent charts and summaries from eligible saved records; 43/02–12. |
| Mood calendar | Trends `View All Days` → Trends | Dated marks from saved Evening reflection feelings; captured calendar 44/02. |
| Sorting by months | Trends period selector → Trends | Week/Month menu, coordinated month view and pager; 49/01–06. |
| Profile | Today profile icon → Today | Sheet with only scoped Notifications and Privacy paths; 59/02–05. |
| Notifications | Profile row → Profile | Morning Preparation and Evening Reflection only; each has an editable local time and permission-backed switch. Adapt 63/02–04 to two rows. |
| Privacy policy | Profile row → Profile | Captured text and reading layout through `Error logs`; 64/02. |

The **two-destination bottom navigation (Today, Journey)** is a scope adaptation. Source captures show five tabs and central independent-entry `+` (04/01, 42/02–06). Preserve safe-area placement, icon/label hierarchy, and active dark versus inactive muted states, but create a balanced two-item arrangement. Profile remains a Today-header entry, and Tomorrow remains a date-strip destination. No source-only tab, central creation affordance, or unused Journey `Filter`/`Days` control should remain active. The source `Days` entry-list grouping is not the selected Trends period control; do not conflate them.

**Record and date model:** one saved morning or evening reflection belongs to its recorded local calendar date. Today, Journey, Daily entries, Entry detail, Trends and Mood calendar read the same stored records and update after edits. A date heading drills into precisely that date (42/03, 52/02). [ASSUMPTION] Save a stable local-date key at creation and preserve it after a time-zone change; exact time-zone semantics are uncaptured. [ASSUMPTION] First onboarding completion (01/12) lands on Today, bypassing excluded 01/13; later launches restore Today. Data examples in the captures, including 42/03 and 43/04, are samples, never seed data.

## Voice and Tone

Use the selected captures' English labels and restrained prompt wording where visible: `Begin`, `Continue`, `Reflect`, `View All Days`, question wording, date labels and short completion copy. Preserve capitalization and punctuation per the specific selected screen: `morning.` (50/02) and `19 JULY` / `Saturday` (52/02) serve different roles. Do not force every sentence into the lowercase headline idiom. Brand/visual voice belongs in `DESIGN.md`.

| Context | Treatment |
|---|---|
| Captured content | Transcribe selected visible copy, after removing excluded feature copy. Do not rewrite captions into new motivational messages. |
| Uncaptured empty/error | Use plain, data-honest copy and a working in-scope next step. `No entries yet.` and a Today route are **[ASSUMPTION]**, not source wording. |
| Permissions | State actual OS status and offer Settings when denial/restriction prevents activation **[ASSUMPTION]**. Never say a reminder is active when it is not. |
| Privacy | Owner reaffirmed the visible Stoic wording verbatim for this internal-only clone, 64/02, ending at the visible `Error logs` heading. The source text mentions iCloud, AI, analytics, and error logs that this clone does not implement; this is a screen-reproduction decision, not a verified statement of the clone's data practices. Do not use it as an external-release policy without a separate factual review. Never invent text below that heading. |

## Component Patterns

Visual variants and tokens live in `DESIGN.md.Components`. The behavior below names the source and the scoped adaptation. New components should first choose the matching anatomy and state, then use that screen's visual variant; a shared primitive does not mean identical geometry.

| Component / primitive | Behavior and states | Evidence / limit |
|---|---|---|
| Pill action and circular forward | A pill begins, continues, saves or opens a destination; the right-bottom **circular** arrow advances one reflection step. Black enabled, gray disabled when a required choice is missing. A tap commits once. White pill reverses on a dark Today card. | 01/02–12, 04/01, 05/02–10, 10/02–10. Do not model the round reflection arrow as a pill. |
| Selection family | Selection is shared state, not shared shape: onboarding answer pills (single age, 01/04–05), round icon Focus options (up to three, 05/06–08), two-column feeling tiles with `Show more/less` within one step (multi-select, 10/03–06), and native/radio settings lists where captured. Announce selection and count/limit. | 16/02–04 metric segmented choice, 25/03–06 standalone mood tiles, 34/06–07 radio list are reference-only variants for future components. |
| Slider / scale | Drag or tap changes the displayed qualitative value and filled track; retain its value when stepping back. | Morning sleep 05/03–04, Evening rest 10/02. Custom metric creation 16/02–04 remains reference-only. |
| Reflection step and editor | Header Back, short segmented progress, Close; body question and input; bottom forward remains reachable above native keyboard. Long text scrolls. Focus and feelings expansion do not create phantom steps. Morning 05/10 advances straight to 05/16. | 05/02–18, 10/02–11; reference editors 24/03 and 40/10 confirm unclipped text. Voice/sketch/AI/rich-format tools from 06–09 are outside scope. |
| Today reflection card | Before/after state changes structure, not just label: dark single Morning hero, paired light Morning/Evening cards, outlined/subdued completed card with answer pills. Date strip marks selected date and completed days. Tap only the captured actionable card or contained CTA. | 04/01–03, 10/12, 17/01–02. Completed state reads stored data, not hardcoded source sample. |
| Quote block | Read quote and attribution on Today. No independent Quote journal, Favorite or Share entry point. | 04/04–06 selected display; 11/01–02 and 19–20 are reference-only interactions. [ASSUMPTION] Packaged deterministic local quote set because source/rotation is uncaptured. |
| Journey banner and day group | Dark banner leads to Trends; relative day/date heading with chevron leads to that day's Daily entries. Banner numbers use eligible data. Preserve the first-day visual scaffold without its excluded `Your first journal`/Life Event actions. | 42/02–06, 43/01, 52/01. Source `14`, `Okay`, `Some` are sample values. |
| Entry card and detail | Card: type icon/eyebrow, title, right time, gray prompt, black answer; tap opens the same saved record. Detail: Back, uppercase timestamp, large type title, spaced question/answer blocks. Show chips/media only for fields actually authored in an included reflection; never manufacture a photo/audio from reference data. Owner-approved edit path: top-right `More` opens a menu containing `Edit`; the editor offers `Save` and `Cancel`. `Cancel` leaves the committed row unchanged. `Save` commits in-scope answer changes once; failure keeps the editor values and prior committed row. | 42/03–06, 50/01–03, 52/02. Only `More` itself is captured at 50/02–03; its menu/editor are owner-approved adaptations, not source-verified screens. No Delete, Share, or unrelated menu actions. |
| Insight card and empty chart | Header title/description, chart/stat body, optional captured drill-down. No data uses explicit source-style `No data yet`, pale ring/empty dots/explanation; insufficient data says more days are needed. No fake percentages or lines. Omit ellipsis if its source menu is excluded. | 43/02–03,05–12, 44/01, 49/04–06. HealthKit 43/09, chart hiding 46 and personalization 47 are reference-only. |
| Period selector, plot and pager | Header `Weeks` pill opens a checked options popover (49/02); `Months` changes title, axis ticks, legend, card labels, calendar density, and fixed bottom pager together (49/01→03–06). Pager moves one period and keeps section context. | 43/04–12, 49/01–06. Source offers `Years` but selected implementation is weeks/months; no invented year aggregates. `Days/Words/Cloud` chart-view toggles at 45/01–03 are reference-only. |
| Approved Trends summaries | For the selected week or calendar month, show (1) distinct local days with at least one completed reflection, (2) separate completed morning and evening record counts, and (3) each evening feeling's number of saved selections. One day with both kinds counts once in (1) and once in each applicable count in (2). Count a feeling at most once per evening record. Use committed records only and recompute after edits. Zero data yields a no-data state, never a copied sample curve or an inferred score/percentage. | Owner-approved metrics using only the app's stored reflections; captured 43/02–12 and 49/03–06 establish visual states and period behavior, not unsupported source health/analytics values. |
| Mood calendar | `View All Days` opens a long month-grouped dot grid. Outlined empty circle differs from filled blue/rose data dot; every mark has date/value semantics. | 44/01–02. Source describes app openings and standalone mood check-ins. This clone **deliberately maps** marks to in-scope Evening reflection feeling answers. Do not import standalone mood entry points. |
| Profile root and nested sheet | Profile is a near-full-height sheet over Today, with large left title and top-right Close; on scroll the title compacts to a small centered nav title. Nested Notifications/Privacy have Back + parent label and their own large title, preserving the underlying sheet/scroll. Close dismisses the root; Back pops one sheet. | 59/02→03→05, 63/02–04, 64/02. Reference sheets vary in size/handle (22/02, 33/02); do not force all overlays into this selected Profile anatomy. |
| Settings / notification row | Section eyebrow outside white grouped rows; left label/description, right chevron or time/switch; thin divider. Switch shows effective on/off, including disabled/muted when unavailable. Morning and evening reminder times are individually editable in onboarding and Profile; tapping a time opens the native picker, and a confirmed change persists and updates its active schedule. Toggling requests OS permission when needed, then re-reads status. Owner-approved visible copy is the captured `Morning Preparation` / `Reminder to prepare for your day in the morning` and `Evening Reflection` / `Reminder to wind down and reflect about your day`. Displayed times and switch states remain real, not copied sample values. | 01/07–09 shows a changed morning time in the picker; 59/02–05 and 63/02–04 govern Profile anatomy. Source During the Day, Your Daily Focus, AI Reminders and Daily Journaling Prompt are **reference-only**. |
| Illustration | Decorative bird/line drawing does not take focus or announce; an illustration inside a named action is part of that action's accessible name only if needed. | 01/01, 05/16–18, 17/02, 42/02; reference motifs 27/02–05 and 40/02. |

**Future component grammar from reference-only flows:** grouped single/multi-select rows show an empty ring versus filled check (34/06–07, 47/02–03, 53/02–03); sheet-stacked editing has Close/Back/Save hierarchy (13/09–15, 62/02–04); fullscreen task steps use segmented progress (25/02–11, 30/02–03); a feedback response uses separate hollow/half/full circles (26/01); timers use setup content plus pinned bottom action (33/02, 37/02–03). These establish interaction families if a **later approved screen** needs them; no associated feature is in this phase.

## State Patterns

| Surface | Cold/empty | Selection, saved, loading | Failure and boundaries |
|---|---|---|---|
| Onboarding | First screen 01/01; no previous preference presumed. | Choices retain state on Back [ASSUMPTION]; 01/11 gray Continue becomes enabled after visible checklist completes at 01/12; native time/permission UI 01/06–10. | OS denial does not trap onboarding or show active reminder. Excluded subscription 01/13 does not appear. |
| Today / Tomorrow / Quote | Today reflects current local date and whether each reflection exists; Tomorrow is a read-only countdown with bird (17/02). | Morning dark/paired/completed card variants 04/01–03, 10/12; date rollover refreshes labels [ASSUMPTION]. | Local read failure shows an explicit retry state [ASSUMPTION]. Missing packaged quote omits its card rather than a dead action [ASSUMPTION]. |
| Reflections | Untouched answers blank/unselected; required selection gates Next. | Step progress counts **retained** steps only; keyboard leaves writing and forward reachable; save updates all reading surfaces. Draft on Close/interruption [ASSUMPTION]. | Save failure keeps visible answers and offers retry [ASSUMPTION]. No AI step or phantom segment. |
| Journey / Daily entries / Entry detail | Source 42/02 first-day Journey has an independent-journal CTA, **not** `No entries yet.` Clone needs a new scoped no-record treatment [ASSUMPTION], preserving banner/day scaffold where meaningful and routing to Today. Empty selected day is honest [ASSUMPTION]. | Data load shows only real morning/evening records; entry edit updates detail, list preview and day/insight rollups. | Unreadable/missing record yields bounded error and Back [ASSUMPTION]; no source photos/audio/sample journal records. |
| Trends / Mood calendar / Months | 43/02–03,05,07 show no-data or insufficient-days treatments. Unrecorded calendar circles remain outlined. | Period/selected month stays in sync across header, plots, cards, dots, bottom pager; changed reflection data recomputes visible summaries. | Do not infer a mood score from an absent feeling or display the source sample blue curve. Not all chart types in 43/09–12 are eligible with this data model. |
| Profile / Notifications | Root opens above Today, nested pages preserve stack and previous scroll [ASSUMPTION]. Two scoped reminder rows show each saved, editable time and OS-effective state. | Enable only after persistence/permission succeeds; re-query OS status on return from permission prompt or Settings. | Denied/restricted OS permission shows actionable Settings route [ASSUMPTION] and an off effective switch. No AI or journaling reminder. |
| Privacy | Captured text through `Error logs` heading only. | Scroll inside nested sheet; Back restores Profile [ASSUMPTION]. | Missing bundled text shows explicit unavailable state and Back [ASSUMPTION]; no invented continuation. |

## Interaction Primitives

- **Tap, Back, Close, Save:** Tap selects or opens one route. Back reverses one retained step or one route; Close exits the current flow/sheet. Save commits a real record once and propagates changed data to every view. A nested sheet pops to its parent, not directly to Today (59/02–05, 64/02). A long press is not required by any selected flow.
- **Selected versus completed:** Visual fill/check and semantic state both change. Onboarding answer selection, Focus, emotion tiles, settings switches, and finished reflection cards have distinct shapes and should not share one indiscriminate black chip (01/04–05, 05/06–08, 10/03–06, 04/02).
- **Scrolling and keyboard:** Dense history, policy text, and chart sections scroll; pinned action/nav sits above safe areas. Reflection keyboard raises the writing accessory/forward action (05/09–10, 10/07–10). Emotion `Show more/less` expands within the same step (10/03–06). No content is clipped just to match a screenshot viewport.
- **Period/date/data coupling:** Week-to-month switch, pager, titles, plot axes/legends, mark density and card values change as one state (49/01–06). Journey day labels, Daily entries, Entry detail and trend aggregations share the local record date. [ASSUMPTION] Keep the selected period on a drill-down/back cycle.
- **OS boundary:** Native notification permission and time picker are system UI (01/08–10). Screen Time picker/permission in 61/04,07–08 are evidence of this boundary only, not scoped features. Never imitate an iOS permission dialog on Android.
- **No dead affordance:** Source-only overflow menus, filter chips, AI tools, independent creation, chart customization, and profile routes disappear when their destination is absent. The captured `More` on Entry detail is a special uncertainty: retain only if it houses the brief-required real edit action; its menu contents are not source-verified.

## Accessibility Floor

- Buttons, text fields, sliders, switches, radios/tiles, dates, chart controls and sheet navigation expose native roles, labels and selected/disabled state on VoiceOver and TalkBack. Multi-select Focus announces its maximum of three; feeling choices announce selected state. Progress announces `Step N of M` for **retained** steps [ASSUMPTION].
- Minimum hit targets: 44 pt iOS / 48 dp Android [ASSUMPTION], enlarging invisible hit area when source glyphs are smaller without changing their silhouette. Dynamic text size must keep cards, policy paragraphs and bottom actions reachable through scrolling or reflow.
- Chart summaries have text alternatives; each calendar dot conveys its date and recorded value or `No data`, so blue/rose/outline are never the only signal. Disable unavailable controls semantically, not through gray alone.
- Focus enters a newly opened sheet/route at its heading and returns to the invoking control on Back/Close; an OS permission return re-evaluates the actual switch state. Decorative birds/line drawings are hidden from screen readers.
- Honor reduced motion; no required state depends on animation. If the source displays a completion transition, the text/result must also be available without it.

## Responsive & Platform

Use the same app content hierarchy on Android and iOS, comparing selected screens first at 393 × 852. The iOS captures are a **baseline**, not a fixed clipping box. Smaller heights scroll the question/list or lift bottom action above keyboard and system bars; longer policy or entry text expands. Larger widths keep a readable centered column [ASSUMPTION]. System status, home/gesture area, keyboard, time picker and permission alert use each platform's native rendering. The Mobbin attribution strip is never implemented. A future dark mode can draw on the Black-mode role inversion at 60/03–08, but Appearance/dark-mode switching is outside this scope; Black/Graphite/Blue are not current settings.

## Inspiration & Anti-patterns

The direct model is the [full Stoic flow corpus](../../../../docs/Stoic/flows/MANIFEST.md), distilled into the [evidence index](CAPTURE-AUDIT.md) and these two spines. Later bmad-ux work should use these rules and citations to choose a component family, then inspect only the relevant source capture for unresolved detail. The selected capture always wins for a selected screen. Reference examples include alternate sheet heights (22/02, 33/02), editor tools (24/03), selection shapes (25/03–06), empty search (41/07), and dark palette (60/03–08); they are evidence for future *new* components only.

Do not import premium, AI mentors/insight actions, independent journaling or mood check-in, voice/sketch/rich text, quote journaling/sharing/favoriting, prompt/Focus/metric personalization, Inspirations/Library/Search, breath/meditation/exercises, badge/stats, chart hide/filter/word exclusion, HealthKit, dark-mode settings, Shield, or source-only Profile/social/account routes. The onboarding `AI Mentors` card is the explicit visual exception. Notifications excludes source During the Day, Your Daily Focus, AI Reminders and Daily Journaling Prompt. Privacy's captured iCloud/OpenAI wording is an internal-clone copy exception, not a functional requirement.

## Key Flows

The named journeys mirror the brief. Mina is an internal tester on a phone; each climax is an observable implementation result.

### Onboarding — Mina starts

1. Mina advances through 01/01–12, making visible choices and setting reminder times.
2. The OS asks for notification permission at the captured point (01/10). The plan-ready `AI Mentors` card stays display-only.
3. **Climax:** Continue goes to Today with retained preferences [ASSUMPTION], bypassing excluded 01/13. Permission denial does not trap her.

### Today — Mina begins or returns

1. Mina sees the current date strip, relevant reflection card state, and the Quote display (04/01–06).
2. She selects a morning or evening Begin; completion later changes that card using saved values (04/02, 10/12).
3. **Climax:** the chosen captured reflection opens, and returning Today reflects its real saved completion. Local read failure shows retry [ASSUMPTION].

### Morning reflection — Mina plans her day

1. From Today, she adjusts sleep and selects up to three focuses (05/03–08), then writes the plan (05/09–10).
2. Next jumps from 05/10 to 05/16–18; AI screens 05/11–15 do not appear or count in progress.
3. **Climax:** her actual morning record persists and is visible on Today and Journey after restart. Failed save keeps the text and retry path [ASSUMPTION].

### Evening reflection — Mina closes the day

1. She adjusts rest, chooses one or more feelings including expanded choices, and writes her summary (10/02–10).
2. She finishes the captured completion state (10/11–12).
3. **Climax:** her evening record and selected feelings appear consistently in Journey and Mood calendar. Interruption keeps the draft [ASSUMPTION].

### Tomorrow — Mina checks the next day

1. She uses Today's date strip to select tomorrow (17/01).
2. **Climax:** the bird/countdown read-only view appears (17/02), and she can return to Today. [ASSUMPTION] Recompute countdown after clock changes.

### Quote display — Mina reads

1. She scrolls to the Today quote and attribution (04/04–06).
2. **Climax:** she can read it without a dead Favorite, Share or Quote-journal action. Missing quote source omits the block [ASSUMPTION].

### Journey — Mina reviews history

1. She opens Journey and sees the insight banner plus dated morning/evening records (42/02–06 adapted to scope).
2. She chooses a card or day heading.
3. **Climax:** the matching saved Entry detail or Daily entries opens. An empty account uses a newly designed no-record treatment [ASSUMPTION], not source 42/02's excluded journal CTA.

### Entry detail — Mina edits a reflection

1. From Journey or Daily entries, she reads the question/answer page (50/02–03).
2. She taps the captured `More` control, selects the owner-approved `Edit` item, and changes an in-scope answer. The menu/editor are uncaptured adaptations.
3. **Climax:** `Save` updates the list preview, detail and derived insights after restart. `Cancel` discards unsaved changes; a failed save retains edited text and the prior committed row.

### Daily entries — Mina opens a day

1. She selects the Journey day heading (42/03, 52/01).
2. **Climax:** 52/02 lists only that date's stored reflections; selecting one opens its detail and Back returns to the same day. Empty dates show an honest state [ASSUMPTION].

### Trends & insights — Mina sees her patterns

1. She opens the Journey insights banner and scrolls through eligible chart categories (43/02–12).
2. **Climax:** the three approved count summaries match saved reflection values and route to selected Mood calendar/period views. Zero data uses the source's explicit no-data treatment (43/02–03,05,07); unsupported source metrics and sample curves are absent.

### Mood calendar — Mina scans days

1. She taps `View All Days` on the eligible Mood Calendar card (44/01).
2. **Climax:** 44/02's month grid shows marks for saved Evening feelings and empty outlines otherwise. This is an intentional clone mapping from the source's app-opening/check-in model.

### Sorting by months — Mina changes the period

1. She opens the Weeks menu (49/02) and selects Months.
2. **Climax:** headings, curve/bar axes, calendar density, values and bottom period pager all switch to the selected month (49/03–06); an empty month never reuses source sample data.

### Profile — Mina opens settings

1. She taps Today's profile icon; the root sheet opens with its large title (59/02).
2. She scrolls and sees the compact title (59/03–05), then selects Notifications or Privacy.
3. **Climax:** each nested destination opens and Back returns to Profile at its prior place [ASSUMPTION]; root Close returns to Today.

### Notifications — Mina enables a reminder

1. She opens the scoped two-row notifications sheet (63/02 adapted to scope) and changes a morning or evening time with the native picker, or chooses a reminder switch.
2. If required, the OS asks permission; return to the app triggers a status re-read (01/10 is the captured permission idiom).
3. **Climax:** the time persists and switch shows effective permission-backed state. Denial leaves it off and offers Settings [ASSUMPTION].

### Privacy policy — Mina reads the captured text

1. She selects Profile's Privacy row (64/01) and reads the nested page (64/02).
2. **Climax:** captured wording through `Error logs` is visible and Back returns to Profile; no uncaptured continuation is fabricated. Missing bundled content shows an unavailable state [ASSUMPTION].

## Open Decisions

The screenshots do not establish quote source/rotation, draft-save trigger, time-zone reassignment policy, exact notification-denial copy, or treatment below the Privacy `Error logs` heading. Each related rule is marked [ASSUMPTION] above. The owner resolved the Entry detail edit path, eligible Trends count formulas, and internal-only visible Privacy/reminder copy. The captured Privacy prose is reproduced for screen comparison, including statements about unavailable source features; it must not be treated as a factual policy for an external release.
