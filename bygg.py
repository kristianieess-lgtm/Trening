#!/usr/bin/env python3
"""Bygger site/ (publiserbar mobilversjon) fra dagbok.html.
Kjør:  python3 bygg.py   – deretter publiseres mappen site/ (Netlify)."""
import hashlib, pathlib, shutil
from PIL import Image, ImageDraw
root = pathlib.Path(__file__).parent
site = root / 'site'; site.mkdir(exist_ok=True)
html = (root / 'dagbok.html').read_text(encoding='utf-8')
(site / 'index.html').write_text(html, encoding='utf-8')
ver = hashlib.sha1(html.encode()).hexdigest()[:10]

def icon(size, path, pad=0.0):
    img = Image.new('RGB', (size, size), '#2f6f4f')
    d = ImageDraw.Draw(img); u = size / 100
    # manual (hantel)
    d.rounded_rectangle([22*u, 40*u, 30*u, 60*u], 2*u, fill='white')
    d.rounded_rectangle([70*u, 40*u, 78*u, 60*u], 2*u, fill='white')
    d.rounded_rectangle([14*u, 44*u, 22*u, 56*u], 2*u, fill='white')
    d.rounded_rectangle([78*u, 44*u, 86*u, 56*u], 2*u, fill='white')
    d.rounded_rectangle([30*u, 47*u, 70*u, 53*u], 1*u, fill='white')
    img.save(path)
icon(192, site / 'icon-192.png'); icon(512, site / 'icon-512.png'); icon(180, site / 'apple-touch-icon.png')

(site / 'manifest.webmanifest').write_text('''{
  "name": "Treningsdagbok",
  "short_name": "Trening",
  "description": "Treningsdagbok og kostholdsveileder: halvmaraton Madrid 2027",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "background_color": "#f6f4ef",
  "theme_color": "#2f6f4f",
  "lang": "nb",
  "icons": [
    {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}
  ]
}
''', encoding='utf-8')

(site / 'sw.js').write_text('''/* Offline-støtte: appen lastes fra cache, oppdateres i bakgrunnen. */
const V='trening-%s';
const FILES=['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png','apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET')return;
  e.respondWith(caches.open(V).then(async c=>{
    const hit=await c.match(e.request,{ignoreSearch:true});
    const net=fetch(e.request).then(r=>{if(r&&r.ok)c.put(e.request,r.clone());return r}).catch(()=>null);
    return hit||(await net)||c.match('index.html');
  }));
});
''' % ver, encoding='utf-8')

(site / '_headers').write_text('''/*
  X-Robots-Tag: noindex, nofollow
/sw.js
  Cache-Control: no-cache
/index.html
  Cache-Control: no-cache
''', encoding='utf-8')
(site / 'robots.txt').write_text('User-agent: *\nDisallow: /\n', encoding='utf-8')
print('site/ bygget, versjon', ver)
