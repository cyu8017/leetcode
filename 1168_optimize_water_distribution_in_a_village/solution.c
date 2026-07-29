// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

#include <stdlib.h>

typedef struct { int a, b, cost; } Edge;

static int cmpEdge(const void* x, const void* y) {
    return ((const Edge*)x)->cost - ((const Edge*)y)->cost;
}

static int findP(int* p, int x) {
    while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}

int minCostToSupplyWater(int n, int* wells, int wellsSize, int** pipes, int pipesSize, int* pipesColSize) {
    (void)wellsSize; (void)pipesColSize;
    Edge* edges = (Edge*)malloc((size_t)(n + pipesSize) * sizeof(Edge));
    int m = 0;
    for (int i = 0; i < n; i++) edges[m++] = (Edge){0, i + 1, wells[i]};
    for (int i = 0; i < pipesSize; i++) edges[m++] = (Edge){pipes[i][0], pipes[i][1], pipes[i][2]};
    qsort(edges, (size_t)m, sizeof(Edge), cmpEdge);
    int* parent = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) parent[i] = i;
    int ans = 0;
    for (int i = 0; i < m; i++) {
        int ra = findP(parent, edges[i].a);
        int rb = findP(parent, edges[i].b);
        if (ra == rb) continue;
        parent[rb] = ra;
        ans += edges[i].cost;
    }
    free(edges); free(parent);
    return ans;
}
