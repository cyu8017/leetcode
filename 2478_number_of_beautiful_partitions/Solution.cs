// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

public class Solution {
    public int BeautifulPartitions(string s, int k, int minLength) {
        const int mod = 1000000007;
        bool IsPrime(char c) => c == '2' || c == '3' || c == '5' || c == '7';
        int n = s.Length;
        if (!IsPrime(s[0]) || IsPrime(s[n - 1])) return 0;
        int[][] dp = new int[k + 1][];
        for (int p = 0; p <= k; p++) dp[p] = new int[n + 1];
        dp[0][0] = 1;
        for (int p = 1; p <= k; p++) {
            int pref = 0, j = 0;
            for (int i = 1; i <= n; i++) {
                while (j <= i - minLength) {
                    if (j == 0 || (IsPrime(s[j]) && !IsPrime(s[j - 1])))
                        pref = (pref + dp[p - 1][j]) % mod;
                    j++;
                }
                if (!IsPrime(s[i - 1])) dp[p][i] = pref;
            }
        }
        return dp[k][n];
    }
}
