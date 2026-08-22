// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

#include <stdlib.h>

static int** g2538;
static int* deg2538;
static int* cap2538;
static int* price2538;
static long long ans2538;

static void add2538(int a, int b) {
    if (deg2538[a] == cap2538[a]) {
        cap2538[a] = cap2538[a] ? cap2538[a] * 2 : 4;
        g2538[a] = (int*)realloc(g2538[a], (size_t)cap2538[a] * sizeof(int));
    }
    g2538[a][deg2538[a]++] = b;
}

static long long dfs2538(int u, int p) {
    long long maxChild = 0;
    for (int i = 0; i < deg2538[u]; i++) {
        int v = g2538[u][i];
        if (v == p) continue;
        long long child = dfs2538(v, u);
        if (child > maxChild) maxChild = child;
        if (child > ans2538) ans2538 = child;
    }
    return (long long)price2538[u] + maxChild;
}

long long maxOutput(int n, int** edges, int edgesSize, int* edgesColSize, int* price, int priceSize) {
    (void)edgesColSize; (void)priceSize;
    g2538 = (int**)calloc((size_t)n, sizeof(int*));
    deg2538 = (int*)calloc((size_t)n, sizeof(int));
    cap2538 = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        add2538(edges[i][0], edges[i][1]);
        add2538(edges[i][1], edges[i][0]);
    }
    price2538 = price;
    ans2538 = 0;
    dfs2538(0, -1);
    long long result = ans2538;
    for (int i = 0; i < n; i++) free(g2538[i]);
    free(g2538); free(deg2538); free(cap2538);
    return result;
}
