// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

#include <stdlib.h>

typedef struct { int to, w; } Edge;
typedef struct { long long without, with; } Pair;

static Pair dfs(Edge** g, int* gs, int u, int p) {
    long long base = 0, bestGain = 0;
    for (int i = 0; i < gs[u]; i++) {
        Edge e = g[u][i];
        if (e.to == p) continue;
        Pair child = dfs(g, gs, e.to, u);
        base += child.without;
        long long gain = child.with + e.w - child.without;
        if (gain > bestGain) bestGain = gain;
    }
    return (Pair){base + bestGain, base};
}

long long maxScore(int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = edgesSize + 1;
    Edge** g = (Edge**)calloc((size_t)n, sizeof(Edge*));
    int* gs = (int*)calloc((size_t)n, sizeof(int));
    int* gc = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) {
        int p = edges[i - 1][0], w = edges[i - 1][1];
        if (gs[p] == gc[p]) { gc[p] = gc[p] ? gc[p]*2 : 2; g[p] = (Edge*)realloc(g[p], (size_t)gc[p]*sizeof(Edge)); }
        if (gs[i] == gc[i]) { gc[i] = gc[i] ? gc[i]*2 : 2; g[i] = (Edge*)realloc(g[i], (size_t)gc[i]*sizeof(Edge)); }
        g[p][gs[p]++] = (Edge){i, w};
        g[i][gs[i]++] = (Edge){p, w};
    }
    Pair ans = dfs(g, gs, 0, -1);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gs); free(gc);
    return ans.without;
}
