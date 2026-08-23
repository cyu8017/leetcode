// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

using System.Collections.Generic;

public class Solution {
    public int MaxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int ans = 0;
        int Dfs(int u, int p) {
            int sum = values[u] % k;
            foreach (int v in g[u]) {
                if (v == p) continue;
                sum = (sum + Dfs(v, u)) % k;
            }
            if (sum == 0) ans++;
            return sum;
        }
        Dfs(0, -1);
        return ans;
    }
}
