// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

using System;

public class Solution {
    public string ShortestSuperstring(string[] words) {
        int n = words.Length;
        int[,] overlap = new int[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                string a = words[i], b = words[j];
                for (int k = Math.Min(a.Length, b.Length); k > 0; k--) {
                    if (a.Substring(a.Length - k) == b.Substring(0, k)) {
                        overlap[i, j] = k;
                        break;
                    }
                }
            }
        }
        int N = 1 << n;
        string[,] dp = new string[N, n];
        for (int i = 0; i < n; i++) dp[1 << i, i] = words[i];
        for (int mask = 0; mask < N; mask++) {
            for (int last = 0; last < n; last++) {
                if ((mask & (1 << last)) == 0 || dp[mask, last] == null) continue;
                for (int nxt = 0; nxt < n; nxt++) {
                    if ((mask & (1 << nxt)) != 0) continue;
                    string cand = dp[mask, last] + words[nxt].Substring(overlap[last, nxt]);
                    int nmask = mask | (1 << nxt);
                    if (dp[nmask, nxt] == null || cand.Length < dp[nmask, nxt].Length)
                        dp[nmask, nxt] = cand;
                }
            }
        }
        int full = N - 1;
        string best = null;
        for (int i = 0; i < n; i++) {
            if (dp[full, i] != null && (best == null || dp[full, i].Length < best.Length))
                best = dp[full, i];
        }
        return best;
    }
}
