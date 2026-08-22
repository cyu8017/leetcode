// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

#include <stdlib.h>
#include <stdbool.h>

static bool dfs(int node, int** graph, int* graphColSize, int* color) {
    if (color[node]) return color[node] == 2;
    color[node] = 1;
    for (int i = 0; i < graphColSize[node]; i++) {
        if (!dfs(graph[node][i], graph, graphColSize, color)) return false;
    }
    color[node] = 2;
    return true;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* eventualSafeNodes(int** graph, int graphSize, int* graphColSize, int* returnSize) {
    int* color = (int*)calloc((size_t)graphSize, sizeof(int));
    int* ans = (int*)malloc((size_t)graphSize * sizeof(int));
    int count = 0;
    for (int i = 0; i < graphSize; i++) {
        if (dfs(i, graph, graphColSize, color)) ans[count++] = i;
    }
    free(color);
    *returnSize = count;
    return ans;
}
