# CloudBots Deck Builder

Skill dla [Claude Code](https://claude.com/claude-code) budujący materiały wizualne
CloudBots w jednym systemie graficznym.

| Element | Plik startowy | Wynik |
|---|---|---|
| **Prezentacja** | `assets/cloudbots-deck-template.html` | jeden plik `.html`, opcjonalnie PDF/PPTX |
| **Wykresy** | `assets/cloudbots-charts.html` | markup do wklejenia w deck albo PNG |
| **Infografiki** | `assets/cloudbots-infographics.html` | PNG w stałym kadrze (16:9, 1:1, 4:5, A4) |
| **LinkedIn** | `assets/cloudbots-linkedin.html` | PNG postów, karuzela jako PDF, baner profilu |

Wykresy, infografiki i grafiki na LinkedIn są osobnymi elementami — można po nie sięgnąć
bez budowania prezentacji.

## Deck

Jeden plik HTML bez zależności, otwiera się z dysku. Wysuwane menu przy lewej krawędzi,
nawigacja klawiaturą, tryb dokument/prezentacja z krokami odsłaniania, autoskalowanie treści
do kadru, autoodtwarzanie, trzy tryby animacji, wersja PL/EN, eksport PDF i PPTX.

Język wizualny wywiedziony z [cloudbots.eu](https://cloudbots.eu): ciemne i jasne kadry
przeplatane slajd po slajdzie, heksagon jako sygnatura, Space Grotesk w nagłówkach,
ziarno na całości, zero zaokrągleń.

## Instalacja

```bash
git clone https://github.com/futureofworktraining/cloudbots-deck-builder.git \
  ~/.claude/skills/cloudbots-deck-builder
```

Na Windowsie katalog docelowy to `%USERPROFILE%\.claude\skills\cloudbots-deck-builder`.
Dla pojedynczego projektu podmień na `<projekt>/.claude/skills/`.

Skrypty eksportu są opcjonalne:

```bash
pip install playwright python-pptx pillow
playwright install chromium
```

## Zawartość

```
SKILL.md                  instrukcja dla modelu — workflow, zasady twarde
references/               dokumentacja czytana na żądanie
  design-system.md          tokeny, typografia, motywy, heksagon, skala danych
  components.md             katalog układów i komponentów slajdu
  charts.md                 trzynaście typów wykresów + zasada doboru
  infographics.md           siedem płócien, co w każdym wolno wymienić
  linkedin.md               formaty, progi czytelności, strefy bezpieczne
  export.md                 PDF, PPTX, PNG, skrypty
assets/                   szablon decku i trzy galerie płócien + logo SVG
scripts/
  shot.py                   zrzuty kontrolne slajdów (QA)
  render.py                 płótna z data-render → PNG / PDF
  export-deck.py            deck → PPTX + PDF przez Chromium
```

## Użycie bez Claude Code

Pliki w `assets/` to zwykły HTML — otwórz w przeglądarce, podmień treść, wyrenderuj
skryptami z `scripts/`. `references/` opisuje, co w każdym płótnie wolno zmienić,
a czego nie ruszać (geometria heksagonów i kadrów jest przeliczona jako zestaw).

---

Materiały marki CloudBots.
