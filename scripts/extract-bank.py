import fitz,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]; doc=fitz.open(root/'public/book.pdf')
starts={52:[283.8,303.3,322.8,332.6,346.4,370,387.2,404.5,421.8,438.7,456,473.6,490.8,507.8,531.6,548.9,572.5,596,619.3],53:[74.9,106.4,145.4,252.9,262.8,272.4,282.2,291.9,301.7,311.4,321.2,330.9,340.7,360.1,379.7,389.5,409,428.5,457.7,477.6,495.2,504.8,526.3,536.1],54:[70.8,100.1,109.8,119.6,129.3,139.1,151,160.4,180.6,200.2,219.7,239.2,268.5,278.2,287.9,297.7,317.2,346.4,375.7,395.2,414.7,434.2,463.4,473.2,590.6,610.1,629.6],55:[70.8,90.3,99.8,109.5,119.3,129.3,158.6,178.1,207.3,226.8,246.3,275.6,304.8,324.3,334,343.8,363.3,373,382.8,392.5,421.8,451,470.5,490,499.8,519.3,538.8]}
rows=[]
for page,ys in starts.items():
 p=doc[page-1]
 for j,y in enumerate(ys):
  end=ys[j+1]-1.4 if j+1<len(ys) else (583 if page==55 else 650)
  if page==53 and j==2:end=183
  if page==54 and j==23:end=512
  # Extract by span position; this avoids losing inline subscripts at crop boundaries.
  left=[];right=[]
  for b in p.get_text('dict')['blocks']:
   for l in b.get('lines',[]):
    for s in l['spans']:
     x,top,x2,bot=s['bbox']
     if y-2<=top<end and x>45 and x2<500:
      (left if x<260 else right).append((top,x,s['text']))
  def join(a):return ' '.join(t for _,_,t in sorted(a))
  rows.append(dict(id=len(rows),page=page,question=join(left),answer=join(right),source='PDF Original Question — extracted wording',verification='Column extraction; mathematical overbars may be lost. Compare original image before memorizing a formula.'))
(root/'public/data/original-bank.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print(len(rows),'original source rows extracted; image comparison required for mathematical notation')
