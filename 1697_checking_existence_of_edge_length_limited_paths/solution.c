// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

#include <stdbool.h>
#include <stdlib.h>

typedef struct { int u, v, w, idx; } Edge;

static int cmpEdge(const void* a, const void* b) {
    return ((const Edge*)a)->w - ((const Edge*)b)->w;
}

static int findp(int* p, int x) {
    while (x != p[x]) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}

bool* distanceLimitedPathsExist(int n, int** edgeList, int edgeListSize, int* edgeListColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)edgeListColSize; (void)queriesColSize;
    Edge* edges = (Edge*)malloc((size_t)edgeListSize * sizeof(Edge));
    for (int i = 0; i < edgeListSize; i++) {
        edges[i].u = edgeList[i][0];
        edges[i].v = edgeList[i][1];
        edges[i].w = edgeList[i][2];
        edges[i].idx = i;
    }
    qsort(edges, (size_t)edgeListSize, sizeof(Edge), cmpEdge);

    Edge* qs = (Edge*)malloc((size_t)queriesSize * sizeof(Edge));
    for (int i = 0; i < queriesSize; i++) {
        qs[i].u = queries[i][0];
        qs[i].v = queries[i][1];
        qs[i].w = queries[i][2];
        qs[i].idx = i;
    }
    qsort(qs, (size_t)queriesSize, sizeof(Edge), cmpEdge);

    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    bool* ans = (bool*)calloc((size_t)queriesSize, sizeof(bool));
    *returnSize = queriesSize;

    int ei = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int limit = qs[qi].w;
        while (ei < edgeListSize && edges[ei].w < limit) {
            int a = findp(parent, edges[ei].u);
            int b = findp(parent, edges[ei].v);
            parent[a] = b;
            ei++;
        }
        ans[qs[qi].idx] = findp(parent, qs[qi].u) == findp(parent, qs[qi].v);
    }
    free(edges); free(qs); free(parent);
    return ans;
}
