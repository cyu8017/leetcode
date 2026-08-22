// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

#include <stdlib.h>

static int** g2477;
static int* deg2477;
static int* cap2477;
static int seats2477;
static long long ans2477;

static void add2477(int a, int b) {
    if (deg2477[a] == cap2477[a]) {
        cap2477[a] = cap2477[a] ? cap2477[a] * 2 : 4;
        g2477[a] = (int*)realloc(g2477[a], (size_t)cap2477[a] * sizeof(int));
    }
    g2477[a][deg2477[a]++] = b;
}

static int dfs2477(int u, int p) {
    int people = 1;
    for (int i = 0; i < deg2477[u]; i++) {
        int v = g2477[u][i];
        if (v != p) people += dfs2477(v, u);
    }
    if (u != 0) ans2477 += (people + seats2477 - 1) / seats2477;
    return people;
}

long long minimumFuelCost(int** roads, int roadsSize, int* roadsColSize, int seats) {
    (void)roadsColSize;
    int n = roadsSize + 1;
    g2477 = (int**)calloc((size_t)n, sizeof(int*));
    deg2477 = (int*)calloc((size_t)n, sizeof(int));
    cap2477 = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < roadsSize; i++) {
        add2477(roads[i][0], roads[i][1]);
        add2477(roads[i][1], roads[i][0]);
    }
    seats2477 = seats;
    ans2477 = 0;
    dfs2477(0, -1);
    long long result = ans2477;
    for (int i = 0; i < n; i++) free(g2477[i]);
    free(g2477); free(deg2477); free(cap2477);
    return result;
}
