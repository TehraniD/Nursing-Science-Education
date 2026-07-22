# 🔍 Quality Assessment — `regimen.html`

**Component:** Regimen — Personal Tracker (single-file client-side app)
**Live URL:** https://tehranilabs.org/regimen.html
**Date:** July 22, 2026
**Status:** ✅ **PASSED with fixes applied** — 3 correctness bugs, 3 robustness/a11y gaps, and hygiene issues resolved. No clinical logic altered.

---

## 📋 Executive summary

Regimen is a well-architected, dependency-free personal health tracker: ~1,730 lines of
HTML + CSS + vanilla JS in one file, all state in `localStorage`, **zero network calls**.
Design quality is high — a coherent design-token system, light/dark theming, `prefers-reduced-motion`
support, tabular-numeric typography, SVG charts that render with no external library, CSV/JSON
export, and a print-ready clinician summary.

The build was **not tracked in version control** despite being served live from this repo's
GitHub Pages domain. This assessment brings it under source control, fixes the defects found,
and documents a prioritized backlog. **The JavaScript parsed with zero syntax errors** before
and after the changes, and the app **renders correctly in headless Chromium** in standards mode.

Scope boundary: all **clinical** content (PK model parameters, hormone dosing, the Ganzoni
iron formula, GLP-1 titration ladders, lab reference ranges) was left **byte-for-byte
unchanged**. Those are clinical judgments for the clinician-user to verify; they are listed
below for review, not edited.

---

## 🧱 Architecture overview

| Layer | Approach | Assessment |
|-------|----------|------------|
| Structure | Single HTML file, no build step, no dependencies | ✅ Excellent for a private, portable, offline tool |
| State | `localStorage` (`tehrani.regimen.v1`), schema-versioned, seeded on first run | ✅ Solid; JSON export/import present |
| Rendering | Hand-rolled hyperscript (`el()`) + hash-less router (`go()`/`render()`) | ✅ Clean and readable |
| Charts | Inline SVG (`sparkline`, `svgLineChart`) with an optional Chart.js hook | ⚠️ Chart.js hook is dead code (see F9) |
| Privacy | No network transmission; data local-only; explicit "Danger zone" wipe | ✅ Strong; enhanced with `noindex` |
| Pages | Today · Log · Regimen · Injections · Labs · Trends · PK & Calc · Data | ✅ Comprehensive |

---

## 🐞 Findings & resolutions

Severity: 🔴 correctness/reachability · 🟠 robustness/accessibility · 🟡 hygiene/polish

### 🔴 F1 — Two pages were unreachable on mobile — **FIXED**
`mobileIds` listed only 6 of 8 routes; `inject` and `pk` were omitted. Because the desktop
rail is `display:none` at ≤780px, **Injections and PK & Calculators could not be opened on a
phone at all.** Fix: all 8 routes now appear in the bottom tab bar with concise labels
(`Meds`, `Sites`, `PK`, …); the grid was widened to 8 columns with ellipsis-guarded labels.
*Verified:* headless render shows mobile tabs `Today | Log | Meds | Sites | Labs | Trends | PK | Data`.

### 🔴 F2 — `biweekly` frequency broke adherence math — **FIXED**
"Every 2 weeks" was selectable in the medication form but unhandled in `expectedDoses()`
(fell through to `return days`) and `isDueToday()` (fell through to a 7-day interval). A
biweekly medication reported ~7% adherence over 30 days and wrong "due today" status. Fix:
added a `biweekly` branch (÷14 days; 14-day due interval).
*Verified by unit test:* `expectedDoses({freq:'biweekly'}, 30) === 2` (was `30`).

### 🔴 F3 — `custom` frequency was inert — **FIXED**
"Custom" was selectable but no input ever wrote `freqDetail.intervalDays`, so it silently
behaved like weekly. Fix: the medication panel now reveals a **"Custom interval (days between
doses)"** field when frequency = custom, and persists it; `expectedDoses`/`isDueToday` already
consumed `freqDetail.intervalDays`.

### 🟠 F4 — Missing document scaffolding → quirks mode — **FIXED**
The document began at `<title>` with **no `<!doctype html>`**, forcing browsers into
**quirks mode**, and had no `<html lang>`, `<head>`, or `<meta charset>` (encoding relied
solely on the HTTP header, so a local/`file://` open could mojibake the em-dashes and `·`/`✓`
glyphs). Fix: proper `<!doctype html><html lang="en"><head>…</head><body>` wrapper, explicit
`<meta charset="utf-8">`, a `<meta name="description">`, light+dark `theme-color`, and an
inline-SVG favicon. *Verified:* `<!DOCTYPE html>` present in the rendered DOM (standards mode).

### 🟠 F5 — Modal dialogs lacked keyboard accessibility — **FIXED**
Panels declared `role="dialog" aria-modal="true"` but did not move focus into the dialog,
trap Tab, close on **Escape**, or restore focus to the opener on close. Fix: `openPanel()`
now captures the previously-focused element, focuses the first field on open, traps Tab within
the panel, and closes on Escape; `closePanel()` restores focus. An `aria-label` (the panel
title) was added to the dialog.

### 🟠 F6 — User text interpolated into `innerHTML` without escaping — **FIXED**
`entryDetail()`, the medication swatch, and `clinicianSummaryHtml()` inserted note text, tags,
medication names, and analytes into `innerHTML`. Beyond the self-XSS smell, a benign note like
`"felt < 100%"` would corrupt rendering. Fix: added an `esc()` helper and applied it to every
user-supplied interpolation. *Verified by unit test:* all of `& < > " '` are escaped.

### 🟡 F7 — Dead code — **FIXED**
Removed an unused `const now` (Injections page) and an unused `const analytes` (Labs page).

### 🟡 F8 — Discoverability vs. "not for distribution" — **FIXED**
The banner says "Not for distribution," yet nothing discouraged search indexing. Added
`<meta name="robots" content="noindex, nofollow">`. (Note: this reduces indexing only; the
file remains publicly served — see recommendations.)

### 🟡 F9 — Misleading Chart.js note — **OPEN (recommendation)**
The Trends page shows "Chart.js detected — richer interactive charts would render here" but no
code path ever renders a Chart.js chart. Left as-is to avoid behavioral change; recommend
either wiring a real Chart.js chart (with a pinned SRI hash) or removing the hook and note.

---

## ✅ Verified good (no change needed)

- JavaScript parses with **zero syntax errors** (before and after).
- App **renders in headless Chromium** with the 5 seeded medications and full navigation.
- CSV export quotes and escapes every cell; JSON import gates on a schema `version`.
- Light/dark theming, `prefers-reduced-motion`, `:focus-visible`, and iOS safe-area insets
  are all handled.
- `<label class="field">`-wrapped inputs use valid implicit association.
- Charts render with no third-party dependency.

---

## ⚕️ Clinical content — flagged for clinician review (intentionally NOT modified)

These are population estimates and label references embedded in the app. They are **not code
defects** and were left unchanged; the clinician-user should confirm them against current
references and individual labs:

- **PK models** — one-compartment ka/ke/F for estradiol esters (valerate/cypionate/enanthate)
  and testosterone cypionate, plus the empirical serum-scaling factors (`×40` for E2, `×6.5`
  for T). Y-axes are explicitly labeled "scaled" estimates.
- **Ganzoni iron deficit** — `weight × ΔHb × 2.4 + storage iron`; product-specific per-infusion
  caps noted in the UI.
- **GLP-1 titration ladders** — semaglutide and tirzepatide escalation schedules.
- **Seeded reference ranges** — the eleven default analyte target ranges are demo defaults and
  are already user-editable; the UI correctly labels them "personal targets," not lab reference
  intervals.

---

## 🚀 Recommended expansions (prioritized backlog)

1. **PWA** — add a web-app manifest + service worker. An offline, local-first health tool is an
   ideal installable PWA (home-screen icon, reliable offline load).
2. **Encryption at rest** — optional passphrase to encrypt the `localStorage` blob; health data
   currently sits in plaintext readable by any script on the origin.
3. **Edit + undo for entries** — the Log page deletes but cannot edit; deletions have no undo.
4. **Chart annotations** — mark dose changes on the weight/appetite trends; surface Tmax and
   half-life readouts alongside the PK curves.
5. **Injection-site suggestion** — recommend the least-recently-used site from the rotation map.
6. **Dose reminders** — optional local notifications for due doses.
7. **Resolve F9** — wire real Chart.js (pinned SRI) or delete the dead hook.
8. **Test harness** — the pure helpers (`bmi`, `expectedDoses`, `interpretLab`, the PK
   summation) are directly unit-testable; a tiny test file would prevent regressions like F2.
9. **Hosting posture** — if "not for distribution" is a hard requirement, consider moving this
   file behind auth or out of the public Pages site; `noindex` alone does not restrict access.

---

## 🔬 How this was verified

- **Static:** `new Function(scriptBody)` parse check (no syntax errors); structural greps for
  doctype/head/charset/lang and tag balance.
- **Unit:** extracted the real `expectedDoses` and `esc` from the file and asserted behavior
  (biweekly cadence; all five HTML metacharacters escaped).
- **Runtime:** headless Chromium `--dump-dom` — confirmed the app boots and renders (seeded
  meds, nav, brand), `<!DOCTYPE html>` present (standards mode), and the mobile tab bar exposes
  all eight routes including the two that were previously unreachable.
