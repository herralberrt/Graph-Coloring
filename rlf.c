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
        if (g->mat[v][i]) {
            degree++;
        }
    }
    return degree;
}

// Checking if vertex v is adjacent to any vertex in vert_set
int checking_adjacent(Graph *g, int v, int *vert_set)
{
    for (int i = 0; i < g->n; i++) {
        if (vert_set[i] && g->mat[v][i]) {
            return 1;
        }
    }
    return 0;
}

// RLF algorithm
int rlf(Graph *g, int *color)
{
    int uncolored[NMAX], vert_set[NMAX];

    for (int i = 0; i < g->n; i++) {
        color[i] = -1;
        uncolored[i] = 1;
    }

    int current_color = 0;

    while (1) {
        int start = -1;
        int max_deg = -1;

        // Finding the uncolored vertex with maximum degree
        for (int i = 0; i < g->n; i++) {
            if (uncolored[i]) {
                int d = degree(g, i);
                if (d > max_deg) {
                    max_deg = d;
                    start = i;
                }
            }
        }

        if (start == -1) {
            break;
        }

        // Initializing vert_set
        for (int i = 0; i < g->n; i++) {
            vert_set[i] = 0;
        }

        vert_set[start] = 1;
        color[start] = current_color;
        uncolored[start] = 0;

        // Go on adding vertices to vert_set
        int changed = 1;
        while (changed) {
            changed = 0;
            int best = -1;
            int best_score = -1;

            for (int v = 0; v < g->n; v++) {
                if (uncolored[v] && !checking_adjacent(g, v, vert_set)) {
                    int score = 0;
                    for (int u = 0; u < g->n; u++) {
                        if (uncolored[u] && g->mat[v][u]) {
                            score++;
                        }
                    }

                    if (score > best_score) {
                        best_score = score;
                        best = v;
                    }
                }
            }

            if (best != -1) {
                vert_set[best] = 1;
                color[best] = current_color;
                uncolored[best] = 0;
                changed = 1;
            }
        }
        
        // Moving to the next color
        current_color++;
    }

    return current_color;
}

int main(void)
{
    Graph g;
    int color[NMAX];

    reading(&g);

    int k = rlf(&g, color);
    printf("%d\n", k);

    for (int i = 0; i < g.n; i++) {
        if (i > 0) printf(" ");
        printf("%d", color[i]);
    }
    printf("\n");
    return 0;
}
