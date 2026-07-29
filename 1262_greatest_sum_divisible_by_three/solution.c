// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

#include <stdlib.h>

int maxSumDivThree(int* nums, int numsSize) {
    const long long impossible = -1000000000000000000LL;
    long long dp[3] = {0, impossible, impossible};
    for (int i = 0; i < numsSize; i++) {
        long long old[3] = {dp[0], dp[1], dp[2]};
        for (int r = 0; r < 3; r++) {
            if (old[r] != impossible) {
                int nr = (int)((old[r] + nums[i]) % 3);
                long long val = old[r] + nums[i];
                if (val > dp[nr]) dp[nr] = val;
            }
        }
    }
    return (int)dp[0];
}
