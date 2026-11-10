import json,re,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
import subprocess
subprocess.run(['pdftotext','-layout',str(ROOT/'public/book.pdf'),str(ROOT/'scripts/extracted.txt')],check=True)
pages=(ROOT/'scripts/extracted.txt').read_text().split('\f')[:55]
rows=(ROOT/'scripts/lessons.txt').read_text().splitlines()
# The pipe in the teaching text is a literal shell symbol, not a field delimiter.
rows[13]=rows[13].replace('Pipe চিহ্ন | এই','Pipe চিহ্ন (vertical bar) এই')
assert len(rows)==55
chapters=[['শুরু করুন · Start here',1,3],['Part 0 · Final revision',4,9],['Part 1 · Basic Linux',10,16],['Part 2 · Numbers & Boolean',17,22],['Part 3 · K-map tutorial',23,29],['Part 4 · Gates & circuits',30,35],['Part 5 · Processor & assembly',36,42],['Part 6 · Software & SDLC',43,51],['Part 7 · Original question bank',52,55]]
lessons=[]
for i,row in enumerate(rows):
 title,bn,intro,points,memory=[s.strip() for s in row.split('|')]
 text=pages[i].strip(); lines=text.splitlines(); printed=None
 for line in reversed(lines):
  if re.fullmatch(r'\s*\d+\s*',line):printed=int(line.strip());break
 if i in [0,2]:printed=None
 topics=[]
 for line in lines:
  t=line.strip()
  if re.match(r'^\d\.\d\s',t) or re.match(r'^(Worked example|Example \d|Rule \d|Q\d\.)',t): topics.append(t)
 lessons.append(dict(id=i+1,title=title,bn=bn,intro=intro,points=points.split(';'),memory=memory,text=text,printed=printed,chapter=next(j for j,c in enumerate(chapters) if c[1]<=i+1<=c[2]),sections=topics))
corrections=[
[2,'Contents lists Parts 0–6.','The body actually has Parts 0–7, with Digital Electronics II as Part 4. Navigation follows the body.'],
[4,'The 4-page final revision sheet','The revision section occupies PDF pages 4–9 (six pages), including a spillover and checklist.'],
[5,'Unicode — 16 bits','Unicode is a character standard, not a fixed 16-bit encoding. UTF-8, UTF-16 and UTF-32 encode it differently.'],
[12,'GPT: 128 partitions; MBR: 2 TB','128 is a common Windows default, not a universal GPT maximum. The usual MBR 2 TiB limit assumes 512-byte logical sectors. LVM/RAID are not a mandatory linear stack.'],
[17,'(145.23)8 = 64 + 32 + 5 + 0.25 + 0.05 = 101.3','3×8⁻²=3/64=0.046875, so the exact value is 101.296875. 101.3 is only a rounded value.'],
[19,'2’s complement of −108; no final carry means negative','The shown 10010100 is the 8-bit representation of −108, obtained by negating +108. Negating the encoded −108 gives +108. Signed subtraction requires overflow checks; carry-out alone is insufficient.'],
[20,'Unicode uses 16 bits; Excess-3 of 1010','Unicode is not fixed-width. The string 1010 is ambiguous: binary 1010 means decimal 10; decimal digits 1010 produce four Excess-3 groups. The calculator requires decimal digits explicitly.'],
[21,'10110 has two 1s and is even; ASCII Delta begins 68','10110 contains THREE 1s: even parity fails. ASCII D is hex 44 (decimal 68), not hex 68. Parity detects any odd number of bit errors, but misses even numbers.'],
[22,'AB′+AC+BC is already minimal','AC is the consensus term of AB′ and BC: AB′+AC+BC = AB′+BC. This is checked over all 8 input combinations.'],
[26,'Worked example 1 grouping prose merges m6,m14 into BD','BD′ is supported by the four-cell group {4,6,12,14}; BC′ by {4,5,12,13}; A′C′D by {1,5}. The printed final answer is consistent, but parts of the grouping prose are not.'],
[28,'A>B is true for these ten; m4,m12 can enlarge with m13 to A0B1′','Only SIX of the 16 combinations have A>B. The listed minterms are correct. The proposed enlargement is invalid: it would include m5 (01>01), which is false. Retain A0B1′B0′.'],
[38,'8086 first 16-bit processor','8086 was Intel’s first 16-bit x86 processor; 16-bit processors existed before it. 8085 clock ratings vary by model.'],
[41,'Macro under 10 instructions; timer 1/12, counter 1/24','Instruction count is a heuristic, not a rule. The timing ratios apply to a classic 12-clock 8051, not every processor or microcontroller.'],
[46,'Agile iteration 1–3 weeks; Agile does not recommend prototypes','Iteration length varies. Scrum allows sprints of one month or less. Agile can use prototypes and does not prohibit them.'],
[49,'White box slowest, black box fastest; white box developer only','Test speed and tester role are not fixed by box type. Both developers and test engineers can use these techniques.'],
[50,'Verification: Are we developing the right product? Validation: Is the developed product right?','Standard mnemonic: verification = building the product right (specification); validation = building the right product (user need). The source table reverses the slogans.'],
[19,'(110101.101)₂ − (010110.110)₂ = (011111.001)₂','53.625 − 22.75 = 30.875 = (11110.111)₂. The printed subtraction result is incorrect.'],
[53,'Parity detects single-bit errors only','Parity detects all odd-count bit errors, including a single-bit error, but not all multi-bit errors.']]
coverage=[]
for p in lessons:
 coverage.append(dict(pdf_page=p['id'],printed_page=p['printed'],chapter=chapters[p['chapter']][0],topic=p['title'],subsections=p['sections'],source=f"page-images/page-{p['id']:02}.jpg",explanation='Bilingual page lesson; brief/guided/full available',formula_status='Original image preserved; extracted overbars not reliable; use verified calculators',question_status='Original source preserved; MCQ adaptations explicitly labeled',verification='Contact-sheet visual audit; NOT line-by-line certification',issues=[c[1:] for c in corrections if c[0]==p['id']]))
for name,data in [('pages',lessons),('chapters',chapters),('corrections',corrections),('coverage',coverage)]:
 (ROOT/f'public/data/{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
# Authored lessons remain in scripts/lessons.txt; generated output is public/data.
print('55 pages mapped;',sum(len(x['sections']) for x in lessons),'source headings; corrections',len(corrections))
