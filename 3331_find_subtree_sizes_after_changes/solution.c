// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

#include <stdlib.h>
#include <string.h>

static void dfs1(int u, int** g, int* glen, char* s, int* newParent, int* last) {
    int c = s[u] - 'a';
    int prev = last[c];
    if (prev != -1) newParent[u] = prev;
    last[c] = u;
    for (int i = 0; i < glen[u]; i++) dfs1(g[u][i], g, glen, s, newParent, last);
    last[c] = prev;
}

static int dfs2(int u, int** ng, int* nglen, int* ans) {
    int sz = 1;
    for (int i = 0; i < nglen[u]; i++) sz += dfs2(ng[u][i], ng, nglen, ans);
    ans[u] = sz;
    return sz;
}

int* findSubtreeSizes(int* parent, int parentSize, char* s, int* returnSize) {
    int n = parentSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* glen = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { gcap[i] = 4; g[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 1; i < n; i++) {
        int p = parent[i];
        if (glen[p] == gcap[p]) { gcap[p] *= 2; g[p] = realloc(g[p], (size_t)gcap[p] * sizeof(int)); }
        g[p][glen[p]++] = i;
    }
    int* newParent = (int*)malloc((size_t)n * sizeof(int));
    memcpy(newParent, parent, (size_t)n * sizeof(int));
    int last[26];
    for (int i = 0; i < 26; i++) last[i] = -1;
    dfs1(0, g, glen, s, newParent, last);
    int** ng = (int**)calloc((size_t)n, sizeof(int*));
    int* nglen = (int*)calloc((size_t)n, sizeof(int));
    int* ngcap = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { ngcap[i] = 4; ng[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 1; i < n; i++) {
        int p = newParent[i];
        if (nglen[p] == ngcap[p]) { ngcap[p] *= 2; ng[p] = realloc(ng[p], (size_t)ngcap[p] * sizeof(int)); }
        ng[p][nglen[p]++] = i;
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    dfs2(0, ng, nglen, ans);
    for (int i = 0; i < n; i++) { free(g[i]); free(ng[i]); }
    free(g); free(glen); free(gcap); free(ng); free(nglen); free(ngcap); free(newParent);
    *returnSize = n;
    return ans;
}
