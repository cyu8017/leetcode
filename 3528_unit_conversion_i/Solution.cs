// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

using System.Collections.Generic;

public class Solution {
    public int[] BaseUnitConversions(int[][] conversions) {
        const int mod = 1000000007;
        int n = conversions.Length + 1;
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in conversions) g[e[0]].Add((e[1], e[2]));
        int[] ans = new int[n];
        void Dfs(int s, int mul) {
            ans[s] = mul;
            foreach (var (t, w) in g[s]) Dfs(t, (int)(1L * mul * w % mod));
        }
        Dfs(0, 1);
        return ans;
    }
}
