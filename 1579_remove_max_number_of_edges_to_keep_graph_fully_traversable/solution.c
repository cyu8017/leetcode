// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

#include <stdlib.h>

typedef struct {
    int* parent;
    int components;
} DSU;

static void dsuInit(DSU* d, int n) {
    d->parent = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) d->parent[i] = i;
    d->components = n;
}

static int dsuFind(DSU* d, int x) {
    while (x != d->parent[x]) {
        d->parent[x] = d->parent[d->parent[x]];
        x = d->parent[x];
    }
    return x;
}

static int dsuUnion(DSU* d, int a, int b) {
    a = dsuFind(d, a);
    b = dsuFind(d, b);
    if (a == b) return 0;
    d->parent[a] = b;
    d->components--;
    return 1;
}

int maxNumEdgesToRemove(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    DSU alice, bob;
    dsuInit(&alice, n);
    dsuInit(&bob, n);
    int used = 0;
    for (int i = 0; i < edgesSize; i++) {
        if (edges[i][0] == 3) {
            int merged = dsuUnion(&alice, edges[i][1], edges[i][2]);
            dsuUnion(&bob, edges[i][1], edges[i][2]);
            used += merged;
        }
    }
    for (int i = 0; i < edgesSize; i++) {
        if (edges[i][0] == 1) used += dsuUnion(&alice, edges[i][1], edges[i][2]);
        else if (edges[i][0] == 2) used += dsuUnion(&bob, edges[i][1], edges[i][2]);
    }
    int ans = (alice.components == 1 && bob.components == 1) ? edgesSize - used : -1;
    free(alice.parent);
    free(bob.parent);
    return ans;
}
