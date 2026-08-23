// LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

using System.Collections.Generic;

public class Solution {
    static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public int CountCoprime(int[][] mat) {
        const int MOD = 1000000007;
        int m = mat.Length;
        var dp = new Dictionary<int, int>();
        foreach (int v in mat[0]) {
            if (!dp.ContainsKey(v)) dp[v] = 0;
            dp[v]++;
        }
        for (int i = 1; i < m; i++) {
            var ndp = new Dictionary<int, int>();
            foreach (int v in mat[i]) {
                foreach (var kv in dp) {
                    int ng = Gcd(kv.Key, v);
                    if (!ndp.ContainsKey(ng)) ndp[ng] = 0;
                    ndp[ng] = (ndp[ng] + kv.Value) % MOD;
                }
            }
            dp = ndp;
        }
        return dp.ContainsKey(1) ? dp[1] : 0;
    }
}
