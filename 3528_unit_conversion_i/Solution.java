// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] baseUnitConversions(int[][] conversions) {
        final int mod = 1_000_000_007;
        int n = conversions.length + 1;
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : conversions) g[e[0]].add(new int[] {e[1], e[2]});
        int[] ans = new int[n];
        dfs(0, 1, g, ans, mod);
        return ans;
    }

    void dfs(int s, int mul, List<int[]>[] g, int[] ans, int mod) {
        ans[s] = mul;
        for (int[] e : g[s]) dfs(e[0], (int) (1L * mul * e[1] % mod), g, ans, mod);
    }
}
