---
name: cloudbots-deck-builder
description: >-
  Buduje materiały wizualne CloudBots w jednym systemie graficznym: (1) prezentacje
  jako jednoplikowy, interaktywny HTML deck — wysuwane menu z lewej krawędzi, nawigacja
  klawiaturą, tryb dokument/prezentacja, kroki odsłaniania, autoskalowanie, autoodtwarzanie,
  wersja PL/EN, eksport PDF i PPTX; (2) wykresy — trzynaście typów w kontenerze zapytań,
  działających na ciemnym i jasnym tle; (3) infografiki — siedem płócien w stałych kadrach
  (16:9, 1:1, 4:5, A4) eksportowanych do PNG; (4) grafiki na LinkedIn — posty 4:5 i 1:1,
  karuzele, grafika pod link, baner profilu. Użyj, gdy użytkownik chce zrobić prezentację,
  deck, ofertę, pitch, slajdy, wykres, infografikę, grafikę na posta albo karuzelę dla CloudBots,
  albo przerobić surową treść (notatki, dokument, stary HTML/PPTX) na te formaty.
---

# CloudBots Deck Builder

Cztery rodzaje materiałów, jeden język wizualny wywiedziony z oferty Kingfisher
i strony cloudbots.eu: ciemne i jasne kadry przeplatane slajd po slajdzie,
heksagon jako sygnatura marki, Space Grotesk w nagłówkach, ziarno na całości,
zero zaokrągleń. Wszystko bez zależności — pliki otwierają się z dysku.

| Element | Plik startowy | Wynik |
|---|---|---|
| **Prezentacja** | `assets/cloudbots-deck-template.html` | jeden plik `.html`, opcjonalnie PDF/PPTX |
| **Wykresy** | `assets/cloudbots-charts.html` | markup wklejany do decku lub PNG |
| **Infografiki** | `assets/cloudbots-infographics.html` | PNG w stałym kadrze |
| **LinkedIn** | `assets/cloudbots-linkedin.html` | PNG postów, karuzela jako PDF |

Wykresy, infografiki i grafiki na LinkedIn są **osobnymi elementami skilla** — można
po nie sięgnąć bez budowania prezentacji.

---

## Złota zasada: TREŚĆ PRZED FORMĄ

Nie zaczynaj od stylowania. Kolejność jest sztywna:

1. **Treść** → 2. **Struktura / narracja** → 3. **Forma** → 4. **QA** → 5. *(opcja)* eksport.

Gdy użytkownik wrzuca surowy materiał (notatki, dokument, stary HTML, PPTX),
najpierw wyciągnij i ustrukturyzuj treść, dopiero potem buduj kadry.
Do ekstrakcji z PPTX użyj skilla **pptx** (`python -m markitdown plik.pptx`).

---

## Workflow — prezentacja

### Krok 1 · Treść
Zbierz materiał. Ustal krótko, jeśli nieznane: **cel**, **odbiorca**, **kontekst**
(oferta, konferencja, raport wewnętrzny), **długość**, **język** (deck ma przełącznik PL/EN).

### Krok 2 · Struktura
Zaproponuj listę slajdów: tytuł + jednozdaniowy komunikat każdego. To jest jednocześnie
spis nawigacji w wysuwanym menu. Jeden komunikat = jeden slajd.

Podziel deck na **sekcje** (`data-group`) i **każdą otwórz przekładką** — ciemnym slajdem
`.sect` z numerem sekcji, tezą i jednym zdaniem kontekstu. Typowy łuk oferty:

```
okładka → spis treści
  ── 01 Kontekst ──   przekładka → problem → liczby
  ── 02 Moduły ──     przekładka → moduł → jak pracujemy
  ── 03 Warunki ──    przekładka → wycena → harmonogram
  ── 04 Dowody ──     przekładka → opinie → kontakt
```

Pierwsza grupa (okładka + spis treści) przekładki nie potrzebuje — deck sam się nią otwiera.
Numer na przekładce to numer SEKCJI, nie slajdu; numeracja slajdów generuje się sama,
więc dołożenie przekładki nigdy nie wymaga przenumerowania niczego.

**Przy prezentacji powyżej ~6 slajdów zatwierdź strukturę z użytkownikiem przed budową formy.**

### Krok 3 · Forma
- Skopiuj `assets/cloudbots-deck-template.html` — ma gotowy szkielet i czternaście
  wzorcowych slajdów do podmiany treści, w tym cztery przekładki sekcyjne.
- Każdy slajd to `<section class="slide slide--dark|slide--light" data-theme="dark|light"
  data-nav="Nazwa w menu" data-group="Grupa w menu">`. Menu buduje się samo z tych atrybutów.
- Wypełniaj komponentami z `references/components.md`. **Nie powtarzaj tego samego układu**
  slajd po slajdzie i przeplataj motywy — ciemny slajd po dwóch jasnych jest cezurą narracji.
- Slajdy z danymi: wykres z `references/charts.md`, dobrany do **typu liczby**
  (udział → pierścień/kołowy, zmiana → `.c-delta`, szereg czasowy → `.c-bars`/`.c-line`,
  wzorzec 2D → `.c-heat`, ranking → `.c-rank`). Wykres koduje realną wartość — nigdy ozdobnik.
- Ponumeruj bloki `data-step="0|1|2…"` — to jednostki odsłaniania w trybie prezentacji
  i kaskada wejścia w trybie dokumentu. Elementy z tym samym numerem wchodzą razem.
- Treść dodatkową (źródła, przypisy, szczegóły dla czytającego, nie dla sali) oznacz klasą
  `detail` — pokazuje ją przycisk „Szczegóły”.
- Wersja angielska: `data-en="…"` na elemencie z polskim tekstem. Skrypt zapamiętuje polski
  przy pierwszym przełączeniu, więc atrybut `data-pl` piszesz tylko wyjątkowo.
- Trzymaj tokeny z `references/design-system.md`. Kolor i typografia marki są nadrzędne
  nad kreatywnymi odstępstwami.

### Krok 4 · QA (obowiązkowo)
Otwórz deck w przeglądarce i sprawdź:
- menu wysuwa się uchwytem przy lewej krawędzi, pozycje prowadzą do właściwych slajdów, Esc zamyka;
- nawigacja: ←/→, ↑/↓, PageUp/Down, spacja, Home/End, kółko myszy (jeden gest = jeden slajd);
- **autoskalowanie** — „Dopasuj: Zmieść / Wypełnij / 1:1”. Jeśli slajd w trybie „Zmieść”
  schodzi mocno poniżej 1, jest przeładowany — podziel go, nie zmniejszaj czcionki;
- tryb prezentacji: kroki `data-step` odsłaniają się po kolei, nic nie zostaje niewidoczne;
- kontrast na obu motywach, brak placeholderów `[KLIENT]`, `[...]`, „Lorem”;
- przełącznik EN — czy każdy widoczny tekst ma `data-en`, czy nie zostały polskie wtrętki;
- wydruk / PDF daje czyste slajdy bez sterowania.

Do weryfikacji wizualnej użyj `scripts/shot.py` — zrzuca każdy slajd do `_shots/`.

### Krok 5 · Eksport (na życzenie)
Szczegóły w `references/export.md`. Skrótowo: przycisk **PDF** (druk przeglądarki),
przycisk **PPTX** (html2canvas + pptxgenjs z CDN, wymaga internetu),
`scripts/export-deck.py` (Playwright — lepsza jakość, bez internetu po instalacji).

---

## Workflow — wykresy, infografiki, LinkedIn

1. **Wybierz kadr.** Otwórz odpowiednią galerię w przeglądarce i wskaż użytkownikowi,
   który wzorzec pasuje do treści. Każdy ma pod spodem notkę „kiedy tego użyć”.
2. **Podmień treść**, nie geometrię. Reguły wymiany dla każdego płótna:
   `references/infographics.md`, `references/linkedin.md`.
3. **Wyrenderuj** przez `scripts/render.py`:
   ```
   python render.py --file cloudbots-linkedin.html          # wszystko z pliku
   python render.py li-teza li-cytat                        # wybrane płótna
   python render.py "li-kar-*" --pdf karuzela.pdf           # karuzela jako jeden PDF
   ```
   Każdy element z atrybutem `data-render="nazwa"` zapisuje się jako `nazwa.png`.
4. **Obejrzyj PNG-i.** Podgląd w galerii jest przeskalowany; dopiero zrzut pokazuje,
   co naprawdę zobaczy odbiorca.

---

## Pliki referencyjne (czytaj na żądanie)

| Plik | Kiedy czytać |
|---|---|
| `references/design-system.md` | Zawsze przy budowie formy — tokeny, typografia, motywy, heksagon, ziarno, skala danych, dostępność. |
| `references/components.md` | Przy wypełnianiu slajdów — katalog układów i komponentów z gotowym markupem. |
| `references/charts.md` | Slajd z liczbami — trzynaście typów wykresów, markup i zasada doboru. |
| `references/infographics.md` | Infografika — siedem płócien, co w każdym wolno wymienić. |
| `references/linkedin.md` | Post, karuzela, baner — formaty, progi czytelności, strefy bezpieczne. |
| `references/export.md` | PDF, PPTX, PNG, `shot.py`, `render.py`, `export-deck.py`. |

Galerie do oglądania (nie do czytania jako kod): `assets/cloudbots-charts.html`,
`assets/cloudbots-infographics.html`, `assets/cloudbots-linkedin.html`.

---

## Zasady twarde (czego NIE robić)

- **Nie zaczynaj od stylu.** Najpierw treść i struktura.
- **Nie powielaj jednego layoutu** ani jednego motywu przez cały deck.
- **Nie zaczynaj sekcji bez przekładki.** Grupa slajdów bez własnego separatora zlewa się
  z poprzednią i odbiorca traci orientację, w której części rozmowy jest.
- **Nie rysuj wykresu bez wartości.** Słupek „dla ozdoby” jest gorszy niż jego brak.
- **Nie koloruj wykresów inline** tam, gdzie istnieje klasa (`.hm-0`…`.hm-5`, `--dv-1`…`--dv-5`) —
  inline'owy kolor przestaje działać na drugim motywie.
- **Nie ruszaj geometrii płócien pojedynczo.** Wymiary heksagonalnego plastra, kadrów
  `.c-169`/`.f-45` i szerokości lejka są przeliczone jako zestaw.
- **Nie zostawiaj placeholderów.** `[KLIENT]`, `[MIESIĄC ROK]`, „Lorem”, „TODO” muszą zniknąć.
- **Nie deklaruj sukcesu bez QA** — co najmniej jeden cykl sprawdź-popraw, a przy grafikach
  obejrzenie wyrenderowanego PNG-a.
