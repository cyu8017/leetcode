// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

#include <stdlib.h>
#include <string.h>

#define LOG 17

static int* H;
static int* TO;
static int* NX;
static int UP[LOG][100005];
static int DEPTH[100005];
static int Nglob;

static void dfs_lca(int u, int p) {
    UP[0][u] = p;
    for (int e = H[u]; e != -1; e = NX[e]) {
        int v = TO[e];
        if (v != p) {
            DEPTH[v] = DEPTH[u] + 1;
            dfs_lca(v, u);
        }
    }
}

static int lift(int v, int d) {
    for (int k = 0; k < LOG; k++) if ((d >> k) & 1) v = UP[k][v];
    return v;
}

static int lca(int a, int b) {
    if (DEPTH[a] < DEPTH[b]) { int t = a; a = b; b = t; }
    a = lift(a, DEPTH[a] - DEPTH[b]);
    if (a == b) return a;
    for (int k = LOG - 1; k >= 0; k--) {
        if (UP[k][a] != UP[k][b]) {
            a = UP[k][a];
            b = UP[k][b];
        }
    }
    return UP[0][a];
}

static int dist(int a, int b) {
    int c = lca(a, b);
    return DEPTH[a] + DEPTH[b] - 2 * DEPTH[c];
}

int* closestNode(int n, int** edges, int edgesSize, int* edgesColSize, int** query, int querySize, int* queryColSize, int* returnSize) {
    (void)edgesColSize; (void)queryColSize;
    Nglob = n;
    H = (int*)malloc((size_t)n * sizeof(int));
    memset(H, -1, (size_t)n * sizeof(int));
    TO = (int*)malloc((size_t)edgesSize * 2 * sizeof(int));
    NX = (int*)malloc((size_t)edgesSize * 2 * sizeof(int));
    int ec = 0;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        TO[ec] = v; NX[ec] = H[u]; H[u] = ec++;
        TO[ec] = u; NX[ec] = H[v]; H[v] = ec++;
    }
    DEPTH[0] = 0;
    dfs_lca(0, 0);
    for (int k = 1; k < LOG; k++)
        for (int v = 0; v < n; v++)
            UP[k][v] = UP[k - 1][UP[k - 1][v]];
    int* ans = (int*)malloc((size_t)querySize * sizeof(int));
    for (int i = 0; i < querySize; i++) {
        int a = query[i][0], b = query[i][1], x = query[i][2];
        int cands[3] = {lca(a, b), lca(a, x), lca(b, x)};
        int best = cands[0], bestD = dist(cands[0], x);
        for (int t = 1; t < 3; t++) {
            int d = dist(cands[t], x);
            if (d < bestD) { bestD = d; best = cands[t]; }
        }
        ans[i] = best;
    }
    free(H); free(TO); free(NX);
    *returnSize = querySize;
    return ans;
}
