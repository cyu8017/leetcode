// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static void dfs3310(int u, int** g, int* glen, bool* sus) {
    if (sus[u]) return;
    sus[u] = true;
    for (int i = 0; i < glen[u]; i++) dfs3310(g[u][i], g, glen, sus);
}

int* remainingMethods(int n, int k, int** invocations, int invocationsSize, int* invocationsColSize, int* returnSize) {
    (void)invocationsColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* glen = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { gcap[i] = 4; g[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < invocationsSize; i++) {
        int a = invocations[i][0], b = invocations[i][1];
        if (glen[a] == gcap[a]) { gcap[a] *= 2; g[a] = realloc(g[a], (size_t)gcap[a] * sizeof(int)); }
        g[a][glen[a]++] = b;
    }
    bool* sus = (bool*)calloc((size_t)n, sizeof(bool));
    dfs3310(k, g, glen, sus);
    for (int i = 0; i < invocationsSize; i++) {
        if (!sus[invocations[i][0]] && sus[invocations[i][1]]) {
            int* ans = (int*)malloc((size_t)n * sizeof(int));
            for (int j = 0; j < n; j++) ans[j] = j;
            *returnSize = n;
            for (int j = 0; j < n; j++) free(g[j]);
            free(g); free(glen); free(gcap); free(sus);
            return ans;
        }
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int an = 0;
    for (int i = 0; i < n; i++) if (!sus[i]) ans[an++] = i;
    *returnSize = an;
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(glen); free(gcap); free(sus);
    return ans;
}
