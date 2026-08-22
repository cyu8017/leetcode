// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

#include <stdlib.h>

#define LOG3553 17

static int** parent3553;
static int* depth3553;
static int* dist3553;

static int lca3553(int u, int v) {
    if (depth3553[u] < depth3553[v]) {
        int t = u;
        u = v;
        v = t;
    }
    for (int k = LOG3553 - 1; k >= 0; k--) {
        if (parent3553[k][u] != -1 && depth3553[parent3553[k][u]] >= depth3553[v]) {
            u = parent3553[k][u];
        }
    }
    if (u == v) return u;
    for (int k = LOG3553 - 1; k >= 0; k--) {
        if (parent3553[k][u] != -1 && parent3553[k][u] != parent3553[k][v]) {
            u = parent3553[k][u];
            v = parent3553[k][v];
        }
    }
    return parent3553[0][u];
}

static int path3553(int u, int v) {
    int a = lca3553(u, v);
    return dist3553[u] + dist3553[v] - 2 * dist3553[a];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minimumWeight(int** edges, int edgesSize, int* edgesColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)edgesColSize;
    (void)queriesColSize;
    int n = edgesSize + 1;
    int** gto = (int**)calloc((size_t)n, sizeof(int*));
    int** gw = (int**)calloc((size_t)n, sizeof(int*));
    int* gsz = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        for (int rep = 0; rep < 2; rep++) {
            int a = rep ? v : u, b = rep ? u : v;
            if (gsz[a] == gcap[a]) {
                gcap[a] = gcap[a] ? gcap[a] * 2 : 2;
                gto[a] = (int*)realloc(gto[a], (size_t)gcap[a] * sizeof(int));
                gw[a] = (int*)realloc(gw[a], (size_t)gcap[a] * sizeof(int));
            }
            gto[a][gsz[a]] = b;
            gw[a][gsz[a]] = w;
            gsz[a]++;
        }
    }
    parent3553 = (int**)malloc((size_t)LOG3553 * sizeof(int*));
    for (int i = 0; i < LOG3553; i++) {
        parent3553[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) parent3553[i][j] = -1;
    }
    depth3553 = (int*)calloc((size_t)n, sizeof(int));
    dist3553 = (int*)calloc((size_t)n, sizeof(int));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int* sp = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    stack[top] = 0;
    sp[top] = -1;
    top++;
    while (top) {
        top--;
        int u = stack[top], p = sp[top];
        parent3553[0][u] = p;
        for (int i = 0; i < gsz[u]; i++) {
            int v = gto[u][i];
            if (v == p) continue;
            depth3553[v] = depth3553[u] + 1;
            dist3553[v] = dist3553[u] + gw[u][i];
            stack[top] = v;
            sp[top] = u;
            top++;
        }
    }
    for (int k = 1; k < LOG3553; k++) {
        for (int v = 0; v < n; v++) {
            if (parent3553[k - 1][v] != -1) {
                parent3553[k][v] = parent3553[k - 1][parent3553[k - 1][v]];
            }
        }
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int a = queries[i][0], b = queries[i][1], c = queries[i][2];
        ans[i] = (path3553(a, b) + path3553(b, c) + path3553(a, c)) / 2;
    }
    for (int i = 0; i < n; i++) {
        free(gto[i]);
        free(gw[i]);
    }
    free(gto);
    free(gw);
    free(gsz);
    free(gcap);
    for (int i = 0; i < LOG3553; i++) free(parent3553[i]);
    free(parent3553);
    free(depth3553);
    free(dist3553);
    free(stack);
    free(sp);
    *returnSize = queriesSize;
    return ans;
}
