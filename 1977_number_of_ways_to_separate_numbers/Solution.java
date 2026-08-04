// LeetCode 1977 - Number of Ways to Separate Numbers
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

class Solution {
    public int numberOfCombinations(String num) {
        final int MOD = 1_000_000_007;
        int n = num.length();
        if (num.charAt(0) == '0') return 0;
        int[][] lcp = new int[n + 1][n + 1];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (num.charAt(i) == num.charAt(j)) lcp[i][j] = lcp[i + 1][j + 1] + 1;
            }
        }
        int[][] dp = new int[n + 1][n + 1];
        int[][] pref = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int l = 1; l <= i; l++) {
                int start = i - l;
                if (num.charAt(start) == '0') dp[i][l] = 0;
                else if (start == 0) dp[i][l] = 1;
                else {
                    int ways = l > 1 ? pref[start][Math.min(l - 1, start)] : 0;
                    if (start >= l && le(num, lcp, start - l, start, l)) {
                        ways = (ways + dp[start][l]) % MOD;
                    }
                    dp[i][l] = ways;
                }
            }
            for (int l = 1; l <= n; l++) {
                pref[i][l] = (pref[i][l - 1] + (l <= i ? dp[i][l] : 0)) % MOD;
            }
        }
        return pref[n][n];
    }

    private boolean le(String num, int[][] lcp, int a, int b, int length) {
        int common = lcp[a][b];
        if (common >= length) return true;
        return num.charAt(a + common) < num.charAt(b + common);
    }
}
