// LeetCode 0377 - Combination Sum IV
// https://leetcode.com/problems/combination-sum-iv/

#include <stdlib.h>

int combinationSum4(int* nums, int numsSize, int target) {
    unsigned int* dp = (unsigned int*)calloc((size_t)target + 1, sizeof(unsigned int));
    dp[0] = 1;

    for (int amount = 1; amount <= target; amount++) {
        for (int index = 0; index < numsSize; index++) {
            int num = nums[index];
            if (amount >= num) {
                dp[amount] += dp[amount - num];
            }
        }
    }

    int result = (int)dp[target];
    free(dp);
    return result;
}
