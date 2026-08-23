// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

public class Solution {
    public int MinCost(string source, string target, string[][] rules, int[] costs) {
        int n = source.Length;
        if (target.Length != n) return -1;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = int.MaxValue;
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == int.MaxValue) continue;
            if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
            for (int j = 0; j < rules.Length; j++) {
                string p = rules[j][0];
                string r = rules[j][1];
                int plen = p.Length;
                if (i + plen > n) continue;
                int c = costs[j];
                bool ok = true;
                for (int k = 0; k < plen; k++) {
                    if (r[k] != target[i + k]) { ok = false; break; }
                    if (p[k] == '*') ++c;
                    else if (p[k] != source[i + k]) { ok = false; break; }
                }
                if (ok && dp[i] <= int.MaxValue - c && dp[i] + c < dp[i + plen]) {
                    dp[i + plen] = dp[i] + c;
                }
            }
        }
        return dp[n] == int.MaxValue ? -1 : dp[n];
    }
}
