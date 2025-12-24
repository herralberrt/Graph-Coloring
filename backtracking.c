#include <stdio.h>
#include <stdlib.h>

#define NMAX 20

// Structure of the graph
typedef struct {
	int n, m;
	int mat[NMAX][NMAX];
} Graph;

// Reading the graph
void reading(Graph *g)
{
	scanf("%d %d", &g->n, &g->m);

	for (int i = 0; i < g->n; i++) {
		for (int j = 0; j < g->n; j++) {
			g->mat[i][j] = 0;
		}
	}

	for (int i = 0; i < g->m; i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		g->mat[u][v] = 1;
		g->mat[v][u] = 1;
	}
}

// Building the order of vertices based on their degrees
void building(Graph *g, int *order)
{
	int deg[NMAX];

	for (int i = 0; i < g->n; i++) {
		int degree = 0;
		for (int j = 0; j < g->n; j++) {
			if (g->mat[i][j] == 1) {
				degree++;
			}
		}
		deg[i] = degree;
		order[i] = i;
	}

	for (int i = 0; i < g->n - 1; i++) {
		for (int j = i + 1; j < g->n; j++) {
			if (deg[order[i]] < deg[order[j]]) {
				int aux = order[i];
				order[i] = order[j];
				order[j] = aux;
			}
		}
	}
}

// Verifying if we can color vertex v with color c
int verifying_color(Graph *g, int *color, int v, int c)
{
	for (int i = 0; i < g->n; i++) {
		if (g->mat[v][i] == 1 && color[i] == c) {
			return 0;
		}
	}
	return 1;
}

// Backtracking function to color the graph
void backtrack(Graph *g, int *order, int *color, int nr,
			   int used_colors, int *best_k, int *best_color)
{
	// Pruning
	if (used_colors >= *best_k) {
		return;
	}

	// All vertices are colored
	if (nr == g->n) {
		*best_k = used_colors;
		for (int i = 0; i < g->n; i++) {
			best_color[i] = color[i];
		}
		return;
	}

	// Current vertex to color
	int v = order[nr];

	// Try to color with existing colors
	for (int c = 0; c < used_colors; c++) {
		if (verifying_color(g, color, v, c)) {
			color[v] = c;
			backtrack(g, order, color, nr+ 1, used_colors, best_k, best_color);
			color[v] = -1;
		}
	}

	// Try to color with a new color
	color[v] = used_colors;
	backtrack(g, order, color, nr+ 1, used_colors + 1, best_k, best_color);
	color[v] = -1;
}

int main(void)
{
	Graph g;
	int best_k, order[NMAX], color[NMAX], best_color[NMAX];

	reading(&g);
	building(&g, order);

	for (int i = 0; i < g.n; i++) {
		color[i] = -1;
	}
	best_k = g.n;

	backtrack(&g, order, color, 0, 0, &best_k, best_color);
	printf("%d\n", best_k);

	for (int i = 0; i < g.n; i++) {
		if (i > 0) {
			printf(" ");
		}
		printf("%d", best_color[i]);
	}
	printf("\n");
	return 0;
}
