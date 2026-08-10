# Wykresy CloudBots

Trzynaście typów, jeden system kolorów. Podgląd wszystkich na ciemnym i jasnym:
otwórz `assets/cloudbots-charts.html` w przeglądarce. Ten plik trzyma markup,
żeby nie było dwóch źródeł prawdy.

Ten sam markup działa w decku (`cloudbots-deck-template.html`) i w galerii —
klasy `.c-*` są w obu plikach identyczne.

---

## Zasady

**1. Wykres koduje wartość.** Słupek bez liczby za nim jest ozdobnikiem i szkodzi —
odbiorca czyta go jako dane. Jeśli nie masz liczby, napisz zdanie.

**2. Każdy wykres siedzi w `.viz`.**

```html
<div class="viz">
  <div class="c-bars">…</div>
  <p class="viz-cap">Podpis: co mierzymy, na jakiej próbie, kiedy.</p>
</div>
```

`.viz` to kontener zapytań (`container-type:inline-size`). Rozmiary wewnętrzne liczą się
w `cqw` — od szerokości `.viz`, nie od okna. Dzięki temu ten sam markup działa w wąskiej
kolumnie splitu i na całą szerokość slajdu, **bez klas rozmiaru**. Wykres wyjęty z `.viz`
rozjedzie się.

**3. Kolor tylko przez zmienne.** `--dv-1`…`--dv-5`, `--dv-rest`, `--dv-pos`, `--dv-neg`,
`--hm-0`…`--hm-5`. Kolor wpisany inline (`#00CED1`, `rgba(...)`) przestaje działać po
przełączeniu motywu — patrz `design-system.md` §7.

**4. Legenda klasą, nie kolorem.** `<i style="--c:var(--dv-2)">Etykieta <b>27%</b></i>`.

**5. Podpis `.viz-cap` jest obowiązkowy** wszędzie tam, gdzie liczba pochodzi z badania,
próby albo okresu. „24 warsztaty, 2024–2026, odpowiedzi wielokrotne” to różnica między
danymi a wrażeniem.

**6. Kolor serii tylko wtedy, gdy koduje kategorię.** Pozycje uszeregowane malejąco już
niosą swoją informację długością i kolejnością — pomalowanie ich na cztery kolory niczego
nie dodaje, a rozbija wykres na cztery niezwiązane paski. Zostaw jeden `--dv-1` i sięgnij
po drugi kolor wyłącznie tam, gdzie pozycja naprawdę jest innego rodzaju: `--dv-rest`
dla „Pozostałe” (worek, nie kategoria), `--dv-neg` dla wartości ujemnej, gradient
`.is-hi` dla prognozy obok faktów.

**7. Dwa wykresy obok siebie to jeden układ.** Owiń je w `.split.split--viz` — krótszy
rozciągnie się do wysokości dłuższego, a `.viz-cap` obu kolumn siądzie na wspólnej linii.
Bez tego prawa kolumna kończy się w powietrzu i slajd czyta się jako wykres plus ozdobnik.

```html
<div class="split split--viz">
  <div class="split-col"><div class="viz"><div class="c-bars">…</div><p class="viz-cap">…</p></div></div>
  <div class="split-col"><div class="viz"><div class="c-meter">…</div><p class="viz-cap">…</p></div></div>
</div>
```

Dobierz też proporcję do gęstości: cztery słupki potrzebują mniej miejsca niż cztery paski
z etykietami tekstowymi. Przy takiej parze zostań przy równym podziale — `.split--62`
rozciąga słupki tak, że przerwy między nimi zaczynają dominować nad danymi.

---

## Dobór typu

| Co masz | Czego użyj |
|---|---|
| szereg czasowy, do 6 punktów | `.c-bars` |
| szereg czasowy, powyżej 6 punktów | `.c-line` |
| kategorie z długimi nazwami, ranking | `.c-rank` |
| udziały, drugi wykres na slajdzie | `.c-meter` |
| jedna liczba niosąca przekaz + kontekst | `.c-donut` |
| jedna wartość względem pełnej skali (SLA, pokrycie) | `.c-gauge` |
| zmiana przed → po | `.c-delta` |
| struktura sumująca się do 100% | `.c-stack` |
| struktura, gdy jest miejsce i mało kategorii | `.c-pie` |
| dwie osie kategorii, jedna wartość | `.c-heat` |
| proporcja rzeczy policzalnych | `.c-units` |
| 3–5 liczb bez porównania między sobą | `.c-kpi` |
| liczba **i** porównanie w jednym wierszu | `.tbl` + `.micro` |

---

## 1. `.c-bars` — słupki pionowe

```html
<div class="viz">
  <div class="c-bars">
    <div class="b"><span class="bv">3</span><i class="bar" style="--v:19%"></i><span class="bx">2023</span></div>
    <div class="b"><span class="bv">7</span><i class="bar" style="--v:44%"></i><span class="bx">2024</span></div>
    <div class="b"><span class="bv">11</span><i class="bar" style="--v:69%"></i><span class="bx">2025</span></div>
    <div class="b is-hi"><span class="bv">16</span><i class="bar" style="--v:100%"></i><span class="bx">2026*</span></div>
  </div>
  <p class="viz-cap">Projekty rocznie. *prognoza z podpisanych umów.</p>
</div>
```

`--v` to udział w maksimum serii, nie wartość bezwzględna. `.is-hi` wyróżnia jeden słupek —
zwykle ostatni albo ten, o którym mówisz.

## 2. `.c-rank` — ranking poziomy

```html
<div class="c-rank">
  <div class="r"><span class="rn">01</span><span class="rl">Brak zbioru ewaluacyjnego</span>
      <span class="rt"><i class="rf" style="--v:88%"></i></span><span class="rv">88%</span></div>
  <div class="r is-rest"><span class="rn">04</span><span class="rl">Pozostałe</span>
      <span class="rt"><i class="rf" style="--v:23%"></i></span><span class="rv">23%</span></div>
</div>
```

Sortuj malejąco, zawsze. `.is-rest` szarzy pozycję „pozostałe” — ona nie jest osobną historią.
Etykieta jest wyrównana do prawej, żeby przylegała do słupka i oko nie skakało przez pustkę.

## 3. `.c-meter` — mierniki udziału

```html
<div class="c-meter">
  <div class="m"><span class="mh"><span>Usługi finansowe</span><b>42%</b></span>
      <span class="mt"><i class="mf" style="--v:42%"></i></span></div>
  <div class="m"><span class="mh"><span>Retail</span><b>26%</b></span>
      <span class="mt"><i class="mf" style="--v:26%"></i></span></div>
  <div class="m"><span class="mh"><span>Pozostałe</span><b>13%</b></span>
      <span class="mt"><i class="mf" style="--v:13%;--c:var(--dv-rest)"></i></span></div>
</div>
```

Lżejszy wizualnie od rankingu — nadaje się jako drugi wykres na slajdzie. Jeden kolor
na wszystkie pozycje, `--dv-rest` tylko dla worka „Pozostałe” (zasada 6).

Wartość stoi po prawej stronie w linii etykiety, nie przy końcu paska: przy 13% wpadłaby
w tor, a wyrównana kolumna liczb daje się porównać wzrokiem. Pustka po prawej przy niskich
udziałach to koszt tego, że tor sięga 100% — skala bez odniesienia przestaje być skalą.

W `.split--viz` mierniki rozkładają się na wysokość sąsiada. Działa to dla trzech do sześciu
pozycji; przy dwóch odstępy robią się większe niż same paski — wtedy zostaw zwykły `.split`.

## 4. `.c-donut` — pierścień

```html
<div style="display:flex;gap:34px;align-items:center;flex-wrap:wrap">
  <div class="viz" style="flex:0 0 auto;width:210px">
    <div class="c-donut" style="--ring:conic-gradient(var(--dv-1) 0 62%, var(--dv-2) 62% 84%, var(--dv-rest) 84% 100%)">
      <span class="dc"><span class="dv">62%</span><span class="dl">wdrożone</span></span>
    </div>
  </div>
  <div class="viz" style="flex:1 1 180px">
    <div class="legend legend--col">
      <i style="--c:var(--dv-1)">Wdrożone <b>62%</b></i>
      <i style="--c:var(--dv-2)">W budowie <b>22%</b></i>
      <i style="--c:var(--dv-rest)">Zatrzymane <b>16%</b></i>
    </div>
  </div>
</div>
```

Progi w `conic-gradient` są **kumulatywne**: 62% → 84% → 100%. Maksymalnie cztery udziały.
Liczba w środku niesie przekaz, reszta to kontekst.

## 5. `.c-gauge` — wskaźnik półkolisty

```html
<div class="viz" style="max-width:300px;margin:0 auto">
  <!-- łuk: r=80, długość półokręgu = π·80 ≈ 251,3; offset = 251,3 · (1 − wartość) -->
  <svg class="c-gauge" viewBox="0 0 200 128" role="img" aria-label="94 procent">
    <path class="gt" d="M20 108 A80 80 0 0 1 180 108" fill="none" stroke-width="14" stroke-linecap="round"/>
    <path class="gf" d="M20 108 A80 80 0 0 1 180 108" fill="none" stroke-width="14" stroke-linecap="round"
          stroke-dasharray="251.3" stroke-dashoffset="15.1"/>
    <text class="gv" x="100" y="98">94%</text>
    <text class="gl" x="100" y="120">SKUTECZNOŚĆ AGENTA</text>
  </svg>
</div>
```

Jedyne, co przeliczasz, to `stroke-dashoffset`: `251,3 · (1 − wartość)`.
Dla 94% → `251,3 · 0,06 ≈ 15,1`. Dla 70% → `75,4`.

## 6. `.c-delta` — przed → po

```html
<div class="c-delta">
  <div class="d"><span class="dv">500 h</span><i class="db" style="--v:100%"></i><span class="dl">przed</span></div>
  <div class="darrow"><span>−84%</span>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
  </div>
  <div class="d is-after"><span class="dv">80 h</span><i class="db" style="--v:16%"></i><span class="dl">po</span></div>
</div>
```

Najmocniejszy wykres na slajdzie z efektem. `--v` obu słupków liczy się **od tej samej
podstawy** — 500 h to 100%, 80 h to 16%. Inaczej wykres kłamie.

## 7. `.c-line` — linia z obszarem

```html
<svg class="c-line" viewBox="0 0 960 260" role="img" aria-label="Wykres liniowy">
  <defs>
    <linearGradient id="cbArea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#00CED1" stop-opacity=".28"/>
      <stop offset="100%" stop-color="#00CED1" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line class="gl" x1="60" y1="20"  x2="940" y2="20"/>
  <line class="gl" x1="60" y1="70"  x2="940" y2="70"/>
  <line class="gl" x1="60" y1="120" x2="940" y2="120"/>
  <line class="gl" x1="60" y1="170" x2="940" y2="170"/>
  <line class="ax" x1="60" y1="220" x2="940" y2="220"/>
  <path fill="url(#cbArea)" d="M60,190 L236,166 L412,120 L588,96 L764,54 L940,32 L940,220 L60,220 Z"/>
  <polyline class="ln2" points="60,196 236,186 412,176 588,166 764,156 940,146"/>
  <polyline class="ln"  points="60,190 236,166 412,120 588,96 764,54 940,32"/>
  <circle class="pt" cx="60" cy="190" r="4"/>… <circle class="pt" cx="940" cy="32" r="5"/>
  <text class="lb" x="60" y="242">STY</text>… <text class="lb" x="905" y="242">LIS</text>
</svg>
```

**Układ współrzędnych: x od 60 do 940, y od 20 do 220. Wartość `v` w skali 0–100 → `y = 220 − v·2`.**
Punkty rozstawiaj równomiernie: `x = 60 + i · (880 / (n−1))`.
Obszar (`<path>`) to ta sama ścieżka co linia, zamknięta przez `L940,220 L60,220 Z`.

`.ln2` (przerywana) to **zawsze punkt odniesienia** — baseline, cel, rok poprzedni —
nigdy druga równorzędna seria. Trzy serie na jednym wykresie to znak, że potrzebujesz
dwóch slajdów.

Jeśli kopiujesz wykres dwa razy na jeden slajd, zmień `id="cbArea"` — powtórzony
identyfikator gradientu skleja oba wykresy.

## 8. `.c-stack` — pasek 100%

```html
<div class="c-stack">
  <i style="--v:46%;--c:var(--dv-1)">46%</i>
  <i style="--v:27%;--c:var(--dv-2)">27%</i>
  <i style="--v:15%;--c:var(--dv-3)">15%</i>
  <i style="--v:12%;--c:var(--dv-rest)"></i>
</div>
<div class="legend" style="margin-top:12px">
  <i style="--c:var(--dv-1)">Discovery</i><i style="--c:var(--dv-2)">Budowa</i>
  <i style="--c:var(--dv-3)">Szkolenia</i><i style="--c:var(--dv-rest)">Doradztwo</i>
</div>
```

`--v` musi sumować się do 100%. Segment poniżej ~14% nie zmieści etykiety —
zostaw go pustym i podaj wartość w legendzie.

## 9. `.c-heat` — mapa ciepła

```html
<div class="c-heat" style="grid-template-columns:150px repeat(6,minmax(0,1fr))">
  <span class="hc hh"></span>
  <span class="hc hh">Prompt Chain</span><span class="hc hh">RAG</span>…

  <span class="hc hh" style="justify-items:start;text-align:left">Finanse</span>
  <span class="hc hm-5">5</span><span class="hc hm-4">4</span><span class="hc hm-0">0</span>…
</div>
<div class="legend" style="margin-top:14px">
  <i style="--c:var(--hm-1)">rzadko</i><i style="--c:var(--hm-3)">czasem</i><i style="--c:var(--hm-5)">standard</i>
</div>
```

Pierwsza komórka wiersza nagłówków jest pusta — trzyma róg siatki.
Rampa `.hm-0`…`.hm-5` ma podane wprost tło **i** kolor tekstu dla obu motywów;
tła siedzą w `--hm-0`…`--hm-5`, więc legenda bierze kolor stamtąd.
**Nie koloruj komórek inline** — alfa nad czernią i nad bielą daje dwa różne kolory
i tekst gdzieś zniknie.

## 10. `.c-units` — piktogram

```html
<div class="c-units" style="--u:17px">
  <i class="on"></i><i class="on"></i>… <i></i><i></i>
</div>
<p class="viz-cap">18 z 25 procesów przeszło ocenę wykonalności.</p>
```

Każda jednostka to heksagon. `--u` ustawia rozmiar; siatka zawija się sama.
Powyżej ~60 jednostek przestaje być czytelna — wtedy jedna jednostka = 10 sztuk,
i napisz to w podpisie.

## 11. `.c-kpi` — kafle

```html
<div class="c-kpi">
  <div class="k"><span class="kv">9</span><span class="kl">agentów na produkcji</span><span class="kd up">+4 r/r</span></div>
  <div class="k"><span class="kv">2,1 s</span><span class="kl">mediana czasu odpowiedzi</span><span class="kd down">−0,4 s</span></div>
</div>
```

`.kd.up` / `.kd.down` kolorują zmianę (`--dv-pos` / `--dv-neg`). Zmiana zawsze
ze znakiem **i okresem** — „+4” bez „r/r” nic nie znaczy.

## 12. `.c-pie` — kołowy

```html
<div class="c-pie" style="background:conic-gradient(var(--dv-1) 0 46%,var(--dv-2) 46% 73%,var(--dv-3) 73% 88%,var(--dv-rest) 88% 100%)"></div>
```

Wartości **zawsze w legendzie obok**, nigdy na wycinkach — na wycinku nie zmieszczą się
czytelnie. Powyżej czterech kategorii przejdź na `.c-stack` albo `.c-rank`.

## 13. `.tbl` + `.micro` — tabela z mikrosłupkiem

```html
<table class="tbl">
  <thead><tr><th>Proces</th><th>Pokrycie</th><th class="t-price">Oszczędność</th></tr></thead>
  <tbody>
    <tr><td class="t-name">Rejestracja faktur</td>
        <td><span class="micro"><i style="--v:92%"></i></span></td>
        <td class="t-price">340 h/mies.</td></tr>
  </tbody>
</table>
```

Gdy potrzebujesz i liczby, i porównania — mikrosłupek zastępuje osobny wykres.

---

## Eksport wykresu jako obrazka

Każde `<figure class="demo" data-render="chart-…">` w galerii da się wyrenderować:

```
cd assets
python ../scripts/render.py --file cloudbots-charts.html chart-heat chart-line
```

Galeria jest płynna, więc rozmiar PNG zależy od szerokości okna renderera
(1700 px viewportu). Do materiałów o stałym kadrze użyj infografik, nie galerii.
