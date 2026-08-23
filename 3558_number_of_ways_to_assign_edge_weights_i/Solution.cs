// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

using System;
using System.Collections.Generic;

public class Solution {
    public int AssignEdgeWeights(int[][] edges) {
        const int mod = 1000000007;
        int n = edges.Length + 1;
        var g = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int Dfs(int i, int fa) {
            int res = 0;
            foreach (int j in g[i]) {
                if (j != fa) res = Math.Max(res, Dfs(j, i) + 1);
            }
            return res;
        }
        int Pow2(int exp) {
            long a = 2, res = 1;
            while (exp > 0) {
                if ((exp & 1) != 0) res = res * a % mod;
                a = a * a % mod;
                exp >>= 1;
            }
            return (int)res;
        }
        return Pow2(Dfs(1, 0) - 1);
    }
}
