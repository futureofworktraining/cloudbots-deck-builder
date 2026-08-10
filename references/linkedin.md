# Grafiki na LinkedIn

Dziewięć płócien w `assets/cloudbots-linkedin.html`. Otwórz w przeglądarce, żeby zobaczyć;
tu jest instrukcja wymiany treści i to, czego format nie wybaczy.

---

## Formaty, które LinkedIn faktycznie obsługuje

| Klasa | Rozmiar | Zastosowanie |
|---|---|---|
| `.f-45` | 1080 × 1350 (4:5) | post pojedynczy i slajd karuzeli — **zajmuje najwięcej miejsca w feedzie** |
| `.f-sq` | 1080 × 1080 (1:1) | post kwadratowy |
| `.f-link` | 1200 × 628 (1,91:1) | grafika pod linkiem (og:image), widoczna też w Slacku i mailu |
| `.f-banner` | 1584 × 396 | baner profilu firmowego |

**4:5 jest domyślnym wyborem.** Kwadrat bierz, gdy grafika ma krążyć także poza LinkedInem.

Motywy: `.canvas` (ciemne), `.canvas.light`, `.canvas.brand` — ciemna zieleń morska
z poświatą, do materiałów, które mają wyglądać na firmowe już w miniaturze.

---

## Twarde progi

**1. Minimum 26 px stopnia pisma przy szerokości 1080 px.** Poniżej tekst znika
na miniaturze telefonu. Każdy tekst na płótnach spełnia ten próg — jeśli twoja treść
się nie mieści, **skróć treść, nie stopień**.

**2. Maksymalnie cztery pozycje na liście.** Piąta zbija stopień poniżej progu.
Pięć punktów = karuzela, nie ciaśniejszy post.

**3. Jedno wyróżnienie na płótno.** `<em>` w nagłówku, `.is-hi` w porównaniu,
gradient na liczbie — jedno z nich, nie trzy.

**4. Dolne 15% kadru czyta się gorzej** — w feedzie zasłania je podgląd tekstu posta
i przycisk „zobacz więcej”. Dlatego CTA idzie do `.li-foot`, a nie na sam dół treści.

## Wspólny szkielet

```html
<div class="canvas f-45 brand" data-render="li-liczba">
  <span class="bar"></span>                       <!-- pasek akcentu przy górnej krawędzi -->
  <div class="hex-deco" style="width:400px;height:462px;top:190px;right:56px"></div>
  <p class="li-eyebrow">Discovery 2025</p>
  <div class="li-body low">…treść…</div>
  <div class="li-foot">
    <div class="mark">…logo…<span class="wm">CLOUDBOTS</span></div>
    <p class="li-cta">Pełne dane<br>w komentarzu</p>
  </div>
</div>
```

`.li-body` centruje treść w pionie. **`.li-body.low` kotwiczy ją nisko** — w kadrze 4:5
krótka treść wyśrodkowana zostawia dwa równe puste pasy i traci napięcie; przy kotwiczeniu
pustka zbiera się u góry jako oddech. Używaj `.low` wszędzie tam, gdzie treść nie wypełnia
kadru: liczba-bomba, cytat, mit/fakt, slajdy karuzeli.

Dekoracja: **jeden heksagon, w całości w kadrze**, H = W · 1,1547. Przycięty czyta się
jak strzałka albo latawiec, nie jak znak marki.

---

## 1. `li-liczba` — liczba-bomba · 4:5, brand

```html
<div class="li-body low">
  <p class="big">9<span class="big-unit">/100</span></p>
  <p class="big-lab">procesów zgłoszonych do automatyzacji trafia na produkcję.</p>
  <p class="li-p">Reszta odpada na braku właściciela i danych — nie na technologii.</p>
</div>
```

Do postu stojącego na jednej danej. Liczba jest całym obrazkiem (250 px, gradient
mięta→turkus→turkus ciemny na wariancie `brand`), `.big-lab` dopowiada ją **jednym zdaniem**,
resztę bierze na siebie tekst posta. Liczba dłuższa niż cztery znaki traci efekt —
„9/100” działa, „1 247 893” nie.

## 2. `li-teza` — teza · 1:1

```html
<h2 class="li-h">Twój agent nie ma<br>problemu z modelem.<br>Ma problem z <em>danymi</em>.</h2>
<p class="li-p">Zmiana modelu to jeden wieczór. Uporządkowanie źródeł prawdy to kwartał.</p>
```

Jedno zdanie, które ma zatrzymać scroll. Łam wiersze ręcznie przez `<br>` — rytm łamania
jest częścią przekazu. `<em>` na **jednym** słowie.

## 3. `li-lista` — lista punktów · `.plist` · 4:5, jasne

```html
<div class="pi"><span class="pn">01</span><div>
  <h3 class="pt">Kto jest właścicielem procesu?</h3>
  <p class="pd">Nie działu. Konkretnej osoby, która zdecyduje o zmianie reguły.</p>
</div></div>
```

Maksymalnie cztery pozycje. Nagłówek dostaje `.li-h.sm`, bo lista zabiera miejsce.
Tytuł punktu do siedmiu słów, opis do dwóch wierszy.

## 4. `li-cytat` — cytat · 1:1, jasne

```html
<blockquote class="quote">Przestaliśmy pytać, czy AI zadziała. Zaczęliśmy pytać, który proces jest na nią gotowy.</blockquote>
<div class="who">
  <span class="ph"></span>
  <span><span class="wn">Anna Kowalska</span><br><span class="wr">DYREKTORKA OPERACYJNA</span></span>
</div>
```

`.ph` to heksagonalny kadr na zdjęcie — podmień `<span>` na `<img class="ph" src="…">`.
Bez zdjęcia zostaje gradient. Cytat do 140 znaków; dłuższy przestaje być cytatem
i staje się akapitem. Nazwisko i rola są obowiązkowe — anonimowy cytat nie jest dowodem.

## 5. `li-mitfakt` — mit / fakt · `.mf` · 4:5

```html
<div class="mf">
  <div class="box"><p class="bl">Mit</p><p class="bt">„Wdrażamy agenta, więc redukujemy etaty."</p></div>
  <div class="box is-hi"><p class="bl">Fakt</p><p class="bt">Agent przejmuje kwalifikację i przepisywanie danych…</p></div>
</div>
```

Nagłówek stawiaj jako **pytanie** — to ono zatrzymuje scroll, nie odpowiedź.
`.is-hi` zawsze na faktach. Mit w cudzysłowie, fakt bez — różnica cudzysłowu robi
połowę roboty.

## 6. `li-kar-1/2/3` — karuzela · 4:5 × 3 · PDF

Trzy płótna: **okładka, treść, wezwanie**. Ten sam schemat działa dla pięciu i siedmiu.

```html
<span class="pager"><i style="--v:33.3%"></i></span>   <!-- 1/3 · 66,6% · 100% -->
<span class="swipe">Przesuń <svg>…</svg></span>        <!-- tylko na slajdach 1..n−1 -->
```

- `--v` w `.pager` to `numer / liczba slajdów`, w procentach. Przy pięciu slajdach:
  20%, 40%, 60%, 80%, 100%.
- Eyebrow numeruje slajd: „Karuzela · 1 z 3”.
- Motywy przeplataj (brand → ciemny → jasny) — jednolita karuzela wygląda na jeden
  długi obraz przycięty na trzy.
- Ostatni slajd niesie CTA i nie ma już `.swipe`.

Złożenie do PDF-a, którego oczekuje LinkedIn:

```
cd assets
python ../scripts/render.py "li-kar-*" --file cloudbots-linkedin.html --pdf karuzela.pdf
```

Wzorzec musi być w cudzysłowie, inaczej rozwinie go powłoka. Kolejność stron jest taka
jak kolejność płócien w pliku — trzymaj `li-kar-1`, `-2`, `-3` po kolei.

## 7. `li-link` — grafika pod linkiem · 1200 × 628, brand

Kadr niski: **jedno zdanie i data, bez akapitów**. `.li-body` bez `.low` — przy tej
wysokości środek jest właściwym miejscem. `.li-cta` w stopce niesie adres rejestracji.

Ta grafika pojawia się też przy udostępnieniu w Slacku i w podglądzie maila —
sprawdź, czy tytuł czyta się bez kontekstu posta.

## 8. `li-baner` — baner profilu firmowego · 1584 × 396, brand

**Strefy bezpieczne, których nie da się obejść:**
- na desktopie **logo profilu przykrywa lewy dolny róg** — stąd zapas 120 px od dołu
  po lewej i `padding-left:260px` na bloku treści;
- na telefonie **boki są przycinane** — treść musi zmieścić się w środkowym pasie;
- `.bside` (logo + adres) siedzi po prawej i jest pierwszą rzeczą, która zniknie
  na wąskim ekranie. Nie umieszczaj tam nic krytycznego.

```html
<div style="padding-left:260px">
  <h2 class="bh">Agenci AI, które wchodzą na produkcję.</h2>
  <p class="bp">Discovery · Wdrożenia · Szkolenia</p>
</div>
```

Jedno zdanie i jedna linia usług. Baner nie jest miejscem na ofertę.

---

## Renderowanie i kontrola

```
cd assets
python ../scripts/render.py --file cloudbots-linkedin.html            # wszystko, ×2
python ../scripts/render.py li-teza li-cytat --file cloudbots-linkedin.html
python ../scripts/render.py "li-kar-*" --file cloudbots-linkedin.html --pdf karuzela.pdf
```

Kontrola przed wysłaniem:
1. **Obejrzyj PNG w 100%** — podgląd w galerii jest zmniejszony i wybacza za mały tekst.
2. **Zmniejsz go do ~200 px szerokości** i sprawdź, czy główny komunikat wciąż się czyta.
   Tak wygląda miniatura w feedzie na telefonie.
3. Sprawdź, czy heksagon nie jest przycięty i czy logo nie wchodzi w treść.
4. Karuzela: otwórz PDF i przewiń — pasek postępu musi rosnąć, numeracja się zgadzać.
