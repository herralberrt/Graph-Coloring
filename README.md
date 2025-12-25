# Graph Coloring

Acest proiect rezolvă problema **NP-2 Graph Coloring**. Scopul este colorarea vârfurilor unui graf neorientat astfel încât două vârfuri adiacente să nu aibă aceeași culoare, folosind un număr
minim de culori.

## Algoritmi implementați

În cadrul proiectului au fost implementați următorii algoritmi de
colorare a grafurilor:

### Backtracking

Algoritmul de backtracking este un algoritm exact, care explorează toate
posibilitățile de colorare și garantează obținerea numărului minim de culori.

Avantaje:
- oferă soluția optimă
- util pentru grafuri mici

Dezavantaje:
- timp de execuție foarte mare pentru grafuri mai mari
- nu este scalabil

### DSATUR

DSATUR este un algoritm euristic care colorează vârfurile în ordinea gradului
de saturație (numărul de culori diferite din vecinătate).

Avantaje:
- rapid
- oferă soluții bune în practică

Dezavantaje:
- nu garantează soluția optimă în toate cazurile

### RLF (Recursive Largest First)

RLF este un algoritm euristic care construiește pe rând mulțimi independente
maxime și le colorează succesiv.

Avantaje:
- eficient pentru grafuri dense
- implementare relativ simplă

Dezavantaje:
- calitatea soluției depinde de structura grafului

## Structura proiectului

Structura proiectului este:

.
├── backtracking.c # Algoritm exact de colorare
├── dsatur.c # Algoritmul DSATUR
├── rlf.c # Algoritmul RLF
├── bin/ # Executabilele compilate
│ ├── backtracking
│ ├── dsatur
│ └── rlf
├── scripts/
│ ├── generate_tests.py # Generator de teste
│ ├── run_benchmarks.py # Rulare benchmark
│ └── plot_results.py # Generare grafice
├── tests/ # Fisiere de test generate
├── plots/ # Graficele rezultate
│ ├── time_vs_vertices.png
│ ├── colors_vs_density.png
│ └── per_algorithm/
├── results.csv # Rezultatele benchmark-ului
└── README.md

## Formatul de intrare și ieșire

Toți algoritmii folosesc același format de intrare, conform cerinței problemei.

### Format de intrare

Un fișier de intrare conține:
- pe prima linie: două numere întregi `n` și `m`, unde:
  - `n` este numărul de vârfuri
  - `m` este numărul de muchii
- pe următoarele `m` linii: câte o muchie, sub forma `u v`

Exemplu:

4 3
0 1
1 2
2 3

### Format de ieșire

Pentru fiecare algoritm, ieșirea este:
- pe prima linie: numărul de culori folosite
- pe a doua linie: culorile atribuite fiecărui vârf, în ordine

Exemplu:

2
0 1 0 1

## Generarea testelor

Testele sunt generate automat folosind scriptul `generate_tests.py`.
Scopul acestuia este de a crea grafuri diferite ca mărime și densitate,
pentru a evalua comportamentul algoritmilor în diverse situații.

Scriptul generează grafuri neorientate cu:
- număr de vârfuri între 4 și 20
- densități diferite (raport între numărul de muchii și numărul maxim posibil)

Pentru fiecare combinație de dimensiune și densitate se generează un fișier
de test în directorul `tests/`.

### Rulare generator teste

Din directorul principal al proiectului:

- python3 scripts/generate_tests.py

După rulare, fișierele de intrare vor fi disponibile în directorul `tests/`
și pot fi folosite direct de algoritmi.

## Rularea benchmark-ului

Pentru a compara performanța algoritmilor, proiectul folosește scriptul
`run_benchmarks.py`, care rulează fiecare algoritm pe toate testele generate
și măsoară timpul de execuție și numărul de culori folosite.

Scriptul:
- rulează executabilele din directorul `bin/`
- citește fișierele de test din `tests/`
- salvează rezultatele într-un fișier `results.csv`

### Rulare benchmark

Din directorul principal al proiectului:

- python3 scripts/run_benchmarks.py

La finalul rulării, fișierul `results.csv` va conține, pentru fiecare test
și fiecare algoritm:
- numărul de vârfuri
- numărul de muchii
- numărul de culori folosite
- timpul de execuție

## Generarea și interpretarea graficelor

Pe baza rezultatelor obținute în urma benchmark-ului, sunt generate grafice
care evidențiază diferențele dintre algoritmi, atât din punct de vedere al
timpului de execuție, cât și al calității soluției.

Graficele sunt generate folosind scriptul `plot_results.py`.

### Rulare script pentru grafice

Din directorul principal al proiectului:

- python3 scripts/plot_results.py

Scriptul generează următoarele grafice:
- timp de execuție în funcție de numărul de vârfuri (comparativ)
- număr de culori în funcție de densitatea grafului (comparativ)
- grafice separate pentru fiecare algoritm

Toate graficele sunt salvate în directorul `plots/`.
