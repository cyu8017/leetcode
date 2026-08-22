// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minCosts(int* cost, int costSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)costSize * sizeof(int));
    int mi = cost[0];
    for (int i = 0; i < costSize; i++) {
        if (cost[i] < mi) mi = cost[i];
        ans[i] = mi;
    }
    *returnSize = costSize;
    return ans;
}
