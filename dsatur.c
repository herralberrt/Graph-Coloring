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

// Calculating the degree of vertex v
int degree(Graph *g, int v)
{
    int degree = 0;
    for (int i = 0; i < g->n; i++) {
        if (g->mat[v][i] == 1) {
            degree++;
        }
    }
    return degree;
}

// Calculating the saturation degree of vertex v
int sat_deg(Graph *g, int *color, int v)
{
    int used[NMAX];
    for (int i = 0; i < NMAX; i++) {
        used[i] = 0;
    }

    for (int i = 0; i < g->n; i++) {
        if (g->mat[v][i] == 1 && color[i] != -1) {
            used[color[i]] = 1;
        }
    }

    int nr = 0;
    for (int i = 0; i < NMAX; i++) {
        if (used[i]) {
            nr++;
        }
    }

    return nr;
}

// Selecting the next vertex to color based on DSATUR criteria
int next_vertex(Graph *g, int *color)
{
    int best = -1;
    int best_sat = -1;
    int best_deg = -1;

    // Iterate through all vertices to find the one with highest saturation degree
    for (int v = 0; v < g->n; v++) {
        if (color[v] == -1) {
            int sat = sat_deg(g, color, v);
            int deg = degree(g, v);

            if (sat > best_sat || (sat == best_sat && deg > best_deg)) {
                best = v;
                best_sat = sat;
                best_deg = deg;
            }
        }
    }

    return best;
}

// Finding the first available color for vertex v
int available_color(Graph *g, int *color, int v)
{
    int used[NMAX];
    for (int i = 0; i < NMAX; i++) {
        used[i] = 0;
    }

    for (int i = 0; i < g->n; i++) {
        if (g->mat[v][i] == 1 && color[i] != -1) {
            used[color[i]] = 1;
        }
    }

    for (int c = 0; c < NMAX; c++) {
        if (!used[c]) {
            return c;
        }
    }

    return -1;
}

// DSATUR algorithm to color the graph
int dsatur(Graph *g, int *color)
{
    for (int i = 0; i < g->n; i++) {
        color[i] = -1;
    }

    int nr_col = -1;

    for (int i = 0; i < g->n; i++) {
        int v = next_vertex(g, color);
        int c = available_color(g, color, v);

        color[v] = c;

        if (c > nr_col) {
            nr_col = c;
        }
    }

    return nr_col + 1;
}

int main(void)
{
    Graph g;
    int color[NMAX];

    reading(&g);

    int nr_col = dsatur(&g, color);

    printf("%d\n", nr_col);

    for (int i = 0; i < g.n; i++) {
        if (i > 0) {
            printf(" ");
        }
        printf("%d", color[i]);
    }
    printf("\n");
    return 0;
}
