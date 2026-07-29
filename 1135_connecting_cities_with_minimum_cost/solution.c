// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

#include <stdlib.h>

static int cmpConn(const void* a, const void* b) {
    const int* x = *(const int* const*)a;
    const int* y = *(const int* const*)b;
    return x[2] - y[2];
}

static int findP(int* p, int x) {
    while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}

int minimumCost(int n, int** connections, int connectionsSize, int* connectionsColSize) {
    (void)connectionsColSize;
    int* parent = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) parent[i] = i;
    qsort(connections, (size_t)connectionsSize, sizeof(int*), cmpConn);
    int cost = 0, edges = 0;
    for (int i = 0; i < connectionsSize; i++) {
        int a = findP(parent, connections[i][0]);
        int b = findP(parent, connections[i][1]);
        if (a != b) {
            parent[b] = a;
            cost += connections[i][2];
            edges++;
            if (edges == n - 1) { free(parent); return cost; }
        }
    }
    free(parent);
    return -1;
}
