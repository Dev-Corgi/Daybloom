---
status: final
stepsCompleted:
  - step-01-validate-prerequisites
  - step-02-design-epics
  - step-03-create-stories
  - step-04-final-validation
inputDocuments:
  - _bmad-output/planning-artifacts/briefs/brief-diary-clone-2026-10-22/brief.md
  - _bmad-output/planning-artifacts/prds/prd-diary-clone-2026-10-22/prd.md
  - _bmad-output/planning-artifacts/ux-designs/ux-diary-clone-2026-10-22/DESIGN.md
  - _bmad-output/planning-artifacts/ux-designs/ux-diary-clone-2026-10-22/EXPERIENCE.md
  - _bmad-output/planning-artifacts/ux-designs/ux-diary-clone-2026-10-22/CAPTURE-AUDIT.md
  - _bmad-output/planning-artifacts/architecture/architecture-diary-clone-2026-10-22/architecture.md
  - _bmad-output/planning-artifacts/initiative-diary-clone.md
---

# DiaryClone - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for DiaryClone, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

The approved brief and PRD define scope; DESIGN and EXPERIENCE define reusable appearance and behavior; the selected capture governs each retained screen. All stories begin in backlog, with no previous implementation progress carried forward.

## Requirements Inventory

### Functional Requirements

FR-1: A tester completes retained onboarding screens 01/01–12, skips the final paywall, sees the display-only AI Mentors card, and reaches Today without an AI route.
FR-2: A tester navigates among retained Today, Tomorrow, Journey, Daily entries, Entry detail, Trends, Mood calendar, Trends month view, Profile, Notifications, and Privacy destinations without dead or excluded controls.
FR-3: Today displays the current device-local date and actual morning/evening completion state.
FR-4: A tester completes at most one morning reflection per local day with sleep, up to three focus choices, and written plans; AI follow-up steps are excluded.
FR-5: A tester completes at most one evening reflection per local day with rest, one or more feelings, summary, optional photo, and Yes/No/Skip bedtime response; AI writing is excluded.
FR-6: A tester opens the read-only Tomorrow countdown from Today and returns, with date-correct remaining time.
FR-7: Today displays local Quote text and attribution without Quote Journal, Favorite, or Share actions.
FR-8: Journey shows only committed morning/evening reflections with truthful empty and populated states.
FR-9: Daily entries lists only reflections belonging to its selected stored local day.
FR-10: Entry detail reads and edits a saved reflection via More → Edit with Save/Cancel; successful edits refresh readers and failed saves preserve the prior committed row.
FR-11: In Trends, a tester switches Weeks/Months and pages periods; heading, date range, axes, values, cards, calendar density, and pager describe the same selected period. Journey month browsing is excluded.
FR-12: Trends derives only approved completed-day, separate morning/evening completion, and evening feeling selection counts from committed records for the selected week or month, with honest no-data states.
FR-13: Mood calendar displays date marks derived from saved evening feeling sets and updates them after edits without inventing a scalar mood score.
FR-14: Profile opens and returns from scoped Notifications and Privacy screens; the internal-only Privacy screen reproduces visible source text through the Error logs heading.
FR-15: Morning and evening local reminders have separate editable times, persist across relaunch, reflect actual OS permission and effective schedule state, deliver at selected times when enabled, and stop when disabled.
FR-16: Completed reflections, edits, feelings, photos, and relevant settings persist on device across relaunch and feed one consistent source for every reading surface.
FR-17: First reflection completion offers one-time streak visibility and goal choice; Today and completion views derive streak days from actual completed dates.

### NonFunctional Requirements

NFR-1: Compare every retained screen with its own selected Stoic capture at the 393 × 852 iOS baseline; recreate surviving illustration and icon assets as SVG.
NFR-2: Keep the same app-screen design on Android and iOS while using native system status bars, keyboard, time picker, and permission dialogs; small screens, safe areas, and dynamic text must remain usable.
NFR-3: Expose accessible roles, labels, selection/disabled states, chart summaries, and dated mood values to VoiceOver and TalkBack; honor reduced motion and keep controls reachable.
NFR-4: Persist local records and settings across process restart, enforce one completed record per day and kind, preserve previous committed data on write or migration failure, and never substitute seeded records or statistics.
NFR-5: Store journal content and photos locally without an app-managed account, backend, cloud sync, remote journal upload, telemetry carrying diary content, or AI capability.
NFR-6: Treat OS permission and scheduler results as the source of reminder effective state; enabled reminders must use the saved local time and avoid duplicate schedules.
NFR-7: Use English app copy. Reproduce the approved source Privacy text only in the internal screen-comparison build; it is not an external-release privacy policy.

### Additional Requirements

- Start with the Expo SDK 58 default starter, Expo Router, feature presentation/application/data layers, and a single internal Android/iOS app deployment.
- Use expo-sqlite with ordered schema migrations; a migration failure blocks writes without replacing the existing database.
- Assign a stable device-local YYYY-MM-DD dayKey when a reflection session begins; preserve it across midnight, time-zone changes, drafts, completion, and edits.
- Store drafts separately from completed rows, flush changes before step exit/Close/background, and commit completion/edit operations transactionally.
- Copy optional evening photos to app-owned persistent files before storing relative references; stage replacements, preserve the old file on failure, and show a bounded missing-media state after restore.
- Derive Journey, Daily entries, Trends, Mood calendar, Today, and streaks from committed records through shared projections; invalidate readers only after a successful commit.
- Keep reminder intent/settings separate from OS-effective state. Use a single schedule per reminder, reconcile permission/schedules on foreground and launch, and gate Android exact alarms as specified in AD-6.
- Package quotes and internal Privacy copy locally; create no runtime service. Internal physical-device builds are needed to verify notification delivery.
- Preserve the source hierarchy: current brief/PRD set scope, UX spines set behavior and reusable design rules, and a selected capture governs its own retained screen.

### UX Design Requirements

UX-DR1: Render retained onboarding 01/01–12 with captured answer pills, native reminder-time/permission boundaries, Back-retained choices, and a display-only AI Mentors card; never route to 01/13.
UX-DR2: Implement distinct Today dark hero, paired light, and completed card states from committed data, plus the captured date strip and a two-destination Today/Journey bottom bar.
UX-DR3: Preserve morning reflection sleep slider, up-to-three circular Focus choices, keyboard-safe plan editor, circular advance control, retained progress count, and completion/streak screens; omit AI screens 05/11–15.
UX-DR4: Preserve evening rest slider, multi-select feeling tiles and expansion within one step, summary editor, optional photo flow, bedtime response, and completion states.
UX-DR5: Keep Tomorrow as a read-only bird/countdown screen and Quote as Today text/attribution without excluded actions.
UX-DR6: Render Journey's scoped Insights banner, dated groups, actual morning/evening entry cards, truthful empty treatment, and exact card/day navigation; remove independent journal, source sample data, Filter, and unused Days controls.
UX-DR7: Render Daily entries for one local day and Entry detail's captured reading anatomy; implement the owner-approved More → Edit menu with Save/Cancel as an explicitly uncaptured adaptation.
UX-DR8: Render Trends period selector and bottom pager from Flow 49; Weeks/Months choice must update title, axes, labels, values, calendar density, and pager together without a Journey month browser.
UX-DR9: Show the three approved record-derived Trends count types with truthful zero/insufficient-data states; omit unsupported HealthKit, sample curves, percentages, inferred mood scores, and chart customization.
UX-DR10: Show Mood calendar date marks from saved evening feeling sets, with empty outlines and accessible date/value labels; update after record edits.
UX-DR11: Preserve Profile root/nested sheet navigation and scroll/title behavior, with only Notifications and Privacy destinations and a Back path to the parent context.
UX-DR12: Show only Morning Preparation and Evening Reflection rows with owner-approved captured descriptions; display real saved times, permission, and OS-effective switch states.
UX-DR13: Reproduce selected Privacy 64/02 layout and visible wording only through Error logs for internal screen comparison; invent no continuation or external-release policy.
UX-DR14: Implement the two measured light surface families, per-screen typography and spacing comparisons, distinct pill/circular/tile choice geometries, and source-specific SVG illustrations.
UX-DR15: Keep keyboard actions, long writing, dense history, sheets, and policy text reachable on smaller screens with safe areas, scrolling, dynamic type, and native platform controls.
UX-DR16: Expose VoiceOver/TalkBack names, roles, chosen/disabled states, reflection step counts, chart text alternatives, focus return from sheets, and reduced-motion-complete states.
UX-DR17: Show honest local-read, save, photo, permission, and no-data failure states with retry or in-scope recovery; never retain a dead source-only control.

### FR Coverage Map

FR-1: Epic 1 — Complete retained onboarding and enter Today.
FR-2: Epics 1–5 — Establish scoped navigation in Epic 1 and complete each destination with its owning epic.
FR-3: Epics 1–2 — Show current local day in Epic 1 and reflect committed completion in Epic 2.
FR-4: Epic 2 — Complete one morning reflection per local day.
FR-5: Epic 2 — Complete one evening reflection per local day with optional photo.
FR-6: Epic 1 — Open and return from Tomorrow with a live countdown.
FR-7: Epic 1 — Show a local Quote on Today.
FR-8: Epic 3 — Read committed reflections in Journey.
FR-9: Epic 3 — Read one stored day's Daily entries.
FR-10: Epic 3 — Read and safely edit Entry detail.
FR-11: Epic 4 — Switch and page Trends Weeks/Months periods.
FR-12: Epic 4 — Show the three approved record-derived Trends count types.
FR-13: Epic 4 — Show saved evening feelings by date in Mood calendar.
FR-14: Epic 5 — Navigate scoped Profile and internal Privacy screens.
FR-15: Epic 5 — Configure and deliver separate morning/evening local reminders; Epic 1 handles the onboarding permission boundary.
FR-16: Epics 2–5 — Establish durable completed records in Epic 2 and use them consistently in later readers and settings.
FR-17: Epic 2 — Choose a streak goal and derive streak state from completed dates.

## Epic List

### Epic 1: Complete onboarding and use Today
An internal tester can finish the retained onboarding sequence, open Today and Tomorrow, see a local Quote, and navigate the currently available scoped destinations with truthful empty completion state.
**FRs covered:** FR-1, FR-2, FR-3, FR-6, FR-7, FR-15 (onboarding permission boundary)

### Epic 2: Complete daily reflections
An internal tester can write one morning and one evening reflection for a local day, resume durable drafts, attach an optional evening photo, and see saved completion and streak state on Today and completion screens.
**FRs covered:** FR-3, FR-4, FR-5, FR-16, FR-17

### Epic 3: Read and edit reflection history
An internal tester can find committed reflections in Journey and Daily entries, read their details, and save or cancel edits without losing the previous committed record.
**FRs covered:** FR-2, FR-8, FR-9, FR-10, FR-16

### Epic 4: Review mood and reflection trends
An internal tester can inspect evening feelings by date and view the approved count metrics across coherent weekly and monthly Trends periods.
**FRs covered:** FR-2, FR-11, FR-12, FR-13, FR-16

### Epic 5: Manage Profile, Privacy, and reminders
An internal tester can navigate the scoped Profile screens and maintain two permission-backed reminder schedules at saved local times.
**FRs covered:** FR-2, FR-14, FR-15, FR-16

## Epic 1: Complete onboarding and use Today

An internal tester can finish the retained onboarding sequence, open Today and Tomorrow, see a local Quote, and navigate the currently available scoped destinations with truthful empty completion state.

### Story 1.1: Set up initial project from starter template

As an internal tester,
I want to launch the iOS or Android app and reach Today,
So that I can start the retained flow on a real device.

**Requirements:** FR-1, FR-2, FR-3; UX-DR2, UX-DR15, UX-DR16.

**Acceptance Criteria:**

**Given** a fresh internal install,
**When** I launch the app,
**Then** the Expo SDK 58 default starter and Expo Router dependencies are installed and configured for one internal Android/iOS app, and a minimal onboarding path reaches Today without a crash or excluded route.

**Given** onboarding has been completed,
**When** I restart the app,
**Then** I return to Today with the current device-local date and a truthful empty reflection state.

**Given** there are no saved reflections,
**When** I open the available Journey destination,
**Then** it shows an empty state without sample entries and both destinations have a working return path.

**Given** a small device or screen reader,
**When** I navigate the initial shell,
**Then** controls remain reachable and have readable labels.

### Story 1.2: Complete the retained onboarding sequence

As an internal tester,
I want to complete the retained onboarding choices,
So that my choices persist and I can enter Today.

**Requirements:** FR-1, FR-15; UX-DR1, UX-DR14, UX-DR15.

**Acceptance Criteria:**

**Given** a fresh install,
**When** I move through captured screens 01/01–12,
**Then** each retained choice and control state appears in captured order and the excluded 01/13 paywall never appears.

**Given** I selected an answer,
**When** I go Back and return to that step,
**Then** the prior selection remains.

**Given** the reminder-time step,
**When** I select separate morning and evening times with the native picker,
**Then** those times survive relaunch; notification denial does not trap onboarding or falsely show a reminder as active.

**Given** the AI Mentors card and the final retained step,
**When** I view the card and finish onboarding,
**Then** the card is display-only, no AI route opens, and relaunch goes directly to Today.

**Given** a retained onboarding screen,
**When** it is compared with its own selected capture at 393 × 852 and exercised on Android, a small screen, and a screen reader,
**Then** its visual hierarchy remains recognizable and every step stays reachable with readable labels.

### Story 1.3: See truthful Today states

As an internal tester,
I want Today to show the current day and reflection status,
So that I can tell what is available and completed.

**Requirements:** FR-2, FR-3; UX-DR2, UX-DR14, UX-DR16.

**Acceptance Criteria:**

**Given** no completed reflections,
**When** I open Today,
**Then** its date strip and dark or light cards show the current device-local day and truthful incomplete states without source sample answers.

**Given** the device date changes at midnight or while the app is backgrounded,
**When** Today is visible or returns to foreground,
**Then** the displayed day refreshes without moving any stored reflection to another day.

**Given** the selected Today captures,
**When** I compare the date strip, dark hero, paired light states, two-destination bar, and scoped SVG assets at the iOS baseline and on smaller screens,
**Then** the two measured light surface families and distinct dark hero match their intended hierarchy, remain accessible, and contain no excluded destination.

### Story 1.4: Open Tomorrow and read a local Quote

As an internal tester,
I want to preview Tomorrow and read a Quote on Today,
So that both retained informational surfaces work without unrelated actions.

**Requirements:** FR-6, FR-7; UX-DR5, UX-DR15.

**Acceptance Criteria:**

**Given** Today is open,
**When** I choose Tomorrow,
**Then** the read-only bird/countdown screen opens and displays the remaining time until the next device-local day.

**Given** Tomorrow remains open across a date change,
**When** the countdown reaches the boundary or the app returns to foreground,
**Then** its date and remaining time refresh and Back returns to the current Today.

**Given** Today is open,
**When** I read the Quote,
**Then** packaged local text and attribution are displayed without Quote Journal, Favorite, or Share actions.

**Given** selected Tomorrow and Quote captures,
**When** I compare them at 393 × 852 and exercise them with dynamic text and a screen reader,
**Then** the text and controls remain readable and the retained visual composition is recognizable.

## Epic 2: Complete daily reflections

An internal tester can write one morning and one evening reflection for a local day, resume durable drafts, attach an optional evening photo, and see saved completion and streak state on Today and completion screens.

### Story 2.1: Start and resume a morning reflection

As an internal tester,
I want my morning answers and current step saved while I write,
So that an interruption does not erase my work or count it as complete.

**Requirements:** FR-4, FR-16; UX-DR3, UX-DR17.

**Acceptance Criteria:**

**Given** I start a morning reflection,
**When** the session begins,
**Then** it receives a stable device-local YYYY-MM-DD dayKey and opens the retained sleep, Focus, and plan steps without AI follow-up steps.

**Given** I change an answer or step,
**When** I advance, close, or background the app,
**Then** the answer and position are durably flushed to a draft separate from completed rows.

**Given** a draft is interrupted by restart, midnight, or time-zone change,
**When** I resume it,
**Then** its original dayKey, answers, and step remain; it does not count in Today, Journey, Trends, Mood calendar, or streaks.

**Given** the first data migration or a draft write fails,
**When** the app reopens or attempts to save,
**Then** existing data is preserved, writes are blocked when the schema is unsafe, and the user sees a bounded retry state rather than an empty replacement database.

**Given** journal text or a photo is stored,
**When** the app persists the draft,
**Then** it stays in app-owned local storage without an app-managed account, backend, cloud sync, remote diary upload, or telemetry carrying journal content.

### Story 2.2: Complete one morning reflection

As an internal tester,
I want to finish a morning reflection,
So that my sleep, Focus, and plan are retained for that local day.

**Requirements:** FR-3, FR-4, FR-16; UX-DR2, UX-DR3, UX-DR15, UX-DR16.

**Acceptance Criteria:**

**Given** a morning draft,
**When** I select sleep, no more than three Focus choices, and write a plan,
**Then** the retained progress and circular advance controls lead to a completion screen without AI steps; the editor and forward action remain reachable above the keyboard.

**Given** a valid morning draft,
**When** I finish,
**Then** one transaction writes exactly one completed morning row for its original dayKey and clears the draft only after successful commit.

**Given** the row is committed,
**When** I revisit Today or relaunch,
**Then** Today shows the completed morning card and prevents a second morning completion for that same dayKey.

**Given** completion fails or a duplicate is attempted,
**When** I retry,
**Then** the previous committed row remains intact, my unsaved answers stay available, and no duplicate completion appears.

### Story 2.3: Complete one evening reflection

As an internal tester,
I want to record my evening rest, feelings, summary, and bedtime response,
So that the day ends with one durable reflection.

**Requirements:** FR-3, FR-5, FR-16; UX-DR2, UX-DR4, UX-DR15.

**Acceptance Criteria:**

**Given** I start an evening reflection,
**When** I enter rest, choose one or more feelings, write a summary, and choose Yes, No, or Skip & Finish,
**Then** the retained rest slider, multi-select feeling tiles, summary editor, and completion states remain reachable without AI writing controls.

**Given** I expand the feeling choices,
**When** I continue or resume after restart,
**Then** expansion remains part of one progress step and all selected feelings survive.

**Given** I finish a valid evening draft,
**When** the transaction commits,
**Then** one completed evening row exists for the session's original dayKey, Today reflects completion, and the same-day duplicate path is disabled.

**Given** the app closes mid-flow or a completion write fails,
**When** I resume,
**Then** the draft and prior completed data remain available without a false completion state.

### Story 2.4: Keep an optional evening photo

As an internal tester,
I want to attach, replace, or remove an evening photo,
So that it remains available with my reflection after relaunch.

**Requirements:** FR-5, FR-16; UX-DR4, UX-DR17.

**Acceptance Criteria:**

**Given** I select a photo,
**When** it is added to an evening draft,
**Then** the app copies it to app-owned persistent storage before saving a relative reference and displays it after relaunch.

**Given** permission is denied or a selected photo cannot be copied,
**When** I return to the evening flow,
**Then** written answers remain available and I can retry or explicitly continue without a photo.

**Given** a photo already selected in an evening draft,
**When** I replace or remove it before completion,
**Then** the draft references only the intended app-owned file and a failed replacement preserves the prior draft photo and answers.

**Given** a restored row references unavailable media,
**When** its completion state reopens,
**Then** the app shows a bounded unavailable-media state without hiding the reflection text.

### Story 2.5: Choose and see a truthful streak

As an internal tester,
I want to choose whether to see a streak and set its goal,
So that Today and completion screens reflect my actual completed days.

**Requirements:** FR-17; UX-DR2, UX-DR3.

**Acceptance Criteria:**

**Given** my first successful morning or evening completion,
**When** the completion flow opens,
**Then** the retained one-time streak visibility and goal choices appear and persist after relaunch.

**Given** both reflection kinds exist on one local day,
**When** a streak is calculated,
**Then** that day counts once; consecutive completed dayKeys extend the streak and skipped days break it.

**Given** I hide the streak or change the goal,
**When** Today and completion screens render,
**Then** the UI honors the saved choice without deleting history or storing an independently drifting streak counter.

**Given** date rollover or relaunch,
**When** streak projections refresh,
**Then** they use committed completed dayKeys and remain consistent on all visible surfaces.

## Epic 3: Read and edit reflection history

An internal tester can find committed reflections in Journey and Daily entries, read their details, and save or cancel edits without losing the previous committed record.

### Story 3.1: Find and read committed reflections

As an internal tester,
I want Journey cards to open the reflection I saved,
So that I can review my actual morning and evening answers.

**Requirements:** FR-2, FR-8, FR-16; UX-DR6, UX-DR7, UX-DR15, UX-DR17.

**Acceptance Criteria:**

**Given** no completed rows,
**When** I open Journey,
**Then** it shows a truthful empty state with no source sample entries, independent journal, dead Filter, or Journey month browser.

**Given** completed rows on multiple dates,
**When** I open Journey,
**Then** dated groups, scoped Insights banner, and morning/evening cards derive only from committed records in stable date order.

**Given** I select a card,
**When** Entry detail opens,
**Then** it shows the exact saved row's authored values and available photo, even after relaunch, with the selected capture's reading anatomy.

**Given** a long record or screen reader,
**When** I read Journey or Entry detail,
**Then** every saved value and return control remains reachable and clearly labeled.

**Given** the local record read fails,
**When** Journey or Entry detail attempts to render,
**Then** it shows a bounded error and retry path without presenting an empty history as if it were the saved truth.

### Story 3.2: Browse one day's entries

As an internal tester,
I want to open a day's entries from Journey,
So that I see only reflections saved for that local day.

**Requirements:** FR-9; UX-DR6, UX-DR7.

**Acceptance Criteria:**

**Given** Journey has headings for two dates,
**When** I select one heading,
**Then** Daily entries lists only completed morning and evening rows with that stored dayKey.

**Given** a selected day has no completed rows,
**When** Daily entries opens,
**Then** it shows an honest empty state without borrowing another day's entries.

**Given** I return from Daily entries,
**When** Journey reappears,
**Then** the selected day and prior scroll context are restored.

### Story 3.3: Edit an Entry detail safely

As an internal tester,
I want to correct a saved reflection from Entry detail,
So that every reading surface shows the corrected committed value.

**Requirements:** FR-10, FR-16; UX-DR7, UX-DR10, UX-DR17.

**Acceptance Criteria:**

**Given** a saved Entry detail,
**When** I open the captured More control,
**Then** its owner-approved menu offers Edit; the editor offers Save and Cancel and labels this uncaptured adaptation clearly.

**Given** I change an in-scope answer or evening photo,
**When** I select Cancel,
**Then** no committed row or app-owned photo changes and the prior detail remains visible.

**Given** I select Save,
**When** the edit transaction succeeds,
**Then** the row keeps its original dayKey and kind, replacement media is staged safely, and existing Journey, Daily entries, Today, and streak readers refresh only after commit.

**Given** Save or photo replacement fails,
**When** the editor reports the error,
**Then** the previous committed row and photo remain intact, unsaved input stays in the editor, and retry is available.

**Given** the app relaunches after a successful edit,
**When** I reopen the record,
**Then** the edited values persist and no unrelated date or record changed.

## Epic 4: Review mood and reflection trends

An internal tester can inspect evening feelings by date and view the approved count metrics across coherent weekly and monthly Trends periods.

### Story 4.1: See evening feelings in Mood calendar

As an internal tester,
I want a calendar mark for each day with saved evening feelings,
So that I can revisit the feelings I recorded without an invented mood score.

**Requirements:** FR-2, FR-13; UX-DR10, UX-DR16.

**Acceptance Criteria:**

**Given** an evening reflection with multiple feelings,
**When** I open Mood calendar,
**Then** its stored local day has one recorded-day mark whose accessible label lists the full saved feeling set.

**Given** a day without committed evening feelings,
**When** I view it in the calendar,
**Then** it remains an empty date state rather than a sample mark or scalar mood value.

**Given** I successfully edit an evening feeling set,
**When** Mood calendar refreshes or the app relaunches,
**Then** the affected date shows the new set and unrelated dates do not change.

**Given** the selected Mood calendar capture and a screen reader,
**When** I inspect dates and marks,
**Then** layout, date labels, value alternatives, and small-screen scrolling remain usable; standalone mood check-in is absent.

### Story 4.2: Read the approved Trends counts

As an internal tester,
I want Trends to count my saved reflection activity,
So that its numbers match what I actually completed.

**Requirements:** FR-12, FR-16; UX-DR9, UX-DR16, UX-DR17.

**Acceptance Criteria:**

**Given** a selected week with both morning and evening rows on one day,
**When** Trends calculates its counts,
**Then** the completed-day count includes that day once and the morning and evening completion counts include their rows separately.

**Given** a completed evening row with multiple feelings,
**When** Trends calculates feeling counts,
**Then** each selected feeling contributes once to its category for that row and no scalar score or inferred percentage is created.

**Given** no rows or insufficient days for a chart,
**When** I open Trends,
**Then** cards and chart areas show truthful zero or insufficient-data states without sample curves, HealthKit figures, or unsupported categories.

**Given** a successful edit or relaunch,
**When** the selected period recalculates,
**Then** values come from committed records only and VoiceOver or TalkBack can read a text summary of each chart.

### Story 4.3: Switch and page coherent Trends periods

As an internal tester,
I want to switch between Weeks and Months and page through periods,
So that every Trends label and value describes the same dates.

**Requirements:** FR-11, FR-12; UX-DR8, UX-DR9, UX-DR16.

**Acceptance Criteria:**

**Given** Trends is open,
**When** I switch Weeks to Months or back,
**Then** the heading, date range, axes, values, cards, calendar density, and bottom pager all use the newly selected period.

**Given** I page across a week, month, or year boundary,
**When** the new period renders,
**Then** its range and approved counts reflect only committed rows within that period.

**Given** a reflection is edited while a period is selected,
**When** Trends refreshes,
**Then** affected periods recompute, unrelated periods remain stable, and the current selection is retained.

**Given** selected Flow 49 and Trends captures,
**When** I compare the week and month states at 393 × 852 and use a screen reader or smaller device,
**Then** the selector and pager remain operable and no Journey month browser, Years aggregate, or dead chart control appears.

## Epic 5: Manage Profile, Privacy, and reminders

An internal tester can navigate the scoped Profile screens and maintain two permission-backed reminder schedules at saved local times.

### Story 5.1: Open scoped Profile and Privacy screens

As an internal tester,
I want to open Profile and read its internal Privacy screen,
So that I can return to the same context without unrelated settings routes.

**Requirements:** FR-2, FR-14; UX-DR11, UX-DR13, UX-DR15, UX-DR16.

**Acceptance Criteria:**

**Given** Today is open,
**When** I open Profile and its nested Privacy screen,
**Then** the selected root and nested sheet anatomy, titles, scroll positions, Back, and Close controls preserve their parent context.

**Given** the internal screen-comparison build,
**When** I read Privacy,
**Then** the selected 64/02 wording is reproduced through the visible Error logs heading, including captured iCloud, AI, and analytics statements, with no invented continuation.

**Given** Profile is open,
**When** I inspect available destinations,
**Then** the Privacy path works; excluded settings and dead controls are absent.

**Given** long policy text, dynamic type, or a screen reader,
**When** I scroll and return,
**Then** content and controls stay reachable, focus returns to its originating Profile control, and the build documentation identifies this as internal capture reproduction rather than an external-release privacy policy.

### Story 5.2: Set one effective morning reminder

As an internal tester,
I want to set a Morning Preparation reminder,
So that my device alerts me at the saved local time only when permission and scheduling succeed.

**Requirements:** FR-15, FR-16; UX-DR12, UX-DR17.

**Acceptance Criteria:**

**Given** the Notifications screen,
**When** I select a morning time with the native picker and enable its switch,
**Then** the saved time survives relaunch and one local schedule is installed only after required OS notification and Android exact-alarm access succeed.

**Given** Profile is open after the morning reminder is available,
**When** I select Notifications,
**Then** its nested screen opens and Back returns to the prior Profile context.

**Given** permission is denied or scheduling fails,
**When** I return to Notifications,
**Then** the effective switch remains off, the saved preference is distinguishable from OS-effective state, and a retry path is visible.

**Given** permission and scheduling succeed on physical Android and iOS devices,
**When** the selected local time arrives,
**Then** one Morning Preparation alert is delivered and the effective switch remains accurate after foreground return or relaunch.

**Given** I disable the morning reminder,
**When** the selected time arrives,
**Then** its schedule has been removed and no morning alert is delivered.

### Story 5.3: Configure the evening reminder separately

As an internal tester,
I want a separate Evening Reflection reminder,
So that its time and enabled state can differ from the morning reminder.

**Requirements:** FR-15, FR-16; UX-DR12.

**Acceptance Criteria:**

**Given** Notifications is open,
**When** I inspect the two rows,
**Then** they show `Morning Preparation` / `Reminder to prepare for your day in the morning` and `Evening Reflection` / `Reminder to wind down and reflect about your day`, actual saved times, and OS-effective switch states; unrelated source reminder rows are absent.

**Given** both reminders are configured at different times,
**When** I relaunch and wait for their selected times on physical Android and iOS devices,
**Then** each enabled reminder delivers once at its own local time and a disabled reminder does not deliver.

**Given** a time picker is open,
**When** I cancel it,
**Then** the saved time and effective schedule remain unchanged.

**Given** an onboarding time was previously chosen,
**When** I open Notifications,
**Then** the corresponding reminder row shows that same saved value without silently enabling an unscheduled alert.

### Story 5.4: Reconcile reminders after changes

As an internal tester,
I want reminder switches and delivery to stay accurate after time or permission changes,
So that I do not receive missing or duplicate alerts.

**Requirements:** FR-15; UX-DR12, UX-DR17.

**Acceptance Criteria:**

**Given** an enabled reminder,
**When** I choose a new time,
**Then** the old schedule is replaced with at most one effective schedule at the new local time and the other reminder remains unchanged.

**Given** replacement scheduling fails,
**When** the app reports the result,
**Then** it preserves the prior effective time where the OS still has that schedule, avoids duplicates, and displays the actual effective state.

**Given** OS permission or Android exact-alarm access is revoked or restored,
**When** the app enters foreground or relaunches,
**Then** it reconciles permission and installed schedules before displaying each switch; revoked access clears effective state.

**Given** the device time zone or local clock changes,
**When** reminders are reconciled,
**Then** each enabled alert follows its saved local time with no stale duplicate schedule.
