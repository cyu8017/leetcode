// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

#include <stdlib.h>
#include <string.h>

int* findMinHeightTrees(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    int* result = (int*)malloc((size_t)n * sizeof(int));
    *returnSize = 0;
    if (n <= 2) {
        for (int node = 0; node < n; node++) {
            result[(*returnSize)++] = node;
        }
        return result;
    }

    int** graph = (int**)calloc((size_t)n, sizeof(int*));
    int* graphSize = (int*)calloc((size_t)n, sizeof(int));
    int* graphCapacity = (int*)calloc((size_t)n, sizeof(int));
    int* degree = (int*)calloc((size_t)n, sizeof(int));

    for (int index = 0; index < edgesSize; index++) {
        int left = edges[index][0];
        int right = edges[index][1];
        if (graphSize[left] == graphCapacity[left]) {
            graphCapacity[left] = graphCapacity[left] ? graphCapacity[left] * 2 : 4;
            graph[left] = realloc(graph[left], (size_t)graphCapacity[left] * sizeof(int));
        }
        graph[left][graphSize[left]++] = right;
        if (graphSize[right] == graphCapacity[right]) {
            graphCapacity[right] = graphCapacity[right] ? graphCapacity[right] * 2 : 4;
            graph[right] = realloc(graph[right], (size_t)graphCapacity[right] * sizeof(int));
        }
        graph[right][graphSize[right]++] = left;
        degree[left] += 1;
        degree[right] += 1;
    }

    int* leaves = (int*)malloc((size_t)n * sizeof(int));
    int leafCount = 0;
    for (int node = 0; node < n; node++) {
        if (degree[node] == 1) {
            leaves[leafCount++] = node;
        }
    }

    int remaining = n;
    while (remaining > 2) {
        remaining -= leafCount;
        int* newLeaves = (int*)malloc((size_t)n * sizeof(int));
        int newLeafCount = 0;
        for (int index = 0; index < leafCount; index++) {
            int leaf = leaves[index];
            for (int neighborIndex = 0; neighborIndex < graphSize[leaf]; neighborIndex++) {
                int neighbor = graph[leaf][neighborIndex];
                degree[neighbor] -= 1;
                if (degree[neighbor] == 1) {
                    newLeaves[newLeafCount++] = neighbor;
                }
            }
        }
        free(leaves);
        leaves = newLeaves;
        leafCount = newLeafCount;
    }

    *returnSize = leafCount;
    free(result);
    result = leaves;

    for (int node = 0; node < n; node++) {
        free(graph[node]);
    }
    free(graph);
    free(graphSize);
    free(graphCapacity);
    free(degree);
    return result;
}
