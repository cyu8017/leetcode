// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

#include <stdlib.h>

static int msb3901(unsigned sub) {
    int n = 0;
    while (sub > 1) { sub >>= 1; n++; }
    return n;
}

int evenSumSubgraphs(int* nums, int numsSize, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = numsSize;
    int** g = calloc((size_t)n, sizeof(int*));
    int* deg = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (deg[a] == cap[a]) { cap[a] = cap[a] ? cap[a] * 2 : 4; g[a] = realloc(g[a], (size_t)cap[a] * sizeof(int)); }
        if (deg[b] == cap[b]) { cap[b] = cap[b] ? cap[b] * 2 : 4; g[b] = realloc(g[b], (size_t)cap[b] * sizeof(int)); }
        g[a][deg[a]++] = b;
        g[b][deg[b]++] = a;
    }
    int m = (1 << n) - 1;
    int ans = 0;
    int vis;
    int* stack = malloc((size_t)n * sizeof(int));
    for (int sub = 1; sub <= m; sub++) {
        int s = 0;
        for (int i = 0; i < n; i++) if ((sub >> i) & 1) s += nums[i];
        if (s % 2 != 0) continue;
        vis = m ^ sub;
        int start = msb3901((unsigned)sub);
        int sp = 0;
        stack[sp++] = start;
        vis |= 1 << start;
        while (sp) {
            int u = stack[--sp];
            for (int j = 0; j < deg[u]; j++) {
                int v = g[u][j];
                if (((vis >> v) & 1) == 0) {
                    vis |= 1 << v;
                    stack[sp++] = v;
                }
            }
        }
        if (vis == m) ans++;
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap); free(stack);
    return ans;
}
