// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

#include <stdlib.h>
#include <stdbool.h>

bool possibleBipartition(int n, int** dislikes, int dislikesSize, int* dislikesColSize) {
    (void)dislikesColSize;
    int** g = (int**)calloc((size_t)(n + 1), sizeof(int*));
    int* gsz = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* gcap = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < dislikesSize; i++) {
        int a = dislikes[i][0], b = dislikes[i][1];
        for (int t = 0; t < 2; t++) {
            int u = t ? b : a, v = t ? a : b;
            if (gsz[u] == gcap[u]) {
                gcap[u] = gcap[u] ? gcap[u] * 2 : 2;
                g[u] = (int*)realloc(g[u], (size_t)gcap[u] * sizeof(int));
            }
            g[u][gsz[u]++] = v;
        }
    }
    int* color = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) color[i] = -1;
    int* q = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int start = 1; start <= n; start++) {
        if (color[start] != -1) continue;
        int qh = 0, qt = 0;
        q[qt++] = start;
        color[start] = 0;
        while (qh < qt) {
            int node = q[qh++];
            for (int i = 0; i < gsz[node]; i++) {
                int nei = g[node][i];
                if (color[nei] == -1) {
                    color[nei] = color[node] ^ 1;
                    q[qt++] = nei;
                } else if (color[nei] == color[node]) {
                    for (int j = 0; j <= n; j++) free(g[j]);
                    free(g); free(gsz); free(gcap); free(color); free(q);
                    return false;
                }
            }
        }
    }
    for (int j = 0; j <= n; j++) free(g[j]);
    free(g); free(gsz); free(gcap); free(color); free(q);
    return true;
}
