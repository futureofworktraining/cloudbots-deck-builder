# Infografiki CloudBots

Siedem płócien w `assets/cloudbots-infographics.html`. Otwórz plik w przeglądarce,
żeby je zobaczyć; ten dokument mówi, **co w każdym wolno wymienić, a czego nie**.

---

## Jak to działa

Płótno ma **stały rozmiar w pikselach**. To decyzja, nie niedoróbka: infografika jest
artefaktem o znanym kadrze, nie responsywną stroną. Podgląd w galerii jest zmniejszany
przez `transform:scale`, a `scripts/render.py` to skalowanie zdejmuje — dlatego PNG
zawsze wychodzi w nominalnym rozmiarze (domyślnie ×2).

```html
<div class="canvas c-169" data-render="ig-lancuch">   <!-- 1600 × 900 -->
```

| Klasa | Rozmiar | Do czego |
|---|---|---|
| `.c-169` | 1600 × 900 | slajd, nagłówek artykułu, prezentacja |
| `.c-sq` | 1080 × 1080 | post kwadratowy, miniatura |
| `.c-45` | 1080 × 1350 | post pionowy, karuzela |
| `.c-a4` | 1240 × 1754 | jednostronicowy PDF do druku |

Motyw: `.canvas` jest ciemne, `.canvas.light` jasne. Atrybut `data-render="nazwa"`
jest nazwą pliku PNG — zmień go, gdy robisz wariant, inaczej nadpiszesz oryginał.

## Wspólny szkielet

```html
<div class="canvas c-169" data-render="nazwa">
  <div class="grid-deco"></div>                                    <!-- opcjonalnie -->
  <div class="hex-deco" style="width:360px;height:415px;top:150px;right:110px"></div>
  <header>
    <p class="eyebrow">Nadtytuł</p>
    <h2 class="ig-title">Tytuł<br>w dwóch wierszach</h2>
    <p class="ig-sub">Jedno zdanie kontekstu.</p>                   <!-- opcjonalnie -->
  </header>
  <div class="ig-body">…</div>
  <footer class="ig-foot">
    <p class="ig-src">Skąd dane, jaka próba, jaki okres.</p>
    <div class="mark">…logo…<span class="wm">CLOUDBOTS</span><span class="dm">cloudbots.eu</span></div>
  </footer>
</div>
```

- `.ig-body` ma `flex:1` i centruje treść — nie ustawiaj mu wysokości.
- `.ig-src` jest **obowiązkowe**, gdy na płótnie są liczby. Infografika bez źródła
  krąży po sieci jako fakt.
- `.mark` to jedyne miejsce na logo. Nie dubluj go w nagłówku.

## Dekoracja

**`.hex-deco` musi mieścić się w kadrze w całości.** Podaj obie wartości i pamiętaj,
że heksagon jest spiczasty do góry: **H = W · 1,1547** (360 → 415, 300 → 346, 216 → 249).
Przycięty u góry czyta się jak strzałka w dół, przycięty z boku — jak latawiec.
**Jeden heksagon na płótno**, nigdy więcej.

---

## 1. `ig-lancuch` — łańcuch procesu · `.chain` · 1600 × 900, ciemne

Cztery etapy w rzędzie: numer, tytuł, opis, metryka czasu.

```html
<div class="node is-hi">
  <span class="cn">03</span>
  <h3 class="ct">Wdrożenie</h3>
  <p class="cd">Integracja z systemami, kontrola dostępu, obserwowalność, rollback.</p>
  <p class="cm">5 tygodni</p>
</div>
```

**Wymieniaj:** teksty, liczby etapów, metryki. **Trzymaj:** cztery węzły.
Trzy zostawiają dziurę, pięć zbija opis poniżej czytelności. Jeden `.is-hi` — ten,
o którym opowiadasz.

## 2. `ig-warstwy` — stos warstw · `.stack` · 1080 × 1350, jasne

Cztery warstwy architektury, od góry L4 do fundamentu L1.

```html
<div class="layer" style="--c:var(--cb-primary)">
  <span class="ln">L4</span>
  <span><span class="lt">Nadzór</span><span class="ld">Ewaluacja, logi decyzji, próg eskalacji.</span></span>
  <span class="lb">ciągły</span>
</div>
```

`--c` na warstwie ustawia jej kolor. Kolejność jest znacząca: **na górze to, co widać,
na dole fundament**. Ostatnia warstwa ma `.is-base` i szary `--c` — fundament nie
konkuruje kolorem z resztą. Cztery warstwy to maksimum tego kadru.

## 3. `ig-macierz` — macierz 2×2 · `.mtx` · 1080 × 1080, ciemne

Cztery ćwiartki plus dwie osie.

```html
<div class="ax ax-y">Wpływ na koszt →</div>
<div class="q is-hi">
  <div><h3 class="qt">Zacznij tutaj</h3><p class="qd">Powtarzalny, opisany, mierzalny.</p></div>
  <span class="qtag">Pilot 6–8 tygodni</span>
</div>
```

Kolejność ćwiartek w HTML to lewa górna → prawa górna → lewa dolna → prawa dolna.
Dokładnie **jedna** ma `.is-hi` — macierz z dwoma wyróżnieniami nie daje rekomendacji.
Opisy osi muszą mieć kierunek (strzałka albo „mało → dużo”), inaczej czytelnik nie wie,
gdzie jest lepiej.

## 4. `ig-oscasu` — roadmapa · `.road` · 1600 × 900, jasne

Cztery przystanki na poziomej osi.

```html
<div class="stop is-hi">
  <span class="when">Q3</span><span class="dot"></span>
  <h3 class="what">Platforma</h3>
  <p class="desc">Wspólna orkiestracja, obserwowalność, kontrola kosztu.</p>
</div>
```

Kropka siedzi na linii `.track` — nie przesuwaj jej ręcznie. Cztery przystanki
dzielą szerokość po równo; przy pięciu opis schodzi do dwóch wierszy i kadr się dusi.
Etykiety `when` trzymaj krótkie (Q1, Tydz. 6, 2026).

## 5. `ig-lejek` — lejek · `.funnel` · 1080 × 1350, ciemne

```html
<div class="fstep">
  <span class="fl">Opisane</span>
  <span class="fr" style="--w:62%;--c:var(--cb-turq)"><b class="fv">62</b></span>
</div>
<span class="fdrop">−34 · dane niedostępne lub niepełne</span>
```

**`--w` to wprost udział w największym etapie.** 100 → `100%`, 62 → `62%`, 28 → `28%`,
9 → `9%`. Nie „poprawiaj” szerokości, żeby ostatni pas ładniej wyglądał — wtedy grafika
kłamie, a cały sens lejka polega na tym, że ostatni pas jest mały.

Etykieta `.fl` idzie **nad** pasem, nie w środku — inaczej najwęższy pas nie ma jej gdzie
zmieścić i zaczyna się rozciąganie szerokości. `.fdrop` między krokami mówi, **dlaczego**
odpadło; lejek bez powodów odpadania to tylko cztery malejące prostokąty.

## 6. `ig-ekosystem` — plaster miodu · `.eco` · 1080 × 1080, ciemne

Siedem komórek: centralna `.core` i sześć wokół.

```html
<div class="cell" style="left:108px;top:3px">…</div>
<div class="cell core" style="left:213px;top:185px">…</div>
```

> **Nie ruszaj tych liczb pojedynczo.** Heksagon jest spiczasty do góry, więc sąsiedzi
> leżą na lewo, na prawo i po skosie — **nigdy dokładnie nad i pod**. Siatka: skok
> poziomy W = 210, pionowy 0,75 · H = 181,5, wiersze przesunięte o W/2. Przy komórce
> 204 × 235 zostaje 6 px fugi, a kontener ma 630 × 605. Zmiana jednej wartości rozspaja
> plaster. Albo przeliczasz cały zestaw, albo nie ruszasz nic.

Pozycje siedmiu komórek (lewa krawędź, góra):

```
(108,3)  (318,3)
(3,185)  (213,185)=core  (423,185)
(108,366) (318,366)
```

**Wymieniaj:** tylko `.et` (tytuł) i `.ed` (opis) w komórkach. Tytuł do dwóch słów,
opis do sześciu — komórka jest heksagonem, róg obcina tekst.

## 7. `ig-porownanie` — przed / po · `.vs` · 1600 × 900, ciemne

Dwie kolumny rozdzielone pionową etykietą.

```html
<div class="col is-hi">
  <span class="vh">Po 12 tygodniach</span>
  <span class="vbig">40 min</span>
  <span class="vrow">Mediana czasu pierwszej odpowiedzi</span>
  …
</div>
```

`.is-hi` zawsze na kolumnie „po”. Liczby `.vbig` muszą być **tą samą miarą** —
18 h obok 40 min działa (czas), 18 h obok 92% nie. Wierszy `.vrow` po tyle samo
w obu kolumnach i **parami w tej samej kolejności**: wiersz 2 z lewej odpowiada
wierszowi 2 z prawej. Bez tego porównanie się nie czyta.

---

## Renderowanie

```
cd assets
python ../scripts/render.py --file cloudbots-infographics.html --out ./_png
python ../scripts/render.py ig-lejek ig-ekosystem --file cloudbots-infographics.html
python ../scripts/render.py "ig-*" --scale 3 --file cloudbots-infographics.html   # do druku
```

Po wyrenderowaniu **obejrzyj PNG**. Podgląd w galerii jest zmniejszony i wybacza
za ciasny tekst, zderzenia dekoracji z treścią i przycięte heksagony — zrzut nie.
