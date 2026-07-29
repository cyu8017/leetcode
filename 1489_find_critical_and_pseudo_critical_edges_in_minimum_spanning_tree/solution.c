// LeetCode 1489 - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

#include <stdlib.h>
#include <limits.h>

typedef struct { int w, a, b, i; } Edge;
static int cmp_edge(const void* a, const void* b) { return ((const Edge*)a)->w - ((const Edge*)b)->w; }

static int findp(int* parent, int x) {
    while (x != parent[x]) { parent[x] = parent[parent[x]]; x = parent[x]; }
    return x;
}

static int mst(Edge* es, int m, int n, int skip, int force) {
    int* parent = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    int total = 0, used = 0;
    if (force >= 0) {
        Edge e = es[force];
        parent[findp(parent, e.a)] = findp(parent, e.b);
        total += e.w; used++;
    }
    for (int j = 0; j < m; j++) {
        if (j == skip || j == force) continue;
        int x = findp(parent, es[j].a), y = findp(parent, es[j].b);
        if (x != y) { parent[x] = y; total += es[j].w; used++; }
    }
    free(parent);
    return used == n - 1 ? total : INT_MAX / 4;
}

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int** findCriticalAndPseudoCriticalEdges(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize, int** returnColumnSizes) {
    (void)edgesColSize;
    Edge* es = (Edge*)malloc(edgesSize * sizeof(Edge));
    for (int i = 0; i < edgesSize; i++) {
        es[i].a = edges[i][0]; es[i].b = edges[i][1]; es[i].w = edges[i][2]; es[i].i = i;
    }
    qsort(es, edgesSize, sizeof(Edge), cmp_edge);
    int base = mst(es, edgesSize, n, -1, -1);
    int* critical = (int*)malloc(edgesSize * sizeof(int));
    int* pseudo = (int*)malloc(edgesSize * sizeof(int));
    int cn = 0, pn = 0;
    for (int j = 0; j < edgesSize; j++) {
        if (mst(es, edgesSize, n, j, -1) > base) critical[cn++] = es[j].i;
        else if (mst(es, edgesSize, n, -1, j) == base) pseudo[pn++] = es[j].i;
    }
    qsort(critical, cn, sizeof(int), cmp_int);
    qsort(pseudo, pn, sizeof(int), cmp_int);
    int** ans = (int**)malloc(2 * sizeof(int*));
    ans[0] = critical; ans[1] = pseudo;
    *returnColumnSizes = (int*)malloc(2 * sizeof(int));
    (*returnColumnSizes)[0] = cn; (*returnColumnSizes)[1] = pn;
    *returnSize = 2;
    free(es);
    return ans;
}
