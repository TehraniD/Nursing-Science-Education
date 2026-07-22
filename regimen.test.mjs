/* =========================================================
   Regimen — regression tests
   Dependency-free. Extracts the *actual* pure functions from
   regimen.html (so the tests exercise shipped code, not a copy)
   and asserts their behavior. Also sanity-checks the PWA files.

   Run:  node regimen.test.mjs
   Exits non-zero on any failure (CI-friendly).
   ========================================================= */
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(here, 'regimen.html'), 'utf8');

/* Pull a top-level `function name(...) {...}` out of the source by
   brace-matching. The targeted helpers contain no unbalanced brace
   inside a string/regex, so a plain counter is safe here. */
function extract(src, name) {
  const start = src.indexOf('function ' + name + '(');
  if (start < 0) throw new Error('function not found: ' + name);
  const open = src.indexOf('{', start);
  let depth = 0;
  for (let i = open; i < src.length; i++) {
    if (src[i] === '{') depth++;
    else if (src[i] === '}' && --depth === 0) return src.slice(start, i + 1);
  }
  throw new Error('unbalanced braces for: ' + name);
}
const materialize = (name) => new Function('return (' + extract(html, name) + ')')();

const expectedDoses = materialize('expectedDoses');
const esc           = materialize('esc');
const bmi           = materialize('bmi');
const bmiCategory   = materialize('bmiCategory');
const interpretLab  = materialize('interpretLab');
const daysBetween   = materialize('daysBetween');
const kgFromLbs     = materialize('kgFromLbs');
const lbsFromKg     = materialize('lbsFromKg');

/* Tiny test runner ------------------------------------------------ */
let passed = 0, failed = 0;
const AP = String.fromCharCode(39); // apostrophe (quote-safe)
function eq(actual, expected, msg) {
  const a = JSON.stringify(actual), e = JSON.stringify(expected);
  if (a === e) { passed++; }
  else { failed++; console.error(`  ✗ ${msg}\n      expected ${e}\n      got      ${a}`); }
}
function ok(cond, msg) { if (cond) passed++; else { failed++; console.error(`  ✗ ${msg}`); } }
function group(name, fn) { console.log('• ' + name); fn(); }

/* expectedDoses — the adherence math (regression guard for the biweekly bug) */
group('expectedDoses', () => {
  eq(expectedDoses({ freq: 'daily' }, 30), 30, 'daily / 30d');
  eq(expectedDoses({ freq: 'weekly' }, 30), 4, 'weekly / 30d');
  eq(expectedDoses({ freq: 'biweekly' }, 30), 2, 'biweekly / 30d (was buggy = 30)');
  eq(expectedDoses({ freq: 'biweekly' }, 90), 6, 'biweekly / 90d');
  eq(expectedDoses({ freq: 'twice-weekly' }, 7), 2, 'twice-weekly / 7d');
  eq(expectedDoses({ freq: 'every-other-day' }, 30), 15, 'every-other-day / 30d');
  eq(expectedDoses({ freq: 'custom', freqDetail: { intervalDays: 10 } }, 30), 3, 'custom q10d / 30d');
  eq(expectedDoses({ freq: 'custom', freqDetail: {} }, 28), 4, 'custom w/o interval defaults to weekly');
});

/* esc — output escaping */
group('esc', () => {
  eq(esc('a < b & c > d'), 'a &lt; b &amp; c &gt; d', 'lt/amp/gt');
  eq(esc('"' + AP), '&quot;&#39;', 'double + single quote');
  eq(esc('<img src=x onerror=alert(1)>'), '&lt;img src=x onerror=alert(1)&gt;', 'tag neutralized');
  eq(esc(null), '', 'null -> empty');
  eq(esc(undefined), '', 'undefined -> empty');
  eq(esc(5), '5', 'number -> string');
});

/* bmi + category */
group('bmi / bmiCategory', () => {
  eq(bmi(80, 180), 24.7, 'bmi(80kg,180cm)');
  eq(bmi(0, 180), null, 'bmi with 0 weight -> null');
  eq(bmi(80, 0), null, 'bmi with 0 height -> null');
  eq(bmiCategory(17).label, 'Underweight', '<18.5 underweight');
  eq(bmiCategory(22).label, 'Normal', '22 normal');
  eq(bmiCategory(27).label, 'Overweight', '27 overweight');
  eq(bmiCategory(32).label, 'Obese', '32 obese');
  eq(bmiCategory(null).label, '—', 'null -> em dash');
});

/* interpretLab — personal-range flagging */
group('interpretLab', () => {
  const r = { low: 100, high: 200, unit: 'pg/mL' }; // span 100, 25% margin = 25
  eq(interpretLab(150, r).cls, 'good', 'in range');
  eq(interpretLab(90, r).cls, 'warn', 'just below');
  eq(interpretLab(70, r).cls, 'crit', 'well below (>25% under)');
  eq(interpretLab(210, r).cls, 'warn', 'just above');
  eq(interpretLab(230, r).cls, 'crit', 'well above (>25% over)');
  eq(interpretLab(150, null).label, 'no range', 'no range configured');
});

/* unit conversions round-trip */
group('unit conversions', () => {
  ok(Math.abs(kgFromLbs(220) - 99.79024) < 1e-4, 'lbs->kg');
  ok(Math.abs(lbsFromKg(kgFromLbs(154)) - 154) < 1e-6, 'kg<->lbs round-trip');
  eq(daysBetween('2026-01-01', '2026-01-15'), 14, 'daysBetween 14');
});

/* PWA asset sanity ------------------------------------------------ */
group('PWA assets', () => {
  const manifest = JSON.parse(readFileSync(join(here, 'regimen.webmanifest'), 'utf8'));
  eq(manifest.scope, './regimen.html', 'manifest scope narrow to the page');
  eq(manifest.start_url, './regimen.html', 'manifest start_url');
  ok(manifest.display === 'standalone', 'manifest display standalone');
  ok(Array.isArray(manifest.icons) && manifest.icons.length > 0, 'manifest has an icon');

  const sw = readFileSync(join(here, 'sw.js'), 'utf8');
  // Syntax-check the worker without executing it (SW globals are stubbed at parse time).
  new Function('self', 'caches', 'fetch', sw);
  ok(/scope: '\.\/regimen\.html'/.test(html), 'SW registered with narrow scope in regimen.html');
  ok(html.includes('rel="manifest"'), 'manifest linked from regimen.html');
});

/* ---------------------------------------------------------------- */
console.log(`\n${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
