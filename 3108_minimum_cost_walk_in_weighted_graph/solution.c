// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

#include <stdlib.h>

typedef struct { int *p, *size; } UF;
static UF* uf_new(int n) {
    UF* uf = (UF*)malloc(sizeof(UF));
    uf->p = (int*)malloc((size_t)n * sizeof(int));
    uf->size = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { uf->p[i] = i; uf->size[i] = 1; }
    return uf;
}
static int uf_find(UF* uf, int x) {
    if (uf->p[x] != x) uf->p[x] = uf_find(uf, uf->p[x]);
    return uf->p[x];
}
static void uf_union(UF* uf, int a, int b) {
    int pa = uf_find(uf, a), pb = uf_find(uf, b);
    if (pa == pb) return;
    if (uf->size[pa] > uf->size[pb]) { uf->p[pb] = pa; uf->size[pa] += uf->size[pb]; }
    else { uf->p[pa] = pb; uf->size[pb] += uf->size[pa]; }
}

int* minimumCost(int n, int** edges, int edgesSize, int* edgesColSize, int** query, int querySize, int* queryColSize, int* returnSize) {
    (void)edgesColSize; (void)queryColSize;
    UF* uf = uf_new(n);
    int* g = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) g[i] = -1;
    for (int i = 0; i < edgesSize; i++) uf_union(uf, edges[i][0], edges[i][1]);
    for (int i = 0; i < edgesSize; i++) {
        int root = uf_find(uf, edges[i][0]);
        g[root] &= edges[i][2];
    }
    int* ans = (int*)malloc((size_t)querySize * sizeof(int));
    for (int i = 0; i < querySize; i++) {
        int u = query[i][0], v = query[i][1];
        if (u == v) ans[i] = 0;
        else {
            int a = uf_find(uf, u), b = uf_find(uf, v);
            ans[i] = (a == b) ? g[a] : -1;
        }
    }
    free(uf->p); free(uf->size); free(uf); free(g);
    *returnSize = querySize;
    return ans;
}
