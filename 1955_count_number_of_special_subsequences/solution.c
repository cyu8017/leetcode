// LeetCode 1955 - Count Number of Special Subsequences
// https://leetcode.com/problems/count-number-of-special-subsequences/

int countSpecialSubsequences(int* nums, int numsSize) {
    const int MOD = 1000000007;
    long long dp0 = 0, dp1 = 0, dp2 = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) dp0 = (dp0 * 2 + 1) % MOD;
        else if (nums[i] == 1) dp1 = (dp1 * 2 + dp0) % MOD;
        else dp2 = (dp2 * 2 + dp1) % MOD;
    }
    return (int)dp2;
}
