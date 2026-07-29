// LeetCode 0785 - Is Graph Bipartite?
#include <stdbool.h>
#include <stdlib.h>

static bool dfs(int** graph, int* graphColSize, int* color, int node, int c) {
    color[node] = c;
    for (int i = 0; i < graphColSize[node]; i++) {
        int nei = graph[node][i];
        if (color[nei] == -1) {
            if (!dfs(graph, graphColSize, color, nei, c ^ 1)) return false;
        } else if (color[nei] == c) return false;
    }
    return true;
}

bool isBipartite(int** graph, int graphSize, int* graphColSize) {
    int* color = (int*)malloc((size_t)graphSize * sizeof(int));
    for (int i = 0; i < graphSize; i++) color[i] = -1;
    for (int i = 0; i < graphSize; i++) {
        if (color[i] == -1 && !dfs(graph, graphColSize, color, i, 0)) {
            free(color); return false;
        }
    }
    free(color); return true;
}
