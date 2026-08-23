// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

using System.Collections.Generic;

public class Solution {
    public long SubtreeInversionSum(int[][] edges, int[] nums, int k) {
        int n = edges.Length + 1;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = -1;
        var memo = new Dictionary<(int, int, bool), long>();
        long Dp(int u, int steps, bool inv) {
            var key = (u, steps, inv);
            if (memo.ContainsKey(key)) return memo[key];
            long num = nums[u];
            if (inv) num = -num;
            long negNum = -num;
            foreach (int v in graph[u]) {
                if (v == parent[u]) continue;
                parent[v] = u;
                int ns = steps + 1;
                if (ns > k) ns = k;
                num += Dp(v, ns, inv);
                if (steps == k) negNum += Dp(v, 1, !inv);
            }
            long res = num;
            if (steps == k && negNum > res) res = negNum;
            return memo[key] = res;
        }
        return Dp(0, k, false);
    }
}
