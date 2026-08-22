// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

#include <stdlib.h>

static int **g3203, *glen3203, *gcap3203, ans3203, a3203;

static void add3203(int u, int v) {
    if (glen3203[u] == gcap3203[u]) {
        gcap3203[u] = gcap3203[u] ? gcap3203[u] * 2 : 4;
        g3203[u] = realloc(g3203[u], gcap3203[u] * sizeof(int));
    }
    g3203[u][glen3203[u]++] = v;
}

static void dfs3203(int i, int fa, int t) {
    for (int x = 0; x < glen3203[i]; x++) {
        int j = g3203[i][x];
        if (j != fa) dfs3203(j, i, t + 1);
    }
    if (ans3203 < t) { ans3203 = t; a3203 = i; }
}

static int treeDiameter(int** edges, int edgesSize) {
    int n = edgesSize + 1;
    g3203 = calloc(n, sizeof(int*));
    glen3203 = calloc(n, sizeof(int));
    gcap3203 = calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        add3203(edges[i][0], edges[i][1]);
        add3203(edges[i][1], edges[i][0]);
    }
    ans3203 = 0; a3203 = 0;
    dfs3203(0, -1, 0);
    dfs3203(a3203, -1, 0);
    int res = ans3203;
    for (int i = 0; i < n; i++) free(g3203[i]);
    free(g3203); free(glen3203); free(gcap3203);
    return res;
}

static int max3203(int a, int b) { return a > b ? a : b; }

int minimumDiameterAfterMerge(int** edges1, int edges1Size, int* edges1ColSize, int** edges2, int edges2Size, int* edges2ColSize) {
    (void)edges1ColSize; (void)edges2ColSize;
    int d1 = treeDiameter(edges1, edges1Size);
    int d2 = treeDiameter(edges2, edges2Size);
    int t = (d1 + 1) / 2 + (d2 + 1) / 2 + 1;
    return max3203(d1, max3203(d2, t));
}
