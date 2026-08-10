# Eksport

Cztery drogi wyjścia. Wybór zależy od tego, **co klient dostanie do ręki**, a nie od tego,
która jest najszybsza.

| Chcę | Użyj | Uwaga |
|---|---|---|
| PDF do wysłania | przycisk **PDF** w decku | jeden slajd = jedna strona, tekst zostaje tekstem |
| PPTX „na już”, mam internet | przycisk **PPTX** w decku | slajdy jako obrazy, jakość html2canvas |
| PPTX i PDF w dobrej jakości | `scripts/export-deck.py` | Chromium, ×2, offline po instalacji |
| PNG wykresu / infografiki / posta | `scripts/render.py` | nominalny rozmiar płótna × skala |
| Zrzuty kontrolne do QA | `scripts/shot.py` | to nie jest eksport, tylko podgląd |

**Żaden z tych eksportów nie daje edytowalnego PowerPointa.** Slajdy wychodzą jako obrazy.
Gdy klient ma poprawiać tekst u siebie, odbuduj deck skilem **`pptx`** — to inne narzędzie
i inna robota, nie da się jej wycisnąć z tego szablonu.

---

## Klasa `is-clean`

Wspólny mechanizm wszystkich ścieżek. Dodana na `<body>` chowa całe sterowanie —
topbar, zakładkę i panel menu, przyciemnienie tła pod menu, strzałki i pasek postępu:

```css
body.is-clean .topbar, body.is-clean .drawer-tab, body.is-clean .vprog,
body.is-clean .arrows, body.is-clean .drawer, body.is-clean .drawer-scrim{display:none!important;}
```

Dlatego zrzut wygląda jak slajd, a nie jak zrzut ekranu z przeglądarki. Wszystkie trzy
skrypty i oba przyciski nakładają ją same — **nie zostawiaj jej wpisanej w HTML**,
bo wtedy deck traci nawigację.

---

## Przycisk PDF (druk przeglądarki)

```js
body.classList.add('is-clean');
/* --fit z powrotem na 1 i pełna szerokość: druk ma stały kadr, autoskalowanie
   ekranowe zrobiłoby na stronie A4 slajd zmniejszony do 84% */
setTimeout(()=>{ window.print(); … }, 120);
```

Reguły druku (`@media print` w sekcji 14 szablonu):
- `@page{size:1600px 900px;margin:0}` — strona ma proporcję slajdu, bez marginesu;
- `.slide{page-break-after:always;height:900px;width:1600px}` — jeden slajd na stronę;
- `[data-step]` dostaje `opacity:1` — kroki animacji nie mogą zostać niewidoczne na papierze;
- `.detail{display:block!important}` — **tryb szczegółów drukuje się zawsze**, niezależnie
  od tego, czy był włączony na ekranie. PDF jest wersją do czytania, nie do prezentowania;
- `print-color-adjust:exact` — inaczej Chrome wypłukuje ciemne tła.

W oknie druku wybierz **Zapisz jako PDF**, marginesy **brak**, grafika tła **włączona**.
Tekst zostaje tekstem — ten PDF da się przeszukać i skopiować, w odróżnieniu od
`export-deck.py --only pdf`, który składa obrazy.

## Przycisk PPTX (html2canvas + pptxgenjs)

Dociąga oba pakiety z CDN przy pierwszym kliknięciu, więc **wymaga internetu**.
Robi zrzut każdego slajdu (`scale:2`) i wkleja go na płótno 13,333 × 7,5 cala.

Ograniczenia html2canvas, które zobaczysz na oczy: gradienty stożkowe (pierścienie
i donuty), `clip-path` (heksagony), maski i filtry potrafią wyjść inaczej niż w przeglądarce.
Gdy eksport padnie, alert kieruje wprost do `scripts/export-deck.py` — i to jest właściwa
odpowiedź także wtedy, gdy nie padnie, ale wygląda gorzej.

---

## `scripts/export-deck.py` — droga zalecana

```
pip install playwright python-pptx pillow
playwright install chromium
```

```
cd assets
python ../scripts/export-deck.py                                   # PPTX + PDF, ×2
python ../scripts/export-deck.py --file oferta-klient.html
python ../scripts/export-deck.py --only pptx --name Oferta-Kingfisher
python ../scripts/export-deck.py --slides 1 4 7 --scale 3          # wybrane slajdy, do druku
python ../scripts/export-deck.py --only png --out ./_png
```

| Flaga | Domyślnie | Znaczenie |
|---|---|---|
| `--file` | pierwszy `*deck*.html` | plik wejściowy |
| `--out` | `scripts/_export` | katalog wynikowy |
| `--name` | `CloudBots-prezentacja` | nazwa PPTX i PDF |
| `--scale` | `2` | mnożnik rozdzielczości zrzutu |
| `--width` / `--height` | `1920` / `1080` | okno przeglądarki |
| `--slides` | wszystkie | numery od 1 |
| `--only` | PPTX **i** PDF | `pptx` \| `pdf` \| `png` |

Co robi krok po kroku: podnosi lokalny serwer na porcie 8813 (fonty Google nie ładują się
z `file://`), czeka na `networkidle` i `document.fonts.ready`, nakłada `is-clean`, wywołuje
`resize` żeby autoskalowanie przeliczyło się bez topbaru, przewija do każdego slajdu,
czeka 600 ms na animację wejścia i zrzuca element `.slide`. PPTX składa `python-pptx`
na układzie bez placeholderów, PDF — Pillow przy 150 dpi.

Renderuje prawdziwy Chromium, więc **gradienty, `clip-path` i maski wychodzą wiernie**.
To jedyna różnica, która naprawdę się liczy przy decku z heksagonami i pierścieniami.

Uruchamiaj **z katalogu, w którym leży deck** — serwer podaje katalog roboczy.

---

## `scripts/render.py` — płótna do PNG

Dotyczy wykresów, infografik i grafik na LinkedIn. Zrzuca **każdy element z `data-render`**
i nazywa plik wartością tego atrybutu.

```
cd assets
python ../scripts/render.py --file cloudbots-infographics.html          # wszystko, ×2
python ../scripts/render.py li-teza li-cytat --file cloudbots-linkedin.html
python ../scripts/render.py "li-kar-*" --file cloudbots-linkedin.html --pdf karuzela.pdf
python ../scripts/render.py "ig-*" --scale 3 --out ./do-druku
```

- Wzorce z `*` **w cudzysłowie** — inaczej rozwinie je powłoka.
- `--pdf` składa wybrane płótna w jeden plik w kolejności wystąpienia w HTML.
  Tak przygotowuje się karuzelę na LinkedIna.
- Skrypt zdejmuje `transform:scale` podglądu, więc PNG wychodzi w **nominalnym rozmiarze
  płótna** × `--scale`: `.f-45` przy ×2 to 2160 × 2700.
- Gdy robisz wariant płótna, **zmień `data-render`** — inaczej nadpiszesz oryginał.

## `scripts/shot.py` — zrzuty kontrolne

Nie eksport, tylko oczy. Po każdej zmianie treści slajdu.

```
cd assets
python ../scripts/shot.py                       # wszystkie slajdy → scripts/_shots/
python ../scripts/shot.py 1 4 7
python ../scripts/shot.py --file oferta.html --dark
```

`--dark` wymusza ciemny motyw systemowy — sprawdzasz, czy `prefers-color-scheme`
nie wywraca układu. Nie nakłada `is-clean`: chcesz zobaczyć także topbar i zakładkę menu,
bo one też mogą wejść w treść.

---

## Kontrola przed wysłaniem

1. **Obejrzyj zrzuty w 100%.** Podgląd w oknie jest zmniejszony i wybacza za ciasny tekst,
   przycięte heksagony i zderzenia dekoracji z treścią.
2. **Sprawdź slajd najgęstszy**, nie pierwszy. Jeśli autoskalowanie zeszło poniżej ~0,8,
   treści jest za dużo — tnij treść, nie stopień pisma.
3. **Otwórz PPTX w PowerPoincie**, zanim wyślesz. Sprawdzasz proporcję i to, czy pierwszy
   slajd nie wszedł w obrys.
4. **PDF przewiń do końca** — brakująca strona zwykle znaczy slajd bez `.slide` albo
   `--slides` z literówką.
5. Zanim oddasz katalog, **usuń `_shots/`, `_render/`, `_export/`** — to śmieci robocze.
