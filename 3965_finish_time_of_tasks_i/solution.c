// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

#include <stdlib.h>

static int** g3965;
static int* deg3965;
static int* base3965;

static long long dfs3965(int i) {
    if (deg3965[i] == 0) return base3965[i];
    long long INF = 1LL << 62;
    long long earliest = INF, latest = -INF;
    for (int j = 0; j < deg3965[i]; j++) {
        long long a = dfs3965(g3965[i][j]);
        if (a < earliest) earliest = a;
        if (a > latest) latest = a;
    }
    long long ownDuration = (latest - earliest) + base3965[i];
    return latest + ownDuration;
}

long long finishTime(int n, int** edges, int edgesSize, int* edgesColSize, int* baseTime, int baseTimeSize) {
    (void)edgesColSize; (void)baseTimeSize;
    g3965 = calloc((size_t)n, sizeof(int*));
    deg3965 = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    base3965 = baseTime;
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (deg3965[a] == cap[a]) { cap[a] = cap[a] ? cap[a] * 2 : 4; g3965[a] = realloc(g3965[a], (size_t)cap[a] * sizeof(int)); }
        g3965[a][deg3965[a]++] = b;
    }
    long long ans = dfs3965(0);
    for (int i = 0; i < n; i++) free(g3965[i]);
    free(g3965); free(deg3965); free(cap);
    return ans;
}
