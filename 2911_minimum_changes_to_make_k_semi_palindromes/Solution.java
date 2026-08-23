// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

class Solution {
    private String s;

    public int minimumChanges(String s, int k) {
        this.s = s;
        int n = s.length();
        int[][] cost = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) cost[i][j] = 1 << 20;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                cost[i][j] = semiCost(i, j);
        int[][] dp = new int[k + 1][n + 1];
        for (int p = 0; p <= k; p++)
            for (int i = 0; i <= n; i++) dp[p][i] = 1 << 20;
        dp[0][0] = 0;
        for (int p = 1; p <= k; p++)
            for (int i = 1; i <= n; i++)
                for (int t = 0; t < i - 1; t++) {
                    int cand = dp[p - 1][t] + cost[t][i - 1];
                    if (cand < dp[p][i]) dp[p][i] = cand;
                }
        return dp[k][n];
    }

    private int semiCost(int l, int r) {
        int length = r - l + 1, best = 1 << 20;
        for (int d = 1; d < length; d++) {
            if (length % d != 0) continue;
            int chg = 0;
            for (int start = 0; start < d; start++) {
                StringBuilder chars = new StringBuilder();
                for (int i = l + start; i <= r; i += d) chars.append(s.charAt(i));
                for (int i = 0, j = chars.length() - 1; i < j; i++, j--)
                    if (chars.charAt(i) != chars.charAt(j)) chg++;
            }
            if (chg < best) best = chg;
        }
        return best;
    }
}
