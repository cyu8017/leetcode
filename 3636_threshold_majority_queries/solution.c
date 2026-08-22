// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

#include <stdlib.h>
int* subarrayMajority(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)numsSize;(void)queriesColSize;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int l = queries[qi][0], r = queries[qi][1], thresh = queries[qi][2];
        /* count with nested scan */
        int bestVal = -1, bestCnt = 0;
        for (int i = l; i <= r; i++) {
            int v = nums[i], c = 0;
            for (int j = l; j <= r; j++) if (nums[j] == v) c++;
            if (c >= thresh && (c > bestCnt || (c == bestCnt && (bestVal == -1 || v < bestVal)))) {
                bestCnt = c; bestVal = v;
            }
        }
        ans[qi] = bestVal;
    }
    *returnSize = queriesSize;
    return ans;
}
