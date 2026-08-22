// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

#include <stdlib.h>
#include <string.h>

typedef struct { int v, w; } Edge;

static void dfs1(Edge** g, int* gsz, int u, int p, int* ans0) {
    for (int i = 0; i < gsz[u]; i++) {
        int v = g[u][i].v, ww = g[u][i].w;
        if (v == p) continue;
        *ans0 += ww;
        dfs1(g, gsz, v, u, ans0);
    }
}

static void dfs2(Edge** g, int* gsz, int u, int p, int* ans) {
    for (int i = 0; i < gsz[u]; i++) {
        int v = g[u][i].v, ww = g[u][i].w;
        if (v == p) continue;
        if (ww == 0) ans[v] = ans[u] + 1;
        else ans[v] = ans[u] - 1;
        dfs2(g, gsz, v, u, ans);
    }
}

int* minEdgeReversals(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    Edge** g = (Edge**)calloc(n, sizeof(Edge*));
    int* gsz = (int*)calloc(n, sizeof(int));
    int* gcap = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (gsz[u] == gcap[u]) { gcap[u] = gcap[u] ? gcap[u]*2 : 4; g[u] = (Edge*)realloc(g[u], gcap[u]*sizeof(Edge)); }
        g[u][gsz[u]++] = (Edge){v, 0};
        if (gsz[v] == gcap[v]) { gcap[v] = gcap[v] ? gcap[v]*2 : 4; g[v] = (Edge*)realloc(g[v], gcap[v]*sizeof(Edge)); }
        g[v][gsz[v]++] = (Edge){u, 1};
    }
    int* ans = (int*)calloc(n, sizeof(int));
    dfs1(g, gsz, 0, -1, &ans[0]);
    dfs2(g, gsz, 0, -1, ans);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap);
    *returnSize = n;
    return ans;
}
