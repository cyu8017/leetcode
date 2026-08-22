// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

#include <stdlib.h>
#include <string.h>

static int dfs(int u, int** g, int* gsz, char* s, int* ans) {
    int best1 = 0, best2 = 0;
    for (int i = 0; i < gsz[u]; i++) {
        int v = g[u][i];
        int lenV = dfs(v, g, gsz, s, ans);
        if (s[v] == s[u]) continue;
        if (lenV > best1) { best2 = best1; best1 = lenV; }
        else if (lenV > best2) best2 = lenV;
    }
    if (1 + best1 + best2 > *ans) *ans = 1 + best1 + best2;
    return 1 + best1;
}

int longestPath(int* parent, int parentSize, char* s) {
    int n = parentSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gsz = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) {
        int p = parent[i];
        if (gsz[p] == gcap[p]) {
            gcap[p] = gcap[p] ? gcap[p] * 2 : 4;
            g[p] = (int*)realloc(g[p], (size_t)gcap[p] * sizeof(int));
        }
        g[p][gsz[p]++] = i;
    }
    int ans = 1;
    dfs(0, g, gsz, s, &ans);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap);
    return ans;
}
