// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

#include <stdlib.h>

int findTargetSumWays(int* nums, int numsSize, int target) {
    long long total = 0;
    for (int index = 0; index < numsSize; index++) {
        total += nums[index];
    }
    if ((total + target) % 2 != 0 || (target < 0 ? -target : target) > total) {
        return 0;
    }
    const int need = (int)((total + target) / 2);
    int* dp = (int*)calloc((size_t)(need + 1), sizeof(int));
    dp[0] = 1;
    for (int index = 0; index < numsSize; index++) {
        const int num = nums[index];
        for (int amount = need; amount >= num; amount--) {
            dp[amount] += dp[amount - num];
        }
    }
    const int result = dp[need];
    free(dp);
    return result;
}
