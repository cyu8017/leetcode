// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

using System.Text;

public class Solution {
    public int MinimumChanges(string s, int k) {
        int n = s.Length;
        int[][] cost = new int[n][];
        for (int i = 0; i < n; i++) {
            cost[i] = new int[n];
            for (int j = 0; j < n; j++) cost[i][j] = 1 << 20;
        }
        int SemiCost(int l, int r) {
            int length = r - l + 1, best = 1 << 20;
            for (int d = 1; d < length; d++) {
                if (length % d != 0) continue;
                int chg = 0;
                for (int start = 0; start < d; start++) {
                    var chars = new StringBuilder();
                    for (int i = l + start; i <= r; i += d) chars.Append(s[i]);
                    string cs = chars.ToString();
                    for (int i = 0, j = cs.Length - 1; i < j; i++, j--)
                        if (cs[i] != cs[j]) chg++;
                }
                if (chg < best) best = chg;
            }
            return best;
        }
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                cost[i][j] = SemiCost(i, j);
        int[][] dp = new int[k + 1][];
        for (int p = 0; p <= k; p++) {
            dp[p] = new int[n + 1];
            for (int i = 0; i <= n; i++) dp[p][i] = 1 << 20;
        }
        dp[0][0] = 0;
        for (int p = 1; p <= k; p++)
            for (int i = 1; i <= n; i++)
                for (int t = 0; t < i - 1; t++) {
                    int cand = dp[p - 1][t] + cost[t][i - 1];
                    if (cand < dp[p][i]) dp[p][i] = cand;
                }
        return dp[k][n];
    }
}
