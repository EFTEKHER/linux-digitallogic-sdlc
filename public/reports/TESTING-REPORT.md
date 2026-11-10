# Verification report

Date: 10 November 2026 (Asia/Dhaka)

## Source audit

- PDF count verified with `pdfinfo`: **55 pages**; a text-bearing PDF, not a scan-only document.
- All 55 pages rendered as JPEG and surveyed in contact sheets. No page intentionally omitted.
- Printed numbers preserved separately: source cover and study-plan pages are unnumbered; numbered body is generally PDF page minus 2, while PDF page 2 shows printed 2.
- Actual body: introduction (PDF 1–3), Part 0 final revision (4–9), Part 1 Linux (10–16), Part 2 numbers/codes/Boolean (17–22), Part 3 K-map (23–29), Part 4 gates/circuits (30–35), Part 5 processor/assembly (36–42), Part 6 SDLC (43–51), Part 7 bank (52–55).
- Front contents numbering disagrees with the actual body. The “4-page revision” section spans six PDF pages.
- 18 errors/qualifications recorded, including octal fractional conversion, binary subtraction, parity, ASCII D, Boolean consensus, comparator row count/grouping, Unicode width, and verification/validation wording.
- Complement bars and some mathematical symbols are damaged in plain text extraction. Original page images remain the authoritative source, and extracted bank rows explicitly warn about this.
- 97 original bank rows have a reveal-answer interface; their mathematical transcriptions are not certified. Original source questions are distinguished from 57 newly authored MCQs.
- 55 page-level bilingual lessons, 52 source-linked worked/numerical illustrations, 10 calculator types, and 261 recall cards.

This report supports **source preservation and page-level mapping**, not 100% line-by-line teaching coverage. Some detailed source topics and exercises still need richer bespoke bilingual lessons. Every topic remains accessible in original source form.

## Unit/calculation verification

`npm test`: **11 test groups passed**.

Known answers include 1101.11₂ = 13.75₁₀, corrected 145.23₈ = 101.296875₁₀, 423₁₀ = 647₈, 423.125₁₀ = 1A7.2₁₆, 675.24₈ = 1BD.5₁₆, complement of +55 = 11001001 (8-bit), BCD 13+26=39, ASCII Delta, and expected costs 50/47/46 lac. The printed binary subtraction is corrected to 11110.111₂.

1,500 conversion roundtrips cover integer values 0–499 in binary, octal and hexadecimal. Tests include zero, negative values, invalid digits and bases, safe precision limits, complement overflow and signed-width boundaries, BCD carry correction, invalid probabilities, invalid ASCII/parity inputs, and corrupted storage. All source K-map examples check all specified truth-table rows. Don’t-cares, constants, empty target sets, malformed expressions and duplicate/out-of-range indices are covered.

## Browser and responsive verification

`npm run test:e2e`: **12 Chromium workflows passed** on the final locally built site:

1. Brief/Guided/Full modes; guided restart; navigation; bookmarks, notes and completion after reload.
2. English and Bangla search, highlighted matches and direct source-page navigation.
3. Calculator recalculation, invalid-input feedback, K-map highlights and all-step display.
4. MCQ feedback, retry and empty topic filters.
5. Timed mock navigation, review flags, submission scoring and incorrect-question retry.
6. Revision flip/learn status, dark mode, original PDF and page-image requests.
7–10. No horizontal document overflow at 320, 390, 768 and 1440 px, across all original main sections.
11. Simulated timer expiry and automatic submission.
12. Backup download, invalid-import feedback and valid progress import.

Additional manual browser check: original-bank question count/search; desktop and mobile screenshots. Source reference HTML/CSS/JS were downloaded and inspected. A browser navigation to the external design reference encountered the environment's certificate-trust error; its source remained accessible through curl.

Tests use Chromium on Linux; Firefox, Safari, iOS hardware and screen-reader testing were not performed. Bangla text was visually checked in screenshots. Images use original English source. Browser actions show no page errors in the exercised study flow. Font size and dark styling are present; this is not a formal WCAG audit.

## Production verification

Deployment status and access checks will be recorded in `DEPLOYMENT-REPORT.md`. A READY deployment is distinct from publicly accessible hosting. The new project's default Vercel Authentication must not be described as removed unless explicitly approved and verified.

## Remaining limits

- Condensed page-level bilingual teaching does not yet fully satisfy the prompt's depth for every subsection and source exercise; all original content remains available.
- Not every original written question has a verified corrected answer or a dedicated interactive numerical walkthrough. Original bank extraction can damage overbars, which is disclosed at point of use.
- Calculator “10 steps” provide a reusable framework; explanatory depth varies by problem type. The math engines are bounded to safe numerical input sizes and 2–4-variable Boolean maps.
- Mock setup filters chapters, not individual topics; no official test pattern is claimed.
- Active mock tests do not survive reload; result history does. Notes/progress are local only.
- Revision is manual; no spaced-repetition scheduler.
- Tutorials are labeled YouTube searches; no direct videos independently verified.
- No per-formula standalone index with exhaustive original formula transcription; source images preserve them.
- Google Fonts require network; system fallback is provided.
