// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

#include <stdlib.h>

static int dfs(int** g, int* gsz, int* values, int k, int u, int p, int* ans) {
    int sum = values[u] % k;
    for (int i = 0; i < gsz[u]; i++) {
        int v = g[u][i];
        if (v == p) continue;
        sum = (sum + dfs(g, gsz, values, k, v, u, ans)) % k;
    }
    if (sum == 0) (*ans)++;
    return sum;
}

int maxKDivisibleComponents(int n, int** edges, int edgesSize, int* edgesColSize, int* values, int valuesSize, int k) {
    (void)edgesColSize; (void)valuesSize;
    int** g = (int**)calloc(n, sizeof(int*));
    int* gsz = (int*)calloc(n, sizeof(int));
    int* gcap = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (gsz[u] == gcap[u]) { gcap[u] = gcap[u] ? gcap[u]*2 : 4; g[u] = (int*)realloc(g[u], gcap[u]*sizeof(int)); }
        g[u][gsz[u]++] = v;
        if (gsz[v] == gcap[v]) { gcap[v] = gcap[v] ? gcap[v]*2 : 4; g[v] = (int*)realloc(g[v], gcap[v]*sizeof(int)); }
        g[v][gsz[v]++] = u;
    }
    int ans = 0;
    dfs(g, gsz, values, k, 0, -1, &ans);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap);
    return ans;
}
