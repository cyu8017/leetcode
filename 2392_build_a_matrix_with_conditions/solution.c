// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

#include <stdlib.h>
#include <string.h>

static int* topo(int k, int** conds, int condsSize, int* ok) {
    int** g = (int**)calloc((size_t)(k + 1), sizeof(int*));
    int* gs = (int*)calloc((size_t)(k + 1), sizeof(int));
    int* gc = (int*)calloc((size_t)(k + 1), sizeof(int));
    int* indeg = (int*)calloc((size_t)(k + 1), sizeof(int));
    for (int i = 0; i < condsSize; i++) {
        int a = conds[i][0], b = conds[i][1];
        if (gs[a] == gc[a]) { gc[a] = gc[a] ? gc[a]*2 : 2; g[a] = (int*)realloc(g[a], (size_t)gc[a]*sizeof(int)); }
        g[a][gs[a]++] = b; indeg[b]++;
    }
    int* q = (int*)malloc((size_t)(k + 1) * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 1; i <= k; i++) if (indeg[i] == 0) q[qt++] = i;
    int* order = (int*)malloc((size_t)k * sizeof(int));
    int oc = 0;
    while (qh < qt) {
        int u = q[qh++];
        order[oc++] = u;
        for (int i = 0; i < gs[u]; i++) {
            int v = g[u][i];
            if (--indeg[v] == 0) q[qt++] = v;
        }
    }
    for (int i = 0; i <= k; i++) free(g[i]);
    free(g); free(gs); free(gc); free(indeg); free(q);
    if (oc != k) { free(order); *ok = 0; return NULL; }
    *ok = 1;
    return order;
}

int** buildMatrix(int k, int** rowConditions, int rowConditionsSize, int* rowConditionsColSize, int** colConditions, int colConditionsSize, int* colConditionsColSize, int* returnSize, int** returnColumnSizes) {
    (void)rowConditionsColSize; (void)colConditionsColSize;
    int ok1, ok2;
    int* rowOrder = topo(k, rowConditions, rowConditionsSize, &ok1);
    int* colOrder = topo(k, colConditions, colConditionsSize, &ok2);
    if (!ok1 || !ok2) {
        free(rowOrder); free(colOrder);
        *returnSize = 0; *returnColumnSizes = NULL; return NULL;
    }
    int* rowPos = (int*)malloc((size_t)(k + 1) * sizeof(int));
    int* colPos = (int*)malloc((size_t)(k + 1) * sizeof(int));
    for (int i = 0; i < k; i++) { rowPos[rowOrder[i]] = i; colPos[colOrder[i]] = i; }
    int** ans = (int**)malloc((size_t)k * sizeof(int*));
    int* cols = (int*)malloc((size_t)k * sizeof(int));
    for (int i = 0; i < k; i++) { ans[i] = (int*)calloc((size_t)k, sizeof(int)); cols[i] = k; }
    for (int v = 1; v <= k; v++) ans[rowPos[v]][colPos[v]] = v;
    free(rowOrder); free(colOrder); free(rowPos); free(colPos);
    *returnSize = k; *returnColumnSizes = cols;
    return ans;
}
