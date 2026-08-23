// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

class Solution {
    public int goodBinaryStrings(int minLength, int maxLength, int oneGroup, int zeroGroup) {
        final int MOD = 1000000007;
        int[] dp = new int[maxLength + 1];
        dp[0] = 1;
        for (int i = 0; i <= maxLength; i++) {
            if (dp[i] == 0) continue;
            if (i + oneGroup <= maxLength) dp[i + oneGroup] = (dp[i + oneGroup] + dp[i]) % MOD;
            if (i + zeroGroup <= maxLength) dp[i + zeroGroup] = (dp[i + zeroGroup] + dp[i]) % MOD;
        }
        int ans = 0;
        for (int i = minLength; i <= maxLength; i++) ans = (ans + dp[i]) % MOD;
        return ans;
    }
}
