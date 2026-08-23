// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int assignEdgeWeights(int[][] edges) {
        final int mod = 1_000_000_007;
        int n = edges.length + 1;
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        return pow2(dfs(1, 0, g) - 1, mod);
    }

    int dfs(int i, int fa, List<Integer>[] g) {
        int res = 0;
        for (int j : g[i]) if (j != fa) res = Math.max(res, dfs(j, i, g) + 1);
        return res;
    }

    int pow2(int exp, int mod) {
        long a = 2, res = 1;
        while (exp > 0) {
            if ((exp & 1) != 0) res = res * a % mod;
            a = a * a % mod;
            exp >>= 1;
        }
        return (int) res;
    }
}
