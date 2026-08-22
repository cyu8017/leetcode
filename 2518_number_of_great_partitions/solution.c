// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

#include <stdlib.h>
#include <string.h>

int countPartitions(int* nums, int numsSize, int k) {
    const int MOD = 1000000007;
    long long sum = 0;
    for (int i = 0; i < numsSize; i++) sum += nums[i];
    if (sum < 2LL * k) return 0;
    int* dp = (int*)calloc((size_t)k, sizeof(int));
    dp[0] = 1;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        for (int s = k - 1; s >= x; s--) dp[s] = (dp[s] + dp[s - x]) % MOD;
    }
    int bad = 0;
    for (int i = 0; i < k; i++) bad = (bad + dp[i]) % MOD;
    int total = 1;
    for (int i = 0; i < numsSize; i++) total = (int)(total * 2LL % MOD);
    int ans = (total - 2LL * bad % MOD + MOD) % MOD;
    free(dp);
    return ans;
}
