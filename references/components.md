# Komponenty decku CloudBots

Katalog do kopiowania. Wszystko pochodzi z `assets/cloudbots-deck-template.html` —
jeśli coś jest niejasne, otwórz szablon i zobacz komponent w kontekście slajdu.

---

## 0. Szkielet slajdu

```html
<section class="slide slide--dark" data-theme="dark"
         data-nav="Problem" data-group="Kontekst">

  <div class="grid-deco"></div>              <!-- opcjonalnie: siatka w tle -->
  <div class="hex-deco">                     <!-- opcjonalnie: heksagony -->
    <span style="width:300px;height:346px;top:14%;right:9%;"></span>
  </div>

  <div class="chrome-top">
    <span class="chrome-tag"><span class="chrome-tag-dot"></span>03</span>
    <span class="chrome-progress"></span>
  </div>

  <div class="stage">
    <div class="stack">
      <!-- treść slajdu -->
    </div>
  </div>

  <div class="chrome-bottom">
    <span class="chrome-tag" data-manual="1">CloudBots · cloudbots.eu</span><span></span>
  </div>
</section>
```

Co robi który atrybut:

| Atrybut | Działanie |
|---|---|
| `data-theme="dark\|light"` | ustawia motyw ramy (menu, topbar, strzałki) po wejściu na slajd |
| `data-nav="…"` | nazwa pozycji w wysuwanym menu |
| `data-group="…"` | nagłówek grupy w menu; kolejne slajdy z tą samą wartością trafiają pod jeden nagłówek |
| `data-manual="1"` | „nie podmieniaj mi tego tekstu” — skrypt numerujący slajdy omija ten element |
| `data-step="0\|1\|2…"` | jednostka odsłaniania; elementy z tym samym numerem wchodzą razem |
| `data-en="…"` | wersja angielska treści elementu (HTML, nie tylko tekst) |
| `data-count-to="24"` | liczba odlicza się od zera po wejściu na slajd; `data-count-suffix="%"` dokleja jednostkę |
| `data-go="5"` | przycisk skacze do slajdu o tym indeksie |
| `data-video="https://…"` | otwiera lightbox z iframe |
| `class="detail"` | element widoczny dopiero po włączeniu trybu „Szczegóły” |

**`.stage` ma dokładnie jedno dziecko.** To ono jest skalowane przez autofit —
dwa dzieci rozjadą się przy skalowaniu.

---

## 1. Typografia slajdu

```html
<p class="eyebrow">Jak pracujemy</p>              <!-- z kreską przed tekstem -->
<p class="eyebrow eyebrow--plain">Moduł 01</p>    <!-- bez kreski -->

<h1 class="h-display">Agenci AI, którzy <em>naprawdę działają</em>.</h1>
<h2 class="h-title">Pilotaże przechodzą. Produkcja nie.</h2>
<h3 class="h-title h-title--s">Wersja mniejsza, gdy nagłówek jest długi</h3>

<p class="h-sub">Podtytuł pod nagłówkiem — lekki, do 76 znaków w wierszu.</p>
<p class="lead">Akapit prowadzący, jaśniejszy od tekstu wtórnego.</p>
<p class="note">Przypis, źródło, zastrzeżenie.</p>
```

Nagłówek z metadanymi po prawej:

```html
<div class="head-row">
  <div>
    <p class="eyebrow">W liczbach</p>
    <h2 class="h-title" style="margin-top:14px">Jak wyglądają ostatnie dwa lata.</h2>
  </div>
  <p class="head-meta">Dane<br><strong>2024–2026</strong><br>24 warsztaty</p>
</div>
```

`<em>` w nagłówku daje kolor akcentu bez kursywy. **Jedno na nagłówek.**

---

## 2. Układy

```html
<div class="stack">…</div>              <!-- pion, gap standardowy -->
<div class="stack stack--tight">…</div> <!-- ciaśniej -->
<div class="stack stack--loose">…</div> <!-- luźniej: gdy slajd ma dwa bloki -->

<div class="split">                     <!-- 1:1 -->
  <div class="split-col">…</div>
  <div class="split-col">…</div>
</div>
<div class="split split--38">…</div>    <!-- wąska lewa (0,62 : 1) -->
<div class="split split--62">…</div>    <!-- wąska prawa (1 : 0,62) -->
<div class="split split--center">…</div><!-- wyrównanie do środka w pionie -->
<div class="split split--viz">…</div>   <!-- dwa wykresy: wspólna linia podpisów -->

<div class="cards cards--3">…</div>     <!-- --2 … --5 -->
```

Dobór: `.split--38` gdy lewa kolumna to tylko nagłówek, a prawa niesie treść.
`.split--62` gdy prawa jest wtrętem (wykres, cytat). Równy `.split` tylko wtedy,
gdy obie strony faktycznie ważą tyle samo.

`.split--viz` jest dla pary wykresów: krótszy rozciąga się do wysokości dłuższego,
a `.viz-cap` obu kolumn siada na jednej linii. Bez tego kolumny kończą się na różnej
wysokości i slajd rozpada się na wykres i ozdobnik — szczegóły w `charts.md`, zasada 8.

Powyżej czterech kart na slajdzie tekst schodzi poniżej progu czytelności —
`cards--5` jest dla haseł jednowyrazowych.

---

## 3. Karta

```html
<div class="card">
  <span class="card-num">01</span>
  <h3 class="card-title">Discovery</h3>
  <p class="card-text">Trzy sesje, które mapują, co organizacja realnie uruchomi.</p>
  <p class="card-foot">2 tygodnie · warsztat zdalny</p>
</div>
```

Warianty:

| Klasa | Efekt | Kiedy |
|---|---|---|
| `.card.is-accent` | poświata i obramowanie w kolorze akcentu | jedna karta na slajdzie, ta rekomendowana |
| `.card.is-dark` | ciemna karta na jasnym slajdzie | kontrapunkt, „to jest inne” |
| `.card.is-quiet` | wyciszona górna krawędź i numer | pozycja poboczna w zestawie |
| `.card-title--s` | mniejszy tytuł | gdy tytuł ma powyżej trzech słów |

`.card-foot` przykleja się do dołu karty — dzięki temu w rzędzie kart stopki są w jednej linii.

### Karta z numerem-znakiem wodnym

```html
<div class="card card--ghost">
  <span class="card-ghost" aria-hidden="true">01</span>
  <p class="card-lead">Przeprojektuj proces, zamiast doklejać agenta do starego obiegu.</p>
  <div class="card-foot"><span class="card-num">Workflow</span><br>
    Najsilniejszy związek z realnym wpływem na biznes.</div>
</div>
```

Numer wchodzi w tło karty jako duża cyfra w kolorze akcentu przy 14% krycia; treść niesie
`.card-lead` (akapit wiodący, jaśniejszy od `.card-text`), a etykieta schodzi do stopki.

Sięgaj po ten wariant tylko wtedy, gdy kolejność coś znaczy — etapy procesu, kroki wdrożenia,
uszeregowany ranking. Trzy równorzędne tezy ponumerowane 01/02/03 udają sekwencję, której nie ma.

Cyfra ma się mieścić w kadrze karty w całości. Wypuszczona poza krawędź jest nieodróżnialna
od przycięcia przez `overflow:hidden`, więc czyta się jak błąd, nie jak decyzja.
Rynnę `padding-right` dostaje wyłącznie `.card-lead` — niższe wiersze biorą pełną szerokość,
bo cyfra siedzi tylko przy górnej krawędzi.

---

## 4. Lista punktowana

```html
<div class="blist">
  <p class="bitem">Zbiór ewaluacyjny <strong>przed</strong> pierwszą linią kodu.</p>
  <p class="bitem">Granica narzędzi zdefiniowana i przetestowana.</p>
</div>

<div class="blist blist--tight">…</div>          <!-- ciaśniej -->
<p class="bitem bitem--s">Mniejszy stopień</p>
```

Punktorem jest heksagon. `.blist` jest blokiem, nie gridem — dzięki temu `<strong>`
wewnątrz zdania zostaje w wierszu, zamiast stać się osobnym elementem.

---

## 5. Wyróżnik (punch)

```html
<div class="punch">
  <p class="punch-text">Nie sprzedajemy pilotaży. Sprzedajemy wdrożenie.</p>
  <p class="punch-tag">Zasada<br>domu</p>
</div>
```

Jedno zdanie, które ma zostać w głowie. **Maksymalnie jeden na slajd**, w całym decku
dwa–trzy. Czwarty kasuje wagę pierwszego.

---

## 6. Liczby

```html
<div class="stats">
  <div class="stat">
    <span class="stat-num" data-count-to="94" data-count-suffix="%">94%</span>
    <span class="stat-lab">zgodność decyzji agenta z decyzją człowieka</span>
    <span class="stat-sub">próba 12 400 spraw</span>
  </div>
  …
</div>

<div class="stats stats--wrap">…</div>   <!-- zawijanie, gdy liczb jest więcej niż cztery -->
```

`.stat-num` ma gradient mięta→błękit i wagę 600. `<sup>` w środku (`14<sup>×</sup>`)
schodzi do 44% stopnia. Liczby odliczają się od zera po wejściu na slajd — działa to
tylko dla `data-count-to` z liczbą całkowitą.

---

## 7. Proces (flow)

```html
<div class="flow">
  <div class="flow-node">
    <span class="flow-n">01</span>
    <h4 class="flow-t">Discovery</h4>
    <p class="flow-d">Mapujemy procesy i wybieramy wykonalne.</p>
  </div>
  … 3–5 węzłów …
</div>
```

Węzły dzielą szerokość po równo. Powyżej pięciu przejdź na oś czasu (`.tl`) albo
infografikę `.chain`.

---

## 8. Tabela

```html
<table class="tbl">
  <thead>
    <tr><th>Moduł</th><th>Zakres</th><th class="t-price">Cena</th></tr>
  </thead>
  <tbody>
    <tr>
      <td class="t-name">AI Discovery</td>
      <td>Trzy sesje, raport, backlog z priorytetami</td>
      <td class="t-price">18 000 zł</td>
    </tr>
    <tr class="is-total">
      <td class="t-name">Razem</td><td class="t-meta">przy pakiecie</td>
      <td class="t-price">54 000 zł</td>
    </tr>
  </tbody>
</table>
```

`.t-name` nie zawija się i jest w kolorze nagłówka. `.t-price` idzie do prawej,
w monospace, w kolorze akcentu. `tr.is-total` dostaje linię akcentu nad sobą.

---

## 9. Chipy

```html
<div class="chips">
  <span class="chip is-on">UiPath</span>
  <span class="chip">LangGraph</span>
  <span class="chip">Azure OpenAI</span>
</div>
```

Do stosów technologicznych i zakresów. `.is-on` wyróżnia to, co dotyczy klienta.

---

## 10. Oś czasu

```html
<div class="tl">
  <div class="tl-item">
    <span class="tl-when">Tydz. 1–2</span>
    <div class="tl-what">
      <h4 class="tl-t">Discovery</h4>
      <p class="tl-d">Warsztaty, inwentaryzacja procesów, wybór pierwszego przypadku.</p>
    </div>
  </div>
  …
</div>
```

Do harmonogramów. Powyżej sześciu pozycji rozważ podział na dwa slajdy —
oś czasu nie skraca się dobrze.

---

## 11. Cytat / opinia

```html
<div class="tq">
  <span class="tq-mark">&rdquo;</span>
  <p class="tq-text">Pierwszy raz dostaliśmy backlog, który dało się od razu wycenić.</p>
  <p class="tq-who"><b>Anna Nowak</b> · Dyrektor Operacyjny, [KLIENT]</p>
</div>
```

Cytat bez nazwiska i roli nie jest dowodem — jest ozdobą. Jeśli klient nie zgodził się
na nazwisko, podaj przynajmniej rolę i branżę.

---

## 12. Separator sekcji

```html
<div class="sect">
  <span class="sect-num">03</span>
  <h2 class="sect-title">Warunki współpracy</h2>
  <p class="lead">Trzy rzeczy do ustalenia: zakres, tempo i kto po stronie klienta decyduje.</p>
</div>
```

Gigantyczny numer w konturze (`-webkit-text-stroke`). Zawsze na slajdzie ciemnym —
to oddech przed nową częścią.

---

## 13. Logotypy i box z linkiem

```html
<div class="logos">
  <img class="logo-item" src="…" alt="Nazwa klienta">
</div>

<a class="linkbox" data-video="https://www.youtube.com/embed/…">
  <span class="lb-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
  <span class="lb-text">
    <span class="lb-t">Demo agenta — 3 minuty</span>
    <span class="lb-d">wideo · otwiera się w oknie</span>
  </span>
</a>
```

Logotypy są domyślnie w skali szarości i wygaszone — kolorują się na hover.
`data-video` otwiera lightbox; z `file://` YouTube blokuje osadzenie, więc skrypt
otwiera link w nowej karcie.

---

## 14. Okładka

```html
<div class="cover">
  <div class="cover-logo" data-step="0">
    <svg viewBox="0 0 240 275" aria-label="CloudBots">
      <polygon points="80,0 160,46.2 160,138.6 80,184.8 0,138.6 0,46.2" fill="#A9F5D6" opacity=".7"/>
      <polygon points="80,0 160,46.2 160,138.6 80,184.8 0,138.6 0,46.2" transform="translate(80,45)" fill="#84DCF1" opacity=".7"/>
      <polygon points="80,0 160,46.2 160,138.6 80,184.8 0,138.6 0,46.2" transform="translate(0,90)" fill="#84F1F1" opacity=".7"/>
    </svg>
    <b>CLOUDBOTS</b>
  </div>
  <p class="eyebrow" data-step="1">Przegląd kompetencji · 2026</p>
  <h1 class="h-display" data-step="1" style="max-width:20ch">…</h1>
  <p class="h-sub" data-step="2" style="max-width:56ch">…</p>
  <div class="cover-meta" data-step="3">
    <div>Dla<b>[KLIENT]</b></div>
    <div>Data<b>[MIESIĄC ROK]</b></div>
    <div>Autor<b>Imię Nazwisko</b></div>
  </div>
</div>
```

Logo jest wklejone inline — deck nie ma zależności zewnętrznych. Te same trzy poligony
są w `assets/cloudbots-logo.svg` i w płótnach graficznych.

---

## 15. Spis treści

```html
<div class="toc">
  <div class="toc-row">
    <span class="toc-n">01</span>
    <span class="toc-t">AI Discovery</span>
    <span class="toc-d">Trzy sesje, które mapują, co organizacja realnie uruchomi.</span>
  </div>
  …
</div>
```

Kolumny 56px / 1fr / 1,35fr. Opis w trzeciej kolumnie jest obowiązkowy —
spis treści z samymi tytułami nie niesie informacji, którą menu już podaje.

---

## 16. Kontakt

```html
<div class="contact">
  <svg class="contact-mark" viewBox="0 0 240 275" aria-label="CloudBots">…</svg>
  <div class="contact-lines">
    <span>Imię Nazwisko · rola</span>
    <a href="mailto:…">adres@cloudbots.eu</a>
    <a href="tel:…">+48 …</a>
    <a href="https://cloudbots.eu">cloudbots.eu</a>
  </div>
</div>
```

Domyślnie w lewej kolumnie stoi znak firmowy (`.contact-mark`) — ten sam inline SVG
co na okładce. Sam jest heksagonem, więc trzyma sygnaturę bez pustego kadru.

Ze zdjęciem prelegenta podmień `<svg>` na `<img class="contact-photo" src="zdjecie.jpg"
alt="Imię Nazwisko">` — `.contact-photo` obetnie je kadrem heksagonalnym. Nie zostawiaj
pustego `<div class="contact-photo">`: gradient bez zdjęcia czyta się jak błąd ładowania.

---

## 17. Kroki odsłaniania

```html
<div data-step="0">nagłówek — widoczny od razu</div>
<div data-step="1">pierwszy blok</div>
<div data-step="1">drugi blok — wchodzi razem z pierwszym</div>
<div data-step="2">puenta</div>
```

- **Tryb dokument** (domyślny): wszystko widać, kroki dają tylko kaskadę wejścia
  z opóźnieniem `numer × 0,13 s`.
- **Tryb prezentacja** (przycisk „Dokument/Prezentacja”, klawisz `P`): kroki czekają
  na strzałkę. Strzałka w prawo najpierw odsłania kolejny krok, dopiero potem przechodzi
  na następny slajd.

Numeruj od 0. Nagłówek zawsze `data-step="0"` — inaczej slajd startuje pusty.

---

## 18. Sterowanie decku (co user zobaczy)

| Przycisk / klawisz | Działanie |
|---|---|
| uchwyt przy lewej krawędzi (`M`) | wysuwa menu ze spisem slajdów; `Esc` zamyka |
| ←/→, ↑/↓, PageUp/Down, spacja | slajd w tył / w przód |
| `Home` / `End` | pierwszy / ostatni slajd |
| `1`–`9` | skok do slajdu o tym numerze |
| kółko myszy | jeden gest = jeden slajd |
| **Dopasuj** (`F`) | Zmieść → Wypełnij → 1:1 |
| **+ / −** | zoom użytkownika 0,6–1,6×, zapamiętywany w `localStorage` |
| **Dokument / Prezentacja** (`P`) | tryb kroków |
| **Szczegóły** (`D`) | pokazuje elementy `.detail` |
| **Auto** (`A`) | autoodtwarzanie co 7 s z kółkiem odliczającym, zapętla się |
| **Anim** | prosta → pełna → brak |
| **EN / PL** (`L`) | przełącza treści `data-en` |
| **PDF**, **PPTX** | eksport (patrz `export.md`) |
| **•••** | rozwija drugi rząd sterowania |

Skala autofitu jest ograniczona do 0,45–1,30. Slajd, który w trybie „Zmieść” dobija
do dolnej granicy, jest przeładowany — podziel go zamiast walczyć ze stopniem pisma.
