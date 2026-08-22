// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

#include <stdlib.h>
#include <string.h>

int maxWeight(int n, int** edges, int edgesSize, int* edgesColSize, int k, int t) {
    (void)edgesColSize;
    int** gto = (int**)calloc((size_t)n, sizeof(int*));
    int** gw = (int**)calloc((size_t)n, sizeof(int*));
    int* gsz = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        if (gsz[u] == gcap[u]) {
            gcap[u] = gcap[u] ? gcap[u] * 2 : 2;
            gto[u] = realloc(gto[u], (size_t)gcap[u] * sizeof(int));
            gw[u] = realloc(gw[u], (size_t)gcap[u] * sizeof(int));
        }
        gto[u][gsz[u]] = v; gw[u][gsz[u]] = w; gsz[u]++;
    }
    /* dp[u][i] = list of sums - use bitsets if t small else dynamic arrays */
    int*** sums = (int***)malloc((size_t)n * sizeof(int**));
    int** ssz = (int**)malloc((size_t)n * sizeof(int*));
    int** scap = (int**)malloc((size_t)n * sizeof(int*));
    for (int u = 0; u < n; u++) {
        sums[u] = (int**)calloc((size_t)(k + 1), sizeof(int*));
        ssz[u] = (int*)calloc((size_t)(k + 1), sizeof(int));
        scap[u] = (int*)calloc((size_t)(k + 1), sizeof(int));
        sums[u][0] = (int*)malloc(sizeof(int));
        sums[u][0][0] = 0;
        ssz[u][0] = 1;
        scap[u][0] = 1;
    }
    for (int i = 0; i < k; i++) {
        for (int u = 0; u < n; u++) {
            for (int si = 0; si < ssz[u][i]; si++) {
                int sum = sums[u][i][si];
                for (int ei = 0; ei < gsz[u]; ei++) {
                    int ns = sum + gw[u][ei];
                    int v = gto[u][ei];
                    if (ns < t) {
                        /* add unique */
                        int found = 0;
                        for (int z = 0; z < ssz[v][i + 1]; z++) if (sums[v][i + 1][z] == ns) { found = 1; break; }
                        if (!found) {
                            if (ssz[v][i + 1] == scap[v][i + 1]) {
                                scap[v][i + 1] = scap[v][i + 1] ? scap[v][i + 1] * 2 : 4;
                                sums[v][i + 1] = realloc(sums[v][i + 1], (size_t)scap[v][i + 1] * sizeof(int));
                            }
                            sums[v][i + 1][ssz[v][i + 1]++] = ns;
                        }
                    }
                }
            }
        }
    }
    int ans = -1;
    for (int u = 0; u < n; u++)
        for (int z = 0; z < ssz[u][k]; z++)
            if (sums[u][k][z] > ans) ans = sums[u][k][z];
    for (int u = 0; u < n; u++) {
        for (int i = 0; i <= k; i++) free(sums[u][i]);
        free(sums[u]); free(ssz[u]); free(scap[u]);
        free(gto[u]); free(gw[u]);
    }
    free(sums); free(ssz); free(scap); free(gto); free(gw); free(gsz); free(gcap);
    return ans;
}
