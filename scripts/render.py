#!/usr/bin/env python
"""
render.py — eksport płócien (wykresy, infografiki, grafiki na LinkedIn) do PNG.

Znajduje w pliku każdy element z atrybutem data-render i zapisuje go jako PNG
w nominalnym rozmiarze pomnożonym przez --scale (domyślnie 2×, bo LinkedIn
i tak przeskaluje grafikę w dół, a nie w górę).

    python render.py                                  # cały plik, wszystkie płótna
    python render.py --file cloudbots-linkedin.html
    python render.py li-teza li-cytat                 # wybrane nazwy
    python render.py "li-kar-*"                       # wzorzec (cudzysłów!)
    python render.py "li-kar-*" --pdf karuzela.pdf    # karuzela jako jeden PDF
    python render.py --scale 1 --out ./gotowe

Serwuje katalog roboczy przez HTTP, bo fonty Google nie ładują się z file://.
Wymaga: pip install playwright pillow && playwright install chromium
(pillow tylko dla --pdf).
"""
import argparse
import fnmatch
import glob
import http.server
import os
import socketserver
import sys
import threading

from playwright.sync_api import sync_playwright

# konsola Windows domyślnie cp1252 — polskie znaki i strzałki w logu ją wywracają
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PORT = 8812
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "_render")

# Zdejmuje skalowanie podglądu, żeby zrzut wyszedł w nominalnym rozmiarze płótna.
# Kontenery podglądu przycinają płótno (overflow:hidden) i układają je w rzędach —
# w trybie zrzutu rozkładamy je pionowo, inaczej sąsiad wchodzi w kadr.
UNSCALE = """() => {
  document.body.classList.add('raw');
  const holders = document.querySelectorAll('.holder');
  const page = document.querySelector('.page');
  // szerokość strony rozpinamy tylko tam, gdzie płótna mają stały rozmiar
  // (galeria wykresów jest płynna — rozepchnięcie zmieniłoby proporcje)
  if (page && holders.length) { page.style.maxWidth = 'none'; page.style.padding = '20px'; }
  document.querySelectorAll('.row').forEach(r => { r.style.display = 'block'; });
  holders.forEach(h => {
    h.style.height = 'auto';
    h.style.width = 'max-content';
    h.style.overflow = 'visible';
    h.style.marginBottom = '28px';
    if (h.firstElementChild) h.firstElementChild.style.transform = 'none';
  });
}"""


def serve(directory):
    handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(*a, directory=directory, **kw)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def pick_file(explicit):
    if explicit:
        return explicit
    for pattern in ("*linkedin*.html", "*infograf*.html", "*chart*.html", "*wykres*.html", "*.html"):
        found = sorted(glob.glob(pattern))
        if found:
            return found[0]
    sys.exit("Nie znalazłem pliku HTML w " + os.getcwd())


def to_pdf(paths, target):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("--pdf wymaga Pillow:  pip install pillow")
    if not paths:
        sys.exit("--pdf: brak zrzutów do złożenia")
    pages = [Image.open(p).convert("RGB") for p in paths]
    pages[0].save(target, save_all=True, append_images=pages[1:], resolution=150.0)
    print("  → " + target + f"  ({len(pages)} str.)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="*", help="nazwy data-render, dopuszczalne wzorce z *")
    ap.add_argument("--file", default=None, help="plik HTML z płótnami")
    ap.add_argument("--scale", type=int, default=2, help="mnożnik rozdzielczości (domyślnie 2)")
    ap.add_argument("--out", default=OUT, help="katalog wyjściowy")
    ap.add_argument("--pdf", default=None, help="złóż wybrane płótna w jeden PDF (kolejność jak w pliku)")
    args = ap.parse_args()

    target = pick_file(args.file)
    print(f"plik: {target}   skala: {args.scale}×")

    os.makedirs(args.out, exist_ok=True)
    httpd = serve(os.getcwd())
    written = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(
                viewport={"width": 1700, "height": 1200},
                device_scale_factor=args.scale,
            )
            page.goto(f"http://127.0.0.1:{PORT}/{target}")
            page.wait_for_load_state("networkidle")
            page.evaluate("() => document.fonts.ready")
            page.evaluate(UNSCALE)
            page.wait_for_timeout(900)  # fonty + przeliczenie układu po zdjęciu skalowania

            found = page.eval_on_selector_all(
                "[data-render]", "els => els.map(e => e.dataset.render)"
            )
            if not found:
                sys.exit("W pliku nie ma elementów z data-render")

            if args.names:
                wanted = [n for n in found if any(fnmatch.fnmatch(n, pat) for pat in args.names)]
                missing = [pat for pat in args.names
                           if not any(fnmatch.fnmatch(n, pat) for n in found)]
                for pat in missing:
                    print(f"  pomijam „{pat}” — brak dopasowania")
            else:
                wanted = found

            print(f"płócien: {len(wanted)} z {len(found)}")

            for name in wanted:
                path = os.path.join(args.out, f"{name}.png")
                page.locator(f'[data-render="{name}"]').screenshot(path=path)
                box = page.locator(f'[data-render="{name}"]').bounding_box()
                dims = f"{int(box['width'] * args.scale)}×{int(box['height'] * args.scale)}" if box else "?"
                print(f"  → {path}   {dims}")
                written.append(path)

            browser.close()
    finally:
        httpd.shutdown()

    if args.pdf:
        to_pdf(written, args.pdf)


if __name__ == "__main__":
    main()
