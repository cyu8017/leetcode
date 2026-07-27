// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool dfs(int node, int destination, int** graph, int* graphSize, int* state) {
    if (graphSize[node] == 0) {
        return node == destination;
    }
    if (state[node] == 1) {
        return false;
    }
    if (state[node] == 2) {
        return true;
    }
    state[node] = 1;
    for (int i = 0; i < graphSize[node]; i++) {
        if (!dfs(graph[node][i], destination, graph, graphSize, state)) {
            return false;
        }
    }
    state[node] = 2;
    return true;
}

bool leadsToDestination(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination) {
    (void)edgesColSize;
    int** graph = (int**)malloc((size_t)n * sizeof(int*));
    int* graphSize = (int*)calloc((size_t)n, sizeof(int));
    int* graphCap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        graph[i] = NULL;
    }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0];
        int b = edges[i][1];
        if (graphSize[a] == graphCap[a]) {
            graphCap[a] = graphCap[a] == 0 ? 4 : graphCap[a] * 2;
            graph[a] = (int*)realloc(graph[a], (size_t)graphCap[a] * sizeof(int));
        }
        graph[a][graphSize[a]++] = b;
    }
    int* state = (int*)calloc((size_t)n, sizeof(int));
    bool ok = dfs(source, destination, graph, graphSize, state);
    for (int i = 0; i < n; i++) {
        free(graph[i]);
    }
    free(graph);
    free(graphSize);
    free(graphCap);
    free(state);
    return ok;
}
