// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

using System.Collections.Generic;

public class Solution {
    const int MOD = 1000000007;
    long Qpow(long x, int n) {
        long res = 1;
        while (n > 0) {
            if ((n & 1) != 0) res = res * x % MOD;
            x = x * x % MOD;
            n >>= 1;
        }
        return res;
    }
    public int[] QueryConversions(int[][] conversions, int[][] queries) {
        int n = conversions.Length + 1;
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in conversions) g[e[0]].Add((e[1], e[2]));
        int[] res = new int[n];
        void Dfs(int s, int mul) {
            res[s] = mul;
            foreach (var (t, w) in g[s]) Dfs(t, (int)(1L * mul * w % MOD));
        }
        Dfs(0, 1);
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++)
            ans[i] = (int)(1L * res[queries[i][1]] * Qpow(res[queries[i][0]], MOD - 2) % MOD);
        return ans;
    }
}
