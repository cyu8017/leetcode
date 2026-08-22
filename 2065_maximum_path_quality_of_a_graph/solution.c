// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

#include <stdlib.h>

static int ans2065, maxTime2065, *values2065, n2065;
static int** g2065; static int* gc2065; static int** gw2065;
static int* vis2065;

static void dfs2065(int u, int time, int quality) {
    if (time > maxTime2065) return;
    int first = vis2065[u] == 0;
    if (first) quality += values2065[u];
    vis2065[u]++;
    if (u == 0 && quality > ans2065) ans2065 = quality;
    for (int i = 0; i < gc2065[u]; i++) dfs2065(g2065[u][i], time + gw2065[u][i], quality);
    vis2065[u]--;
}

int maximalPathQuality(int* values, int valuesSize, int** edges, int edgesSize, int* edgesColSize, int maxTime) {
    (void)edgesColSize;
    n2065 = valuesSize; values2065 = values; maxTime2065 = maxTime; ans2065 = 0;
    int* deg = (int*)calloc((size_t)n2065, sizeof(int));
    for (int i = 0; i < edgesSize; i++) { deg[edges[i][0]]++; deg[edges[i][1]]++; }
    g2065 = (int**)malloc((size_t)n2065 * sizeof(int*));
    gw2065 = (int**)malloc((size_t)n2065 * sizeof(int*));
    gc2065 = (int*)calloc((size_t)n2065, sizeof(int));
    for (int i = 0; i < n2065; i++) {
        g2065[i] = (int*)malloc((size_t)(deg[i] ? deg[i] : 1) * sizeof(int));
        gw2065[i] = (int*)malloc((size_t)(deg[i] ? deg[i] : 1) * sizeof(int));
    }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1], w = edges[i][2];
        g2065[a][gc2065[a]] = b; gw2065[a][gc2065[a]++] = w;
        g2065[b][gc2065[b]] = a; gw2065[b][gc2065[b]++] = w;
    }
    vis2065 = (int*)calloc((size_t)n2065, sizeof(int));
    dfs2065(0, 0, 0);
    for (int i = 0; i < n2065; i++) { free(g2065[i]); free(gw2065[i]); }
    free(g2065); free(gw2065); free(gc2065); free(deg); free(vis2065);
    return ans2065;
}
