// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (String string : strs) {
            int zeros = 0;
            int ones = 0;
            for (int i = 0; i < string.length(); i++) {
                if (string.charAt(i) == '0') {
                    zeros++;
                } else {
                    ones++;
                }
            }
            for (int zero = m; zero >= zeros; zero--) {
                for (int one = n; one >= ones; one--) {
                    dp[zero][one] = Math.max(dp[zero][one], dp[zero - zeros][one - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }
}
