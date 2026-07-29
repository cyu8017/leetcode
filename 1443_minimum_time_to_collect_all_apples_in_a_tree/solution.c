// LeetCode 1443 - Minimum Time to Collect All Apples in a Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

#include <stdlib.h>
#include <stdbool.h>

static int visit(int node, int parent, int** graph, int* gSize, bool* hasApple) {
    int cost = 0;
    for (int i = 0; i < gSize[node]; i++) {
        int child = graph[node][i];
        if (child == parent) continue;
        int child_cost = visit(child, node, graph, gSize, hasApple);
        if (child_cost || hasApple[child]) cost += child_cost + 2;
    }
    return cost;
}

int minTime(int n, int** edges, int edgesSize, int* edgesColSize, bool* hasApple, int hasAppleSize) {
    (void)edgesColSize; (void)hasAppleSize;
    int** graph = (int**)malloc(n * sizeof(int*));
    int* gSize = (int*)calloc(n, sizeof(int));
    int* gCap = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) { gCap[i] = 4; graph[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (gSize[a] == gCap[a]) { gCap[a] *= 2; graph[a] = (int*)realloc(graph[a], gCap[a] * sizeof(int)); }
        if (gSize[b] == gCap[b]) { gCap[b] *= 2; graph[b] = (int*)realloc(graph[b], gCap[b] * sizeof(int)); }
        graph[a][gSize[a]++] = b;
        graph[b][gSize[b]++] = a;
    }
    int ans = visit(0, -1, graph, gSize, hasApple);
    for (int i = 0; i < n; i++) free(graph[i]);
    free(graph); free(gSize); free(gCap);
    return ans;
}
