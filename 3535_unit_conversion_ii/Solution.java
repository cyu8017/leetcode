// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    static final int MOD = 1_000_000_007;

    long qpow(long x, int n) {
        long res = 1;
        while (n > 0) {
            if ((n & 1) != 0) res = res * x % MOD;
            x = x * x % MOD;
            n >>= 1;
        }
        return res;
    }

    public int[] queryConversions(int[][] conversions, int[][] queries) {
        int n = conversions.length + 1;
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : conversions) g[e[0]].add(new int[] {e[1], e[2]});
        int[] res = new int[n];
        dfs(0, 1, g, res);
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++)
            ans[i] = (int) (1L * res[queries[i][1]] * qpow(res[queries[i][0]], MOD - 2) % MOD);
        return ans;
    }

    void dfs(int s, int mul, List<int[]>[] g, int[] res) {
        res[s] = mul;
        for (int[] e : g[s]) dfs(e[0], (int) (1L * mul * e[1] % MOD), g, res);
    }
}
