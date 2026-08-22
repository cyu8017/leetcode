// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

#include <stdlib.h>
#include <stdbool.h>

static int findp(int* parent, int x) {
    if (parent[x] != x) parent[x] = findp(parent, parent[x]);
    return parent[x];
}

typedef struct { int idx; int val; } Node;
static int cmpNode(const void* a, const void* b) { return ((const Node*)a)->val - ((const Node*)b)->val; }

int numberOfGoodPaths(int* vals, int valsSize, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = valsSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gs = (int*)calloc((size_t)n, sizeof(int));
    int* gc = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (gs[a]==gc[a]) { gc[a]=gc[a]?gc[a]*2:2; g[a]=(int*)realloc(g[a],(size_t)gc[a]*sizeof(int)); }
        if (gs[b]==gc[b]) { gc[b]=gc[b]?gc[b]*2:2; g[b]=(int*)realloc(g[b],(size_t)gc[b]*sizeof(int)); }
        g[a][gs[a]++]=b; g[b][gs[b]++]=a;
    }
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    int* size = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
    Node* nodes = (Node*)malloc((size_t)n * sizeof(Node));
    for (int i = 0; i < n; i++) nodes[i] = (Node){i, vals[i]};
    qsort(nodes, (size_t)n, sizeof(Node), cmpNode);
    int ans = n;
    int i = 0;
    while (i < n) {
        int j = i;
        while (j < n && nodes[j].val == nodes[i].val) j++;
        for (int k = i; k < j; k++) {
            int u = nodes[k].idx;
            for (int t = 0; t < gs[u]; t++) {
                int v = g[u][t];
                if (vals[v] <= vals[u]) {
                    int ru = findp(parent, u), rv = findp(parent, v);
                    if (ru != rv) { parent[ru] = rv; size[rv] += size[ru]; }
                }
            }
        }
        /* count freq of roots */
        int* roots = (int*)malloc((size_t)(j - i) * sizeof(int));
        int rc = 0;
        for (int k = i; k < j; k++) {
            int r = findp(parent, nodes[k].idx);
            int found = 0;
            for (int z = 0; z < rc; z++) if (roots[z] == r) { found = 1; /* count in parallel */ break; }
            if (!found) roots[rc++] = r;
        }
        /* recount properly */
        for (int z = 0; z < rc; z++) {
            int c = 0;
            for (int k = i; k < j; k++) if (findp(parent, nodes[k].idx) == roots[z]) c++;
            ans += c * (c - 1) / 2;
        }
        free(roots);
        i = j;
    }
    for (int i2 = 0; i2 < n; i2++) free(g[i2]);
    free(g); free(gs); free(gc); free(parent); free(size); free(nodes);
    return ans;
}
