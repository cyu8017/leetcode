// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

#include <stdlib.h>
#include <stdbool.h>

static int findRoot(int* parent, int x) {
    while (x != parent[x]) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

bool* areConnected(int n, int threshold, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* parent = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) parent[i] = i;
    for (int d = threshold + 1; d <= n; d++) {
        for (int x = 2 * d; x <= n; x += d) {
            int a = findRoot(parent, d), b = findRoot(parent, x);
            if (a != b) parent[b] = a;
        }
    }
    bool* ans = (bool*)malloc((size_t)queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; i++) {
        ans[i] = findRoot(parent, queries[i][0]) == findRoot(parent, queries[i][1]);
    }
    *returnSize = queriesSize;
    free(parent);
    return ans;
}
