// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

#include <stdbool.h>
#include <stdlib.h>

static int find(int* parent, int node) {
    if (parent[node] != node) {
        parent[node] = find(parent, parent[node]);
    }
    return parent[node];
}

bool validTree(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    if (edgesSize != n - 1) {
        return false;
    }
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }
    for (int i = 0; i < edgesSize; i++) {
        int rootLeft = find(parent, edges[i][0]);
        int rootRight = find(parent, edges[i][1]);
        if (rootLeft == rootRight) {
            free(parent);
            return false;
        }
        parent[rootLeft] = rootRight;
    }
    free(parent);
    return true;
}
