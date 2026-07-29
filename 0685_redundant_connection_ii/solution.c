// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

#include <stdlib.h>
#include <string.h>

static int findRoot(int* uf, int x) {
    while (uf[x] != x) { uf[x] = uf[uf[x]]; x = uf[x]; }
    return x;
}

int* findRedundantDirectedConnection(int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    int* parent = (int*)calloc((size_t)edgesSize + 1, sizeof(int));
    int cand1[2] = {0, 0}, cand2[2] = {0, 0};
    int hasCand = 0;
    int* uArr = (int*)malloc((size_t)edgesSize * sizeof(int));
    int* vArr = (int*)malloc((size_t)edgesSize * sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        uArr[i] = edges[i][0];
        vArr[i] = edges[i][1];
        if (parent[vArr[i]] == 0) parent[vArr[i]] = uArr[i];
        else {
            cand1[0] = parent[vArr[i]]; cand1[1] = vArr[i];
            cand2[0] = uArr[i]; cand2[1] = vArr[i];
            uArr[i] = -1; vArr[i] = -1;
            hasCand = 1;
            break;
        }
    }
    int* uf = (int*)malloc((size_t)(edgesSize + 1) * sizeof(int));
    for (int i = 0; i <= edgesSize; i++) uf[i] = i;
    int* result = (int*)malloc(2 * sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        if (uArr[i] < 0) continue;
        int pu = findRoot(uf, uArr[i]), pv = findRoot(uf, vArr[i]);
        if (pu == pv) {
            if (hasCand) { result[0] = cand1[0]; result[1] = cand1[1]; }
            else { result[0] = uArr[i]; result[1] = vArr[i]; }
            free(parent); free(uArr); free(vArr); free(uf);
            *returnSize = 2;
            return result;
        }
        uf[pu] = pv;
    }
    result[0] = cand2[0]; result[1] = cand2[1];
    free(parent); free(uArr); free(vArr); free(uf);
    *returnSize = 2;
    return result;
}
