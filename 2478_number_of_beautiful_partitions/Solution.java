// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

class Solution {
    private boolean isPrime(char c) {
        return c == '2' || c == '3' || c == '5' || c == '7';
    }

    public int beautifulPartitions(String s, int k, int minLength) {
        final int mod = 1000000007;
        int n = s.length();
        if (!isPrime(s.charAt(0)) || isPrime(s.charAt(n - 1))) return 0;
        int[][] dp = new int[k + 1][n + 1];
        dp[0][0] = 1;
        for (int p = 1; p <= k; p++) {
            int pref = 0, j = 0;
            for (int i = 1; i <= n; i++) {
                while (j <= i - minLength) {
                    if (j == 0 || (isPrime(s.charAt(j)) && !isPrime(s.charAt(j - 1)))) {
                        pref = (pref + dp[p - 1][j]) % mod;
                    }
                    j++;
                }
                if (!isPrime(s.charAt(i - 1))) dp[p][i] = pref;
            }
        }
        return dp[k][n];
    }
}
