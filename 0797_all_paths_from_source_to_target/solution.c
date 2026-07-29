// LeetCode 0797 - All Paths From Source to Target
#include <stdlib.h>

typedef struct { int** paths; int* colSizes; int size; int cap; } Acc;

static void addPath(Acc* acc, int* path, int len) {
    if (acc->size == acc->cap) {
        acc->cap = acc->cap ? acc->cap * 2 : 8;
        acc->paths = (int**)realloc(acc->paths, (size_t)acc->cap * sizeof(int*));
        acc->colSizes = (int*)realloc(acc->colSizes, (size_t)acc->cap * sizeof(int));
    }
    acc->paths[acc->size] = (int*)malloc((size_t)len * sizeof(int));
    for (int i = 0; i < len; i++) acc->paths[acc->size][i] = path[i];
    acc->colSizes[acc->size] = len;
    acc->size++;
}

static void dfs(int** graph, int* graphColSize, int target, int node, int* path, int len, Acc* acc) {
    if (node == target) { addPath(acc, path, len); return; }
    for (int i = 0; i < graphColSize[node]; i++) {
        path[len] = graph[node][i];
        dfs(graph, graphColSize, target, graph[node][i], path, len + 1, acc);
    }
}

int** allPathsSourceTarget(int** graph, int graphSize, int* graphColSize, int* returnSize, int** returnColumnSizes) {
    Acc acc = {0};
    int* path = (int*)malloc((size_t)graphSize * sizeof(int));
    path[0] = 0;
    dfs(graph, graphColSize, graphSize - 1, 0, path, 1, &acc);
    free(path);
    *returnSize = acc.size;
    *returnColumnSizes = acc.colSizes;
    return acc.paths;
}
