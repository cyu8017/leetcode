// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

#include <stdlib.h>

int* findSmallestSetOfVertices(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    int* incoming = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) incoming[edges[i][1]] = 1;
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int sz = 0;
    for (int i = 0; i < n; i++) if (!incoming[i]) ans[sz++] = i;
    free(incoming);
    *returnSize = sz;
    return ans;
}
