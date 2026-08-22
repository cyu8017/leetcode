// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

#include <stdlib.h>

typedef struct { int x, w; } Pair;
static Pair** g3067;
static int* gsz3067;
static int signal3067;

static int dfs3067(int a, int fa, int ws) {
    int cnt = (ws % signal3067 == 0);
    for (int i = 0; i < gsz3067[a]; i++) {
        int b = g3067[a][i].x, w = g3067[a][i].w;
        if (b != fa) cnt += dfs3067(b, a, ws + w);
    }
    return cnt;
}

int* countPairsOfConnectableServers(int** edges, int edgesSize, int* edgesColSize, int signalSpeed, int* returnSize) {
    (void)edgesColSize;
    int n = edgesSize + 1;
    signal3067 = signalSpeed;
    g3067 = (Pair**)calloc((size_t)n, sizeof(Pair*));
    gsz3067 = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1], w = edges[i][2];
        if (gsz3067[a] == cap[a]) { cap[a] = cap[a] ? cap[a]*2 : 2; g3067[a] = (Pair*)realloc(g3067[a], (size_t)cap[a]*sizeof(Pair)); }
        if (gsz3067[b] == cap[b]) { cap[b] = cap[b] ? cap[b]*2 : 2; g3067[b] = (Pair*)realloc(g3067[b], (size_t)cap[b]*sizeof(Pair)); }
        g3067[a][gsz3067[a]++] = (Pair){b, w};
        g3067[b][gsz3067[b]++] = (Pair){a, w};
    }
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    for (int a = 0; a < n; a++) {
        int s = 0;
        for (int i = 0; i < gsz3067[a]; i++) {
            int t = dfs3067(g3067[a][i].x, a, g3067[a][i].w);
            ans[a] += s * t;
            s += t;
        }
    }
    for (int i = 0; i < n; i++) free(g3067[i]);
    free(g3067); free(gsz3067); free(cap);
    *returnSize = n;
    return ans;
}
