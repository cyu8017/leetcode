// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

#include <stdlib.h>
#include <string.h>

typedef struct { int node, time; } MarkNode;
typedef struct { MarkNode top1, top2; } Top2;

static int getTime3241(int u) { return (u % 2 == 0) ? 2 : 1; }

static int dfs3241(int u, int prev, int** tree, int* tlen, Top2* dp) {
    MarkNode t1 = {0, 0}, t2 = {0, 0};
    for (int i = 0; i < tlen[u]; i++) {
        int v = tree[u][i];
        if (v == prev) continue;
        int t = dfs3241(v, u, tree, tlen, dp) + getTime3241(v);
        if (t >= t1.time) { t2 = t1; t1.node = v; t1.time = t; }
        else if (t > t2.time) { t2.node = v; t2.time = t; }
    }
    dp[u].top1 = t1; dp[u].top2 = t2;
    return t1.time;
}

static void reroot3241(int u, int prev, int maxTime, int** tree, int* tlen, Top2* dp, int* ans) {
    ans[u] = maxTime;
    if (dp[u].top1.time > ans[u]) ans[u] = dp[u].top1.time;
    for (int i = 0; i < tlen[u]; i++) {
        int v = tree[u][i];
        if (v == prev) continue;
        int side = dp[u].top1.time;
        if (dp[u].top1.node == v) side = dp[u].top2.time;
        int newMax = maxTime > side ? maxTime : side;
        reroot3241(v, u, getTime3241(u) + newMax, tree, tlen, dp, ans);
    }
}

int* timeTaken(int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    int n = edgesSize + 1;
    int** tree = (int**)calloc((size_t)n, sizeof(int*));
    int* tcap = (int*)calloc((size_t)n, sizeof(int));
    int* tlen = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) { tcap[i] = 4; tree[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (tlen[u] == tcap[u]) { tcap[u] *= 2; tree[u] = (int*)realloc(tree[u], (size_t)tcap[u] * sizeof(int)); }
        if (tlen[v] == tcap[v]) { tcap[v] *= 2; tree[v] = (int*)realloc(tree[v], (size_t)tcap[v] * sizeof(int)); }
        tree[u][tlen[u]++] = v;
        tree[v][tlen[v]++] = u;
    }
    Top2* dp = (Top2*)calloc((size_t)n, sizeof(Top2));
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    dfs3241(0, -1, tree, tlen, dp);
    reroot3241(0, -1, 0, tree, tlen, dp, ans);
    for (int i = 0; i < n; i++) free(tree[i]);
    free(tree); free(tcap); free(tlen); free(dp);
    *returnSize = n;
    return ans;
}
