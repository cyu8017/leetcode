// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

#include <stdlib.h>

static int find(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

int* findRedundantConnection(int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    int* parent = (int*)malloc((size_t)(edgesSize + 1) * sizeof(int));
    for (int i = 0; i <= edgesSize; i++) parent[i] = i;
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = result[1] = 0;
    for (int i = 0; i < edgesSize; i++) {
        int a = find(parent, edges[i][0]);
        int b = find(parent, edges[i][1]);
        if (a == b) {
            result[0] = edges[i][0];
            result[1] = edges[i][1];
        } else parent[a] = b;
    }
    free(parent);
    *returnSize = 2;
    return result;
}
