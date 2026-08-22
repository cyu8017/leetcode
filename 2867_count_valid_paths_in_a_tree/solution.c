// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int dfs_comp(int** g, int* gsz, bool* isPrime, int u, int p) {
    if (isPrime[u]) return 0;
    int sz = 1;
    for (int i = 0; i < gsz[u]; i++) {
        int v = g[u][i];
        if (v != p) sz += dfs_comp(g, gsz, isPrime, v, u);
    }
    return sz;
}

long long countPaths(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    bool* isPrime = (bool*)calloc(n + 1, sizeof(bool));
    for (int i = 2; i <= n; i++) isPrime[i] = true;
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) isPrime[j] = false;
        }
    }
    int** g = (int**)calloc(n + 1, sizeof(int*));
    int* gsz = (int*)calloc(n + 1, sizeof(int));
    int* gcap = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (gsz[u] == gcap[u]) { gcap[u] = gcap[u] ? gcap[u]*2 : 4; g[u] = (int*)realloc(g[u], gcap[u]*sizeof(int)); }
        g[u][gsz[u]++] = v;
        if (gsz[v] == gcap[v]) { gcap[v] = gcap[v] ? gcap[v]*2 : 4; g[v] = (int*)realloc(g[v], gcap[v]*sizeof(int)); }
        g[v][gsz[v]++] = u;
    }
    long long ans = 0;
    for (int u = 1; u <= n; u++) {
        if (!isPrime[u]) continue;
        long long total = 0;
        for (int i = 0; i < gsz[u]; i++) {
            int c = dfs_comp(g, gsz, isPrime, g[u][i], u);
            ans += c;
            ans += total * c;
            total += c;
        }
    }
    for (int i = 0; i <= n; i++) free(g[i]);
    free(g); free(gsz); free(gcap); free(isPrime);
    return ans;
}
