---
type: initiative
title: DiaryClone
parent: none
sources:
  - _bmad-output/planning-artifacts/briefs/brief-diary-clone-2026-10-22/brief.md
  - _bmad-output/planning-artifacts/prds/prd-diary-clone-2026-10-22/prd.md
companions:
  - _bmad-output/planning-artifacts/architecture/architecture-diary-clone-2026-10-22/architecture.md
  - _bmad-output/planning-artifacts/ux-designs/ux-diary-clone-2026-10-22/DESIGN.md
  - _bmad-output/planning-artifacts/ux-designs/ux-diary-clone-2026-10-22/EXPERIENCE.md
risk: high
---

# DiaryClone

## Description

Build an internal Android and iOS clone of the selected Stoic diary flows as a working local-first foundation for later product work. Only the flows selected in the product brief are implementation scope.

## Outcome

Internal testers can complete, revisit, and edit daily reflections on both platforms, with the selected screens matching their captures and showing consistent device data.

## Requirements

- R1 (PRD FR-1): A tester completes the selected onboarding screens, skips the excluded final screen, sees the display-only AI Mentors card, and reaches Today without an AI route.
- R2 (PRD FR-2): Every retained screen and control has a working selected route or action, and excluded feature entry points are absent.
- R3 (PRD FR-3): Today displays the device-local date and real morning/evening completion state before and after relaunch.
- R4 (PRD FR-4): One morning reflection per local day records sleep, at most three focus choices, and written plans; it persists and can later be edited in Entry detail.
- R5 (PRD FR-5): One evening reflection per local day records rest, one or more feelings, summary, optional persistent photo, and Yes/No/Skip bedtime response; photo permission denial does not prevent a text record.
- R6 (PRD FR-6): Tomorrow opens from Today, shows a date-correct countdown, and returns without out-of-scope actions.
- R7 (PRD FR-7): Today displays a local Quote without Quote journal, Favorite, or Share controls.
- R8 (PRD FR-8): Journey lists only stored reflections, with honest empty and populated states.
- R9 (PRD FR-9): Daily entries displays only reflections belonging to the selected date.
- R10 (PRD FR-10): Entry detail reads and edits a stored reflection; a successful edit refreshes other views and a failed save preserves the prior record.
- R11 (PRD FR-11): Trends switches Weeks/Months and pages the selected period; its title, date range, charts, and values stay synchronized with saved data. Journey month browsing is excluded.
- R12 (PRD FR-12): Trends & insights derives eligible values from stored records and feelings for the selected period, with honest insufficient-data states.
- R13 (PRD FR-13): Mood calendar derives date marks from saved evening feelings and refreshes after edits without inventing missing values.
- R14 (PRD FR-14): Profile opens scoped Notifications and Privacy policy screens, allows return, and exposes no excluded settings.
- R15 (PRD FR-15): Morning and evening local reminders keep separately editable times across relaunch, reflect actual OS permission and effective scheduling, fire at the selected time when enabled, and stop when disabled.
- R16 (PRD FR-16): Completed records, edits, feelings, and attached photos persist on device across relaunch and feed one consistent source for all reading surfaces.
- R17 (PRD FR-17): The first completed reflection offers streak visibility and goal choice once; Today and completion screens derive streak days from actual completed dates.

## Constraints

- PRD section 5: English app copy; the same app-screen design on Android and iOS, with platform-native system UI.
- PRD section 5: Compare retained screens with the selected captures, starting at the 393 × 852 iOS baseline; use SVG for retained illustrations and icons, and keep smaller devices usable.
- PRD sections 5–6: No runtime account, cloud sync, remote journal upload, example records, invented statistics, or new AI capability.
- Architecture AD-1–10: Use one committed local record source, stable day keys, durable drafts, transactional completion/edit, app-owned photo files, versioned migrations, derived views, and permission-backed reminder state.

## Done when

- All selected flows run end to end on Android and iOS without dead controls or duplicate daily completion.
- Saved and edited records, photos, mood values, and streak preferences survive relaunch and agree across Today, Journey, detail, daily entries, and Trends week/month views.
- Retained screens pass capture comparison for layout, color, typography, and SVG assets at the baseline and remain usable on actual device sizes.
- The two scoped reminders reflect OS permission, persist chosen times, and deliver or stop on physical devices as configured.
- No excluded route, card, example data, AI action, account, or sync feature enters this internal clone.

## Boundaries

The tracer path is onboarding → Today → one saved reflection → Journey/detail → derived insights; Profile/reminders is a second device integration path. The internal app is the only deployable unit. The OS notification scheduler, photo picker, SQLite, and local file system are touch points owned by the epics below.

- Touch point: Expo app scaffold, routing, SQLite schema, and local settings — owned by epic-foundation.
- Touch point: photo picker and app-owned media files — owned by epic-reflections.
- Touch point: OS notification permission and scheduler — owned by epic-reminders.
- Must not add unselected Stoic flows, independent journaling or mood check-ins, AI features, accounts, cloud sync, or multilingual screens.

## References

- product brief — _bmad-output/planning-artifacts/briefs/brief-diary-clone-2026-10-22/brief.md, scope and completion criteria
- prd — _bmad-output/planning-artifacts/prds/prd-diary-clone-2026-10-22/prd.md, FR-1–17 and section 7
- architecture — _bmad-output/planning-artifacts/architecture/architecture-diary-clone-2026-10-22/architecture.md, AD-1–10
- design — _bmad-output/planning-artifacts/ux-designs/ux-diary-clone-2026-10-22/DESIGN.md
- experience — _bmad-output/planning-artifacts/ux-designs/ux-diary-clone-2026-10-22/EXPERIENCE.md

## Notes

- Assumption: The source documents' current internal-clone scope is the approved input for this breakdown; epic boundaries can be revised before build.
- Decision: Entry detail uses the captured `More` control to open an owner-approved `Edit` action with `Save` and `Cancel`.
- Decision: Trends uses completed-day count, separate morning/evening completion counts, and evening feeling selection counts over the selected week or month.
- Decision: The internal clone reproduces the visible Privacy copy through `Error logs` and the two captured reminder-row texts; the source Privacy copy is not a factual policy for external distribution.
- Assumption: A Mood calendar day with multiple feelings uses one recorded-day mark and an accessible label listing every saved feeling; no scalar score is inferred.
- Decision: 2026-10-22 — Split into foundation, reflections, history/editing, insights, and reminders/Privacy by independently demonstrable outcomes; all remain in one Expo app deployment.
- Decision: 2026-10-22 — The foundation first proves launch, persisted onboarding, and Today; the next epic saves and reopens a morning reflection before derived views.

## UX handoff

When running `bmad-ux`, use the companion product brief for the clone scope. All screens in `docs/Stoic/flows` may inform the design system and future component patterns; only the flows selected in the brief are implementation scope for this stage.
