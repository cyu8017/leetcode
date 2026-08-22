// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

#include <stdlib.h>

int* findIndices(int* nums, int numsSize, int indexDifference, int valueDifference, int* returnSize) {
    int* ans = (int*)malloc(2 * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        for (int j = i; j < numsSize; j++) {
            int di = j - i; if (di < 0) di = -di;
            int dv = nums[i] - nums[j]; if (dv < 0) dv = -dv;
            if (di >= indexDifference && dv >= valueDifference) {
                ans[0] = i; ans[1] = j; *returnSize = 2; return ans;
            }
        }
    }
    ans[0] = -1; ans[1] = -1; *returnSize = 2; return ans;
}
