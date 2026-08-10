# System wizualny CloudBots

Źródła: oferta `Kingfisher-uproszczona` (układ, rytm, przeplot motywów) i strona
`cloudbots.eu` (kolor, heksagon, typografia). Ten dokument opisuje, co jest stałe
we wszystkich czterech elementach skilla — decku, wykresach, infografikach i grafikach
na LinkedIn.

---

## 1. Kolory marki

```css
--cb-primary:#00CED1;      /* turkus — sygnatura, akcent numer jeden */
--cb-primary-700:#00b8b8;  /* ciemniejszy wariant do hover / drugiego planu */
--cb-mint:#A9F5D6;         /* mięta — pierwszy heksagon logo */
--cb-cyan:#84DCF1;         /* błękit — drugi heksagon */
--cb-turq:#84F1F1;         /* turkus jasny — trzeci heksagon */
--cb-cyan-deep:#0891b2;    /* akcent na jasnym tle: #00CED1 na bieli ma za mało kontrastu */
--cb-softblue:#E0F2FE;     /* poświata w tle jasnych slajdów */
```

`--cb-primary` na białym tle daje kontrast ~1,9:1 — jest nieczytelny jako kolor tekstu.
Dlatego na motywie jasnym `--accent` przełącza się na `--cb-cyan-deep`. Turkus zostaje
na jasnym tylko jako **wypełnienie** (słupek, kafel, kropka), nigdy jako litera.

## 2. Motywy

Dwa komplety zmiennych, przełączane klasą. Zmienne nazywają rolę, nie kolor —
komponent nigdy nie sięga po `--d-bg-1`, tylko po `--bg-1`.

| Rola | Ciemny | Jasny |
|---|---|---|
| `--bg-0` tło kadru | `#08090f` | `#F8FAFC` |
| `--bg-1` warstwa | `#0e1019` | `#f1f5f9` |
| `--bg-2` karta | `#161927` | `#ffffff` |
| `--ink-0` nagłówek | `#f4f1e8` | `#0f1729` |
| `--ink-1` tekst | `#c2c5d2` | `#243043` |
| `--ink-2` tekst wtórny | `#7b819a` | `#475569` |
| `--ink-3` metadane | `#4a4f63` * | `#7b8a9d` |
| `--line` | `rgba(255,255,255,.10)` | `rgba(15,23,41,.11)` |
| `--accent` | `--cb-primary` | `--cb-cyan-deep` |

\* W **infografikach i grafikach na LinkedIn** `--ink-3` jest podniesione do `#606779`.
Deck ogląda się na kontrolowanym ekranie, grafikę na telefonie w słońcu i na wydruku —
tam `#4a4f63` na czerni schodzi poniżej 3:1.

**Selektor motywu jest inny w każdym pliku** — to najczęstsze źródło pomyłki:

| Plik | Ciemny | Jasny |
|---|---|---|
| deck | `.slide--dark` (na sekcji slajdu) | `.slide--light` + `body.is-light` dla ramy |
| galeria wykresów | domyślny | `body.light` |
| infografiki, LinkedIn | domyślny `.canvas` | `.canvas.light`, dodatkowo `.canvas.brand` |

`.canvas.brand` to trzeci wariant, tylko dla LinkedIna: ciemna zieleń morska
`radial-gradient(… #0d3b44 …, #04141a)` pod grafiki, które mają wyglądać na firmowe
z odległości miniatury.

**Przeplot motywów w decku jest narzędziem narracji.** Ciemny slajd po dwóch jasnych
działa jak cezura — stawiaj go na okładce, separatorze sekcji i kontakcie. Cały deck
w jednym motywie jest płaski.

## 3. Typografia

```css
--ff-display:'Space Grotesk';   /* nagłówki, liczby, tytuły kart */
--ff-body:'Inter';              /* tekst ciągły */
--ff-mono:'JetBrains Mono';     /* metadane, etykiety osi, eyebrow, wartości */
--ff-logo:'Exo 2';              /* WYŁĄCZNIE wordmark CLOUDBOTS */
```

Skala decku jest płynna (`clamp`), skala płócien — stała w pikselach, bo kadr też jest stały.

| Token | Zakres | Rola |
|---|---|---|
| `--fs-display-xl` | 42–74 px | tytuł okładki, jeden na deck |
| `--fs-display-l` | 30–50 px | `h2` slajdu |
| `--fs-display-m` | 24–36 px | `.h-title--s` |
| `--fs-display-s` | 19–26 px | tytuł karty |
| `--fs-lead` | 15–20 px | lead, podtytuł |
| `--fs-body` | 13,5–17 px | tekst |
| `--fs-small` | 12–14,5 px | metadane, tabela |
| `--fs-mono` | 12–15,5 px | eyebrow |

Reguły:
- Nagłówki mają **wagę 500, nie 700**. Space Grotesk w bold robi się ciężki, a marka
  jest techniczna, nie krzykliwa. Waga 600 zostaje dla liczb.
- Ujemny tracking rośnie ze stopniem: `-.028em` w display-xl, `-.015em` w tytule karty.
- Wersaliki z trackingiem `.14em`–`.24em` tylko w monospace. W Inter wyglądają na błąd.
- `text-wrap:balance` na nagłówkach — bez tego ostatnie słowo zostaje samo w wierszu.
- Akcent w nagłówku: `<em>słowo</em>` (kolor akcentu, bez kursywy). **Jedno wyróżnienie
  na nagłówek.** Dwa znoszą się nawzajem.

## 4. Heksagon — sygnatura marki

Jeden clip-path, używany wszędzie:

```css
--hex:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
```

To heksagon **spiczasty do góry** (pointy-top). Wynika z tego geometria, której nie da się
obejść: **H = W · 1,1547**. Podaj obie wartości — samo `width` daje zdeformowany kształt.
Sąsiedzi w plastrze leżą na lewo, na prawo i po skosie — **nigdy dokładnie nad i pod**.

Gdzie występuje:
- punktor listy (`.bitem::before`), kropka w chrome, ikona w `.linkbox`, jednostka piktogramu;
- kadr zdjęcia w slajdzie kontaktowym (`.contact-photo`);
- logo (trzy heksagony: mięta, błękit, turkus, z przesunięciem `translate(80,45)` i `(0,90)`);
- dekoracja tła.

**Reguła dekoracji: heksagon dekoracyjny musi mieścić się w całości w kadrze.**
Przycięty u góry czyta się jak strzałka w dół, przycięty z boku — jak latawiec.
Ani jedno, ani drugie nie czyta się jak znak marki. W decku dekoracja żyje w `.hex-deco`
(kilka `<span>` z animacją unoszenia, opacity .06–.16), na płótnach — jeden `.hex-deco`
z jawnym `width`/`height`/`top`/`right`, opacity `.05`, **nigdy więcej niż jeden**.

## 5. Ziarno i siatka

Ziarno to inline'owy SVG `feTurbulence` w data-URI — jedna warstwa na całym kadrze,
`opacity:.04` z `mix-blend-mode:overlay` na ciemnym, `.025` z `multiply` na jasnym.
Jest w decku, w infografikach i w grafikach LinkedIn; bez niego płótna wyglądają
jak obcy zestaw doklejony do prezentacji.

`.grid-deco` to druga, dyskretna warstwa atmosfery: siatka 64–74 px wygaszana maską
radialną, `opacity:.05`. Stosuj rzadko, na slajdach „technicznych”.

## 6. Rytm i gęstość

```css
--pad-y:clamp(22px,3vh,40px);  --pad-x:clamp(34px,4.2vw,76px);
--gap:clamp(16px,1.6vw,28px);
--ease:cubic-bezier(.16,1,.3,1);
```

- **Zero zaokrągleń.** `border-radius` nie występuje w tym systemie. Kant jest cechą marki.
- Karta ma `border-top:3px solid var(--accent)` — to jedyna gruba linia w systemie.
- Cienie prawie nie występują; głębię robi różnica tła (`--bg-2` na `--bg-0`).
- Kolumny nigdy nie są równe „bo tak” — `.split--38` i `.split--62` niosą informację o wadze.

## 7. Skala kolorów danych

```css
--dv-1:var(--cb-primary);  --dv-2:#0E7490;  --dv-3:var(--cb-mint);
--dv-4:#5B7FE0;            --dv-5:#F2B441;  --dv-rest:#94A3B8;
--dv-pos:#10B981;          --dv-neg:#E15566;
--dv-track:rgba(148,163,184,.20);
```

Nadpisania per motyw (bo ten sam kolor nie działa na obu tłach):

| | ciemny | jasny |
|---|---|---|
| `--dv-2` | `--cb-cyan` `#84DCF1` | `#0E7490` |
| `--dv-rest` | `#5b6379` | `#94A3B8` |
| `--dv-track` | `rgba(255,255,255,.10)` | `rgba(15,23,41,.10)` |

Zasady:
- Serie bierz **po kolei**, od `--dv-1`. Nie przeskakuj do `--dv-5`, bo „ładniejszy”.
- `--dv-rest` jest zarezerwowane dla kategorii „pozostałe” — szary mówi „to nie jest
  osobna historia”.
- `--dv-pos` / `--dv-neg` tylko dla zmiany kierunkowej (wzrost / spadek), nie jako
  zwykłe kolory serii.
- **Nigdy nie koduj wartości przezroczystością.** Ten sam kolor z alfą daje nad czernią
  i nad bielą dwa różne kolory tła, więc żaden jeden kolor tekstu nie będzie czytelny
  w obu motywach. Rampa mapy ciepła jest z tego powodu podana wprost, jako `--hm-0`…`--hm-5`
  w obu motywach.

## 8. Dostępność i ruch

- Tekst na tle: `--ink-1` i `--ink-0` zawsze przechodzą 4,5:1; `--ink-2` i `--ink-3`
  są dla treści drugoplanowej i przechodzą 3:1.
- Tekst na wypełnieniu turkusowym jest **ciemny** (`#04141a`), nie biały.
- `@media (prefers-reduced-motion:reduce)` wyłącza animację heksagonów.
- Sterowanie decku ma `title` i `aria-label`; Esc zamyka menu i lightbox.
- Klasa `is-clean` na `body` chowa całe sterowanie — używa jej eksport i wydruk.

## 9. Wierność marce

Kolor, typografia i heksagon są nadrzędne nad kreatywnym odstępstwem. Kiedy sięgasz
po skill **frontend-design** (hero, diagram-bohater, nietypowa kompozycja), on projektuje
układ, ruch i detal — **w ramach** tych tokenów. Nowy kolor akcentu, zaokrąglone rogi
albo inny font to złamanie marki, nie kreatywność.
