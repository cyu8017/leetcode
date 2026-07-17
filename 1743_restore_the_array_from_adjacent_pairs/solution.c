// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

#include <stdlib.h>

#define OFFSET 100000
#define RANGE 200001

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* restoreArray(int** adjacentPairs, int adjacentPairsSize, int* adjacentPairsColSize, int* returnSize) {
    int n = adjacentPairsSize + 1;
    int (*neighbors)[2] = malloc(RANGE * sizeof(*neighbors));
    int* degree = (int*)calloc(RANGE, sizeof(int));
    for (int i = 0; i < adjacentPairsSize; i++) {
        int a = adjacentPairs[i][0] + OFFSET;
        int b = adjacentPairs[i][1] + OFFSET;
        neighbors[a][degree[a]++] = b - OFFSET;
        neighbors[b][degree[b]++] = a - OFFSET;
    }
    int start = 0;
    for (int i = 0; i < adjacentPairsSize; i++) {
        int a = adjacentPairs[i][0];
        int b = adjacentPairs[i][1];
        if (degree[a + OFFSET] == 1) {
            start = a;
            break;
        }
        if (degree[b + OFFSET] == 1) {
            start = b;
            break;
        }
    }
    int* ans = (int*)malloc(n * sizeof(int));
    ans[0] = start;
    for (int i = 1; i < n; i++) {
        int cur = ans[i - 1];
        int* adj = neighbors[cur + OFFSET];
        if (i == 1 || adj[0] != ans[i - 2]) {
            ans[i] = adj[0];
        } else {
            ans[i] = adj[1];
        }
    }
    free(neighbors);
    free(degree);
    *returnSize = n;
    return ans;
}
