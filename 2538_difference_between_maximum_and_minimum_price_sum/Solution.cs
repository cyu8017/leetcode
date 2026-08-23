// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

using System.Collections.Generic;

public class Solution {
    public long MaxOutput(int n, int[][] edges, int[] price) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        long ans = 0;
        long Dfs(int u, int p) {
            long maxChild = 0;
            foreach (int v in g[u]) {
                if (v == p) continue;
                long child = Dfs(v, u);
                if (child > maxChild) maxChild = child;
                if (child > ans) ans = child;
            }
            return (long)price[u] + maxChild;
        }
        Dfs(0, -1);
        return ans;
    }
}
