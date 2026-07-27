// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

#include <stdlib.h>
#include <string.h>

int longestArithSeqLength(int* nums, int numsSize) {
    // diffs in [-10000, 10000] -> offset 10000, width 20001
    const int OFFSET = 10000;
    const int WIDTH = 20001;
    int* dp = (int*)calloc((size_t)numsSize * WIDTH, sizeof(int));
    int ans = 1;
    for (int j = 1; j < numsSize; j++) {
        for (int i = 0; i < j; i++) {
            int d = nums[j] - nums[i] + OFFSET;
            int prev = dp[i * WIDTH + d];
            int cur = (prev ? prev : 1) + 1;
            if (cur > dp[j * WIDTH + d]) dp[j * WIDTH + d] = cur;
            if (cur > ans) ans = cur;
        }
    }
    free(dp);
    return ans;
}
