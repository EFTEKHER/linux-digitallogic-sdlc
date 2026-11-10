import {readFile,mkdir,access,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createCanvas} from '@napi-rs/canvas';
import {getDocument} from 'pdfjs-dist/legacy/build/pdf.mjs';
const root=resolve(import.meta.dirname,'..');
const destination=process.argv[2]?resolve(process.argv[2]):resolve(root,'public/page-images');
await mkdir(destination,{recursive:true});
const doc=await getDocument({data:new Uint8Array(await readFile(resolve(root,'public/book.pdf'))),useSystemFonts:true}).promise;
for(let n=1;n<=doc.numPages;n++){
 const target=resolve(destination,`page-${String(n).padStart(2,'0')}.jpg`);
 try{await access(target);continue;}catch{}
 const page=await doc.getPage(n),raw=page.getViewport({scale:1}),viewport=page.getViewport({scale:1250/Math.max(raw.width,raw.height)});
 const canvas=createCanvas(Math.ceil(viewport.width),Math.ceil(viewport.height));
 await page.render({canvas,canvasContext:canvas.getContext('2d'),viewport}).promise;
 await writeFile(target,canvas.encodeSync('jpeg',82));page.cleanup();
}
await doc.destroy();console.log(`Original page images ready: ${doc.numPages} pages in ${destination}`);
