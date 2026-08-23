// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        boolean[][] isPal = new boolean[n][n];
        for (int i = 0; i < n; i++) isPal[i][i] = true;
        for (int i = 0; i + 1 < n; i++) isPal[i][i + 1] = s.charAt(i) == s.charAt(i + 1);
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                isPal[i][j] = s.charAt(i) == s.charAt(j) && isPal[i + 1][j - 1];
            }
        }
        int[] dp = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = dp[i + 1];
            for (int j = i + k - 1; j < n; j++) {
                if (isPal[i][j] && 1 + dp[j + 1] > dp[i]) dp[i] = 1 + dp[j + 1];
            }
        }
        return dp[0];
    }
}
