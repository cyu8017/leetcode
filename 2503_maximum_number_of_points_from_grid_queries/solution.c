// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct { int r, c, v; } Cell2503;
typedef struct { int idx, q; } Q2503;

static void push2503(Cell2503* h, int* n, Cell2503 x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].v <= h[i].v) break;
        Cell2503 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static Cell2503 pop2503(Cell2503* h, int* n) {
    Cell2503 res = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = i * 2 + 1, r = l + 1, best = i;
        if (l < *n && h[l].v < h[best].v) best = l;
        if (r < *n && h[r].v < h[best].v) best = r;
        if (best == i) break;
        Cell2503 t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return res;
}

static int cmpQ(const void* a, const void* b) {
    return ((const Q2503*)a)->q - ((const Q2503*)b)->q;
}

int* maxPoints(int** grid, int gridSize, int* gridColSize, int* queries, int queriesSize, int* returnSize) {
    int m = gridSize, n = gridColSize[0];
    Q2503* order = (Q2503*)malloc((size_t)queriesSize * sizeof(Q2503));
    for (int i = 0; i < queriesSize; i++) { order[i].idx = i; order[i].q = queries[i]; }
    qsort(order, (size_t)queriesSize, sizeof(Q2503), cmpQ);
    int* ans = (int*)calloc((size_t)queriesSize, sizeof(int));
    bool** visited = (bool**)malloc((size_t)m * sizeof(bool*));
    for (int i = 0; i < m; i++) visited[i] = (bool*)calloc((size_t)n, sizeof(bool));
    Cell2503* heap = (Cell2503*)malloc((size_t)(m * n + 5) * sizeof(Cell2503));
    int hn = 0;
    push2503(heap, &hn, (Cell2503){0, 0, grid[0][0]});
    visited[0][0] = true;
    int points = 0;
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    for (int oi = 0; oi < queriesSize; oi++) {
        int q = order[oi].q;
        while (hn > 0 && heap[0].v < q) {
            Cell2503 cur = pop2503(heap, &hn);
            points++;
            for (int d = 0; d < 4; d++) {
                int nr = cur.r + dirs[d][0], nc = cur.c + dirs[d][1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    push2503(heap, &hn, (Cell2503){nr, nc, grid[nr][nc]});
                }
            }
        }
        ans[order[oi].idx] = points;
    }
    for (int i = 0; i < m; i++) free(visited[i]);
    free(visited); free(heap); free(order);
    *returnSize = queriesSize;
    return ans;
}
