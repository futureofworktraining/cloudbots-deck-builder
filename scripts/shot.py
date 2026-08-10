#!/usr/bin/env python
"""
shot.py — zrzuty kontrolne slajdów decku.

Podaje deck przez lokalny serwer (fonty Google i moduły CDN nie ładują się
z file://), przewija do każdego slajdu i zapisuje PNG do _shots/.

    python shot.py                      # wszystkie slajdy pliku *deck*.html
    python shot.py 1 4 7                # tylko wskazane slajdy
    python shot.py --file oferta.html   # inny plik wejściowy
    python shot.py --dark               # wymuś ciemny motyw systemowy

Wymaga: pip install playwright && playwright install chromium
"""
import argparse
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

PORT = 8811
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "_shots")


def serve(directory):
    handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(*a, directory=directory, **kw)
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    httpd.allow_reuse_address = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slides", nargs="*", type=int, help="numery slajdów od 1")
    ap.add_argument("--file", default=None, help="plik HTML decku")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--scale", type=int, default=1)
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--dark", action="store_true", help="wymuś ciemny motyw systemowy")
    args = ap.parse_args()

    cwd = os.getcwd()
    target = args.file
    if not target:
        found = sorted(glob.glob("*deck*.html")) or sorted(glob.glob("*.html"))
        if not found:
            sys.exit("Nie znalazłem pliku HTML w " + cwd)
        target = found[0]
    print(f"deck: {target}")

    os.makedirs(args.out, exist_ok=True)
    httpd = serve(cwd)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(
                viewport={"width": args.width, "height": args.height},
                device_scale_factor=args.scale,
                color_scheme="dark" if args.dark else "light",
            )
            page.goto(f"http://127.0.0.1:{PORT}/{target}")
            page.wait_for_timeout(2500)  # fonty + pierwsze dopasowanie

            count = page.locator(".slide").count()
            wanted = args.slides or range(1, count + 1)
            print(f"slajdów: {count}")

            for n in wanted:
                if not 1 <= n <= count:
                    print(f"  pomijam {n} — poza zakresem")
                    continue
                page.evaluate(
                    "i => document.querySelectorAll('.slide')[i]"
                    ".scrollIntoView({behavior:'instant',block:'start'})",
                    n - 1,
                )
                page.wait_for_timeout(700)
                path = os.path.join(args.out, f"slide-{n:02d}.png")
                page.locator(".slide").nth(n - 1).screenshot(path=path)
                print("  →", path)

            browser.close()
    finally:
        httpd.shutdown()


if __name__ == "__main__":
    main()
