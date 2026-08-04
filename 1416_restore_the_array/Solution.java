// LeetCode 1416 - Restore The Array
// https://leetcode.com/problems/restore-the-array/

class Solution {
    public int numberOfArrays(String s, int k) {
        int mod = 1000000007, n = s.length;
        var dp = new int[n + 1]; dp[n] = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '0') continue;
            long value = 0;
            for (int j = i; j < n; j++) {
                value = value * 10 + (s[j] - '0');
                if (value > k) break;
                dp[i] = (dp[i] + dp[j + 1]) % mod;
            }
        }
        return dp[0];
    }
}
