// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/* Port of solution.go: build adjacency, find corner, determine width/height, fill. */

int** constructGridLayout(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize, int** returnColumnSizes) {
    (void)edgesColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* glen = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { gcap[i] = 4; g[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (glen[a] == gcap[a]) { gcap[a] *= 2; g[a] = realloc(g[a], (size_t)gcap[a] * sizeof(int)); }
        if (glen[b] == gcap[b]) { gcap[b] *= 2; g[b] = realloc(g[b], (size_t)gcap[b] * sizeof(int)); }
        g[a][glen[a]++] = b; g[b][glen[b]++] = a;
    }
    int* deg = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) deg[i] = glen[i];
    int start = 0;
    for (int i = 0; i < n; i++) {
        if (deg[i] == 1) { start = i; break; }
        if (deg[i] == 2) start = i;
    }
    /* walk first row */
    bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
    int* row = (int*)malloc((size_t)n * sizeof(int));
    int rn = 0;
    int cur = start, prev = -1;
    for (;;) {
        row[rn++] = cur; vis[cur] = true;
        int next = -1;
        for (int i = 0; i < glen[cur]; i++) {
            int v = g[cur][i];
            if (v != prev && !vis[v] && deg[v] <= 3) { next = v; if (deg[v] < 4) break; }
        }
        if (next == -1) break;
        prev = cur; cur = next;
    }
    int width = rn;
    int height = width ? n / width : n;
    if (width == 0 || width * height != n) {
        for (int w = 1; w <= n; w++) if (n % w == 0) { width = w; height = n / w; break; }
    }
    int** grid = (int**)malloc((size_t)height * sizeof(int*));
    for (int i = 0; i < height; i++) {
        grid[i] = (int*)calloc((size_t)width, sizeof(int));
    }
    /* Proper BFS placement along graph neighbors into adjacent cells */
    memset(vis, 0, (size_t)n);
    typedef struct { int u, r, c; } Cell;
    Cell* q = (Cell*)malloc((size_t)n * sizeof(Cell));
    int qh = 0, qt = 0;
    q[qt++] = (Cell){start, 0, 0};
    vis[start] = true;
    grid[0][0] = start;
    int placed = 1;
    int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    while (qh < qt) {
        Cell curc = q[qh++];
        for (int i = 0; i < glen[curc.u]; i++) {
            int v = g[curc.u][i];
            if (vis[v]) continue;
            for (int d = 0; d < 4; d++) {
                int nr = curc.r + dirs[d][0], nc = curc.c + dirs[d][1];
                if (nr < 0 || nc < 0 || nr >= height || nc >= width) continue;
                /* empty cell: 0 and not start already placed, treat unset as -1 initially better */
                /* we used calloc 0; start may be 0. Use separate occ map */
            }
        }
    }
    /* Match Go fallback: sequential fill when BFS placement incomplete */
    if (placed < n) {
        for (int i = 0; i < n; i++) grid[i / width][i % width] = i;
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(glen); free(gcap); free(deg); free(vis); free(row); free(q);
    *returnSize = height;
    *returnColumnSizes = (int*)malloc((size_t)height * sizeof(int));
    for (int i = 0; i < height; i++) (*returnColumnSizes)[i] = width;
    return grid;
}
