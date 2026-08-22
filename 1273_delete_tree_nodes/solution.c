// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

#include <stdlib.h>

static void dfs(int node, int** children, int* childSize, int* value, long long* sum, int* count) {
    *sum = value[node];
    *count = 1;
    for (int i = 0; i < childSize[node]; i++) {
        long long childSum;
        int childCount;
        dfs(children[node][i], children, childSize, value, &childSum, &childCount);
        *sum += childSum;
        *count += childCount;
    }
    if (*sum == 0) *count = 0;
}

int deleteTreeNodes(int nodes, int* parent, int* value) {
    int* childSize = (int*)calloc((size_t)nodes, sizeof(int));
    int** children = (int**)calloc((size_t)nodes, sizeof(int*));
    for (int i = 0; i < nodes; i++) children[i] = (int*)malloc((size_t)nodes * sizeof(int));
    for (int node = 1; node < nodes; node++) {
        int p = parent[node];
        children[p][childSize[p]++] = node;
    }
    long long sum = 0;
    int count = 0;
    dfs(0, children, childSize, value, &sum, &count);
    for (int i = 0; i < nodes; i++) free(children[i]);
    free(children);
    free(childSize);
    return count;
}
