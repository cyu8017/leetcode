// LeetCode 2369 - Check if There is a Valid Partition For The Array
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

#include <stdlib.h>
#include <stdbool.h>

bool validPartition(int* nums, int numsSize) {
    bool* dp = (bool*)calloc((size_t)(numsSize + 1), sizeof(bool));
    dp[0] = true;
    for (int i = 1; i <= numsSize; i++) {
        if (i >= 2 && nums[i-1] == nums[i-2] && dp[i-2]) dp[i] = true;
        if (i >= 3 && nums[i-1] == nums[i-2] && nums[i-2] == nums[i-3] && dp[i-3]) dp[i] = true;
        if (i >= 3 && nums[i-1] == nums[i-2]+1 && nums[i-2] == nums[i-3]+1 && dp[i-3]) dp[i] = true;
    }
    bool ans = dp[numsSize];
    free(dp);
    return ans;
}
