// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

#include <stdlib.h>
#include <string.h>

typedef struct { int to, w; } E;
typedef struct { E* a; int n, cap; } Adj;
static void adj_push(Adj* g, int u, int to, int w) {
    if (g[u].n == g[u].cap) { g[u].cap = g[u].cap ? g[u].cap * 2 : 4; g[u].a = (E*)realloc(g[u].a, g[u].cap * sizeof(E)); }
    g[u].a[g[u].n++] = (E){to, w};
}

static Adj* G3425; static int* nums3425;
static int bestLen, bestNodes;
static int lastPos[100001]; static char lastSeen[100001];

static void dfs3425(int u, int p, int dist, int left, int* path, int plen) {
    int val = nums3425[u];
    int prevPos = lastPos[val]; int seen = lastSeen[val];
    lastPos[val] = plen; lastSeen[val] = 1;
    int newLeft = left;
    if (seen && prevPos >= left) newLeft = prevPos + 1;
    path[plen] = dist;
    int length = dist - path[newLeft];
    int nodes = plen + 1 - newLeft;
    if (length > bestLen || (length == bestLen && nodes < bestNodes)) { bestLen = length; bestNodes = nodes; }
    for (int i = 0; i < G3425[u].n; i++) {
        int v = G3425[u].a[i].to;
        if (v == p) continue;
        dfs3425(v, u, dist + G3425[u].a[i].w, newLeft, path, plen + 1);
    }
    if (seen) lastPos[val] = prevPos; else lastSeen[val] = 0;
}

int* longestSpecialPath(int** edges, int edgesSize, int* edgesColSize, int* nums, int numsSize, int* returnSize) {
    (void)edgesColSize;
    int n = numsSize;
    G3425 = (Adj*)calloc(n, sizeof(Adj)); nums3425 = nums;
    for (int i = 0; i < edgesSize; i++) {
        adj_push(G3425, edges[i][0], edges[i][1], edges[i][2]);
        adj_push(G3425, edges[i][1], edges[i][0], edges[i][2]);
    }
    bestLen = 0; bestNodes = 1;
    memset(lastSeen, 0, sizeof(lastSeen));
    int* path = (int*)malloc((n + 1) * sizeof(int));
    dfs3425(0, -1, 0, 0, path, 0);
    for (int i = 0; i < n; i++) free(G3425[i].a);
    free(G3425); free(path);
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = bestLen; ans[1] = bestNodes;
    *returnSize = 2;
    return ans;
}
