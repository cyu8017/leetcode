// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

class Solution {
    public int deleteString(String s) {
        int n = s.length();
        int[][] lcp = new int[n + 1][];
        for (int i = 0; i <= n; i++) lcp[i] = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (s.charAt(i) == s.charAt(j)) lcp[i][j] = lcp[i + 1][j + 1] + 1;
            }
        }
        int[] dp = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = 1;
            for (int len = 1; i + 2 * len <= n; len++) {
                if (lcp[i][i + len] >= len)
                    dp[i] = Math.max(dp[i], 1 + dp[i + len]);
            }
        }
        return dp[0];
    }
}
