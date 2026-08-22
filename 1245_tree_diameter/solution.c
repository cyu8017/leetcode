// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

#include <stdlib.h>
#include <string.h>

static void farthest(
    int node,
    int dist,
    int** graph,
    int* graphSize,
    int* visited,
    int* outNode,
    int* outDist
) {
    visited[node] = 1;
    *outNode = node;
    *outDist = dist;
    for (int i = 0; i < graphSize[node]; i++) {
        int nxt = graph[node][i];
        if (!visited[nxt]) farthest(nxt, dist + 1, graph, graphSize, visited, outNode, outDist);
    }
}

int treeDiameter(int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    if (edgesSize == 0) return 0;
    int nodes = edgesSize + 1;
    int* graphSize = (int*)calloc((size_t)nodes, sizeof(int));
    int** graph = (int**)calloc((size_t)nodes, sizeof(int*));
    for (int i = 0; i < nodes; i++) graph[i] = (int*)calloc(8, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0];
        int b = edges[i][1];
        graph[a][graphSize[a]++] = b;
        graph[b][graphSize[b]++] = a;
    }
    int* visited = (int*)calloc((size_t)nodes, sizeof(int));
    int endpoint = 0, dummy = 0;
    farthest(edges[0][0], 0, graph, graphSize, visited, &endpoint, &dummy);
    memset(visited, 0, (size_t)nodes * sizeof(int));
    int dist = 0;
    farthest(endpoint, 0, graph, graphSize, visited, &endpoint, &dist);
    for (int i = 0; i < nodes; i++) free(graph[i]);
    free(graph);
    free(graphSize);
    free(visited);
    return dist;
}
