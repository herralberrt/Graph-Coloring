# Graph Coloring

This project solves the **NP-2 Graph Coloring** problem. The goal is to color the
vertices of an undirected graph so that no two adjacent vertices share the same
color, using the minimum number of colors.

The project compares one exact algorithm against two heuristics, both in terms
of execution time and solution quality.

## Implemented algorithms

### Backtracking

Backtracking is an exact algorithm that explores all possible colorings and is
guaranteed to find the minimum number of colors.

Advantages:
- returns the optimal solution
- useful for small graphs

Disadvantages:
- very high execution time on larger graphs
- does not scale

### DSATUR

DSATUR is a heuristic that colors vertices in order of their saturation degree
(the number of distinct colors among their neighbors).

Advantages:
- fast
- produces good solutions in practice

Disadvantages:
- does not guarantee the optimal solution in every case

### RLF (Recursive Largest First)

RLF is a heuristic that builds maximal independent sets one at a time and colors
them successively.

Advantages:
- efficient on dense graphs
- relatively simple to implement

Disadvantages:
- solution quality depends on the structure of the graph

## Project structure

```
.
├── backtracking.c        # Exact coloring algorithm
├── dsatur.c              # DSATUR algorithm
├── rlf.c                 # RLF algorithm
├── scripts/
│   ├── generate_tests.py # Test generator
│   ├── run_benchmarks.py # Benchmark runner
│   └── plot_results.py   # Plot generation
├── tests/                # Generated test files
├── plots/                # Resulting plots
│   ├── time_vs_vertices.png
│   ├── colors_vs_density.png
│   └── per_algorithm/
├── results.csv           # Benchmark results
├── main.tex              # LaTeX source of the report
├── ProiectAA.pdf         # Project report
└── README.md
```

The compiled executables are produced in the `bin/` directory, which is not
tracked in the repository (see `.gitignore`).

## Requirements

- `gcc` to compile the algorithms
- `python3` for the testing and benchmarking scripts
- `matplotlib` to generate the plots:

```
pip install matplotlib
```

## Building

From the root directory of the project:

```
mkdir -p bin
gcc -O2 -Wall -o bin/backtracking backtracking.c
gcc -O2 -Wall -o bin/dsatur dsatur.c
gcc -O2 -Wall -o bin/rlf rlf.c
```

## Input and output format

All algorithms use the same input format, as required by the problem statement,
and read their data from standard input.

### Input format

An input file contains:
- on the first line: two integers `n` and `m`, where:
  - `n` is the number of vertices
  - `m` is the number of edges
- on the next `m` lines: one edge per line, in the form `u v`

Vertices are numbered from `0` to `n - 1`, and the maximum number of vertices
supported by the implementations is 20.

Example:

```
4 3
0 1
1 2
2 3
```

### Output format

For each algorithm, the output is:
- on the first line: the number of colors used
- on the second line: the color assigned to each vertex, in order

Example:

```
2
1 0 1 0
```

### Running a single algorithm

```
./bin/dsatur < tests/test_01.in
```

## Generating the tests

Tests are generated automatically using the `generate_tests.py` script. Its
purpose is to create graphs of varying size and density, in order to evaluate
how the algorithms behave across different situations.

The script generates undirected graphs with:
- between 2 and 20 vertices
- varying densities (the ratio between the number of edges and the maximum
  possible number of edges)

One test file is written to the `tests/` directory for each size and density
combination. The generator uses a fixed seed (`seed = 42`), so the tests are
reproducible.

To run it, from the root directory of the project:

```
python3 scripts/generate_tests.py
```

## Experimental setup

Tests were limited to graphs of at most 20 vertices so that the exact algorithm
(backtracking) could run within a reasonable time. It is used as the reference
point for evaluating the quality of the heuristic solutions.

For each graph size, instances with different densities were generated in order
to analyze how the structure of the graph influences algorithm performance.

## Running the benchmark

To compare algorithm performance, the project uses the `run_benchmarks.py`
script, which runs each algorithm on every generated test and measures the
execution time and the number of colors used.

The script:
- runs the executables from the `bin/` directory
- reads the test files from `tests/`
- saves the results to `results.csv`

To run it:

```
python3 scripts/run_benchmarks.py
```

## Solution quality

The backtracking algorithm provides the optimal solution for every instance.
The results obtained with the heuristics (DSATUR and RLF) are compared directly
against this optimal solution, using the number of colors as the quality metric.

## Generating and interpreting the plots

Based on the benchmark results, plots are generated that highlight the
differences between the algorithms, both in execution time and in solution
quality.

To run it, from the root directory of the project:

```
python3 scripts/plot_results.py
```

The script generates the following plots:
- execution time as a function of the number of vertices (comparative)
- number of colors as a function of graph density (comparative)
- separate plots for each algorithm

All plots are saved to the `plots/` directory.

## Observations

For very small graphs, execution time is dominated by fixed costs: process
startup, initialization, and reading the input files. For this reason, those
instances can appear slower than slightly larger graphs.

## Conclusions

Backtracking guarantees the optimal solution, but is only practical for small
graphs. The heuristics, DSATUR in particular, produce near-optimal solutions in
a very short time, making them better suited to larger graphs. RLF can be
efficient on dense graphs, but its solution quality depends on the structure of
the instance.

## Report

The full project report is available in `ProiectAA.pdf`, generated from the
LaTeX source `main.tex`. The report itself is written in Romanian.
