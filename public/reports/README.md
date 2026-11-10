# IT Path — বাংলা Exam Academy

A responsive, browser-based study academy for the supplied **Crack the IT Written** PDF. It preserves all 55 PDF pages and maps each to newly authored Bangla-English study notes. Source images retain the original diagrams, complement bars, tables and question wording.

## Install, run, build and test

Requires Node 20.19+ / 22.12+ (Node 24 used in this session).

```sh
npm ci
npm run prepare:pages  # regenerate page JPEGs from the included source PDF
npm run dev
npm test
npm run build
npm run preview
npm run test:e2e
```

`playwright.config.js` uses `/usr/bin/chromium` in this environment. On another computer, run `npx playwright install chromium` and remove that executablePath override, or replace it with your browser path. Production tests: `BASE_URL=https://your-project.vercel.app npm run test:e2e`.

The GitHub source archive includes the original PDF and all 55 page images. If derived images are absent, `npm run build` (or `npm run prepare:pages`) regenerates them using PDF.js and @napi-rs/canvas. Already present images are preserved.

Vite and standard JavaScript modules were chosen instead of Next/React: this academy has no server-dependent features, accounts or secrets, and all learning data/calculations run locally. Static output is inexpensive to deploy and the source content remains independent of the UI.

## Interactive visual learning

The K-map studio (`/#view=kmap`) walks through the problem, Gray ordering, filling the grid, each colored group, per-variable KEEP/DROP decisions, Boolean cancellation, expression construction, and full truth-table verification. Learners can select their own groups and receive feedback on invalid sizes, forbidden cells, incomplete cubes, or all-don’t-care selections. Source examples and custom SOP/POS inputs are supported.

Page lessons also include live binary-weight, Linux-layer, logic-gate, processor-memory and SDLC widgets.

Source repository: https://github.com/EFTEKHER/linux-digitallogic-sdlc

## Content and architecture

- `public/book.pdf`: unchanged uploaded PDF.
- `public/page-images/page-01.jpg` … `page-55.jpg`: original rendered pages.
- `public/data/pages.json`: page IDs, separate printed-page references, source headings/text, bilingual notes and keywords.
- `public/data/chapters.json`: actual body chapter mapping, not the inconsistent front contents numbering.
- `public/data/corrections.json`: explicitly separated original statements and justified corrections/qualifications.
- `public/data/coverage.json`: one record per PDF page, including verification limits.
- `public/data/original-bank.json`: 97 column-extracted original question/answer rows; mathematical notation needs image comparison.
- `src/math.js`: pure calculation models and exact Boolean minimization; independent of the interface.
- `src/examples.js`: calculator specifications, defaults and source-linked problem inventory.
- `src/questions.js`: newly authored MCQs, explicitly labeled AI generated.
- `src/storage.js`: validated versioned local browser state, import/export safeguards.
- `src/app.js`: navigation and learning workflows.
- `src/style.css`: responsive design, typography, theme and accessibility.
- `tests/math.test.js`: known answers, edge cases and storage validation.
- `tests/e2e/academy.spec.js`: learning workflows and responsive browser checks.

## Updating lessons, formulas, questions and calculators

Edit page lessons in `public/data/pages.json`, keeping stable IDs 1–55. Update `chapters.json` if adding chapters; adjust the explicit page limits in UI/storage if the source page count changes. Prefer a content migration rather than reusing existing IDs for unrelated content.

For a reproducible source refresh, install Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`) and Python PyMuPDF. `scripts/lessons.txt` holds authored page notes. `python scripts/content.py` regenerates page data and the coverage report. `python scripts/extract-bank.py` rebuilds source bank rows using audited row positions; those coordinates must be re-audited if the PDF changes. PDF images can be rendered with:

```sh
pdftoppm -scale-to 1250 -jpeg -jpegopt quality=82 public/book.pdf public/page-images/page
```

New MCQs go in `src/questions.js`; four distinct options, a single correct index, full rationale, source-topic page and an honest origin label are required. New examples go in `src/examples.js`. Add a pure calculator function to `src/math.js`, a lab spec in `src/examples.js`, dispatch in `app.js`, and known-answer/boundary tests. Test equations against source images, not plain text that may have lost overbars.

Use KaTeX for equations (`String.raw` or escaped backslashes in JavaScript). Keep raw input validation in the mathematical model. Maximum supported K-map size is four variables; the exact cover solver enumerates valid cubes and checks all specified truth-table rows.

## Browser study data

Storage key: `it-path-v1`. JSON schema version: `1`. Stable page/card/question IDs preserve compatibility. Notes, bookmarks, learned/difficult status, MCQ answers and mock-test result history are local only. Dashboard exports JSON backups and validates imports. Backups merge progress; imports do not reset settings. Never change storage schema without a migration. An active mock test persists across section changes but not page reloads. Clearing browser data removes local progress.

## Vercel deployment

Build with `npm run build`, then deploy the `dist/` static output. A **new** project `it-path-bangla-written-academy` was created in the connected `efte` team; existing projects were not modified. The native connected Vercel tools can upload file digests and create a production deployment from those static files. Alternatively link this source to a new Vercel project with build command `npm run build` and output directory `dist`. Do not deploy it over another academy.

The owner explicitly approved public access on 10 November 2026. Vercel confirmed that Authentication is disabled on this new project. Deployment and live HTTP checks are documented separately.

## Scope and verification limits

All original pages, source order and page-level lessons are present. This is **not certified 100% topic-by-topic instructional coverage**. Full mode uses an interactive reading deck with focus checklists, clickable terms, Bangla concept coaching, command missions, table exploration and recall checks; original PDF/page images remain separately accessible. Some topics need richer individual tutoring, additional diagrams and further worked variants. Original bank rows are extracted text, not fully certified transcriptions; complement bars can be damaged. The source audit explicitly flags these limits. Source past-paper provenance is reported as the book's claim, not independently authenticated.

Every implemented calculator is editable and has input validation. Binary arithmetic shows column carry/borrow; fixed-width signed representation is separate. Repeating fractions are truncated and labeled. K-map/Boolean outputs are verified against specified input rows, with don’t-care rows excluded from equivalence requirements. Multiple minimum solutions may be valid. Generated MCQs are not an official examination pattern.

Tutorials are explicitly labeled YouTube searches; direct video links have not been verified. Google Fonts are external; system fallbacks remain usable if unavailable. No account, cloud sync, AI chat backend or analytics is implemented.

See `TESTING-REPORT.md` and `public/data/coverage.json` for delivered evidence and limits.

The repository is linked to Vercel project linux-digitallogic-sdlc (production branch main): https://linux-digitallogic-sdlc.vercel.app. Pushes to main trigger Git-based builds. The earlier standalone academy URL is maintained as a separate deployment.

Full-reader card progress uses it-path-source-reader-v1 and is included in study backup export/import as sourceCards.
