// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

#include <stdlib.h>

static int dfs3249(int a, int fa, int** g, int* glen, int* ans) {
    int pre = -1, cnt = 1, ok = 1;
    for (int i = 0; i < glen[a]; i++) {
        int b = g[a][i];
        if (b == fa) continue;
        int cur = dfs3249(b, a, g, glen, ans);
        cnt += cur;
        if (pre < 0) pre = cur;
        else if (pre != cur) ok = 0;
    }
    *ans += ok;
    return cnt;
}

int countGoodNodes(int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = edgesSize + 1;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* glen = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { gcap[i] = 4; g[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (glen[a] == gcap[a]) { gcap[a] *= 2; g[a] = realloc(g[a], (size_t)gcap[a] * sizeof(int)); }
        if (glen[b] == gcap[b]) { gcap[b] *= 2; g[b] = realloc(g[b], (size_t)gcap[b] * sizeof(int)); }
        g[a][glen[a]++] = b;
        g[b][glen[b]++] = a;
    }
    int ans = 0;
    dfs3249(0, -1, g, glen, &ans);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(glen); free(gcap);
    return ans;
}
