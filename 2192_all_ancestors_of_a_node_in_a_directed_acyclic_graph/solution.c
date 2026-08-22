// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int cmpAsc(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int** getAncestors(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize, int** returnColumnSizes) {
    (void)edgesColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gLen = (int*)calloc((size_t)n, sizeof(int));
    int* gCap = (int*)calloc((size_t)n, sizeof(int));
    int* indeg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (gLen[u] == gCap[u]) {
            gCap[u] = gCap[u] ? gCap[u] * 2 : 4;
            g[u] = (int*)realloc(g[u], (size_t)gCap[u] * sizeof(int));
        }
        g[u][gLen[u]++] = v;
        indeg[v]++;
    }
    bool** anc = (bool**)malloc((size_t)n * sizeof(bool*));
    for (int i = 0; i < n; i++) anc[i] = (bool*)calloc((size_t)n, sizeof(bool));
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 0; i < n; i++) if (indeg[i] == 0) q[qt++] = i;
    while (qh < qt) {
        int u = q[qh++];
        for (int t = 0; t < gLen[u]; t++) {
            int v = g[u][t];
            anc[v][u] = true;
            for (int a = 0; a < n; a++) if (anc[u][a]) anc[v][a] = true;
            if (--indeg[v] == 0) q[qt++] = v;
        }
    }
    int** ans = (int**)malloc((size_t)n * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        int* tmp = (int*)malloc((size_t)n * sizeof(int));
        int tn = 0;
        for (int a = 0; a < n; a++) if (anc[i][a]) tmp[tn++] = a;
        qsort(tmp, (size_t)tn, sizeof(int), cmpAsc);
        ans[i] = tmp;
        (*returnColumnSizes)[i] = tn;
    }
    for (int i = 0; i < n; i++) { free(g[i]); free(anc[i]); }
    free(g); free(gLen); free(gCap); free(indeg); free(anc); free(q);
    *returnSize = n;
    return ans;
}
