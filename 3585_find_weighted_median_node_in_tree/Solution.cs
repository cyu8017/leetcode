// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

using System.Collections.Generic;

public class Solution {
    public int[] FindMedian(int n, int[][] edges, int[][] queries) {
        var g = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int u = queries[qi][0], v = queries[qi][1];
            int[] parent = new int[n], pw = new int[n];
            for (int i = 0; i < n; i++) parent[i] = -2;
            parent[u] = -1;
            var q = new Queue<int>();
            q.Enqueue(u);
            while (q.Count > 0) {
                int x = q.Dequeue();
                if (x == v) break;
                foreach (var e in g[x]) {
                    if (parent[e.to] == -2) {
                        parent[e.to] = x;
                        pw[e.to] = e.w;
                        q.Enqueue(e.to);
                    }
                }
            }
            var nodes = new List<int> { v };
            var weights = new List<int>();
            int cur = v;
            while (cur != u) {
                weights.Add(pw[cur]);
                cur = parent[cur];
                nodes.Add(cur);
            }
            nodes.Reverse();
            weights.Reverse();
            int total = 0;
            foreach (int w in weights) total += w;
            int need = (total + 1) / 2, sum = 0, med = u;
            for (int i = 0; i < weights.Count; i++) {
                sum += weights[i];
                med = nodes[i + 1];
                if (sum >= need) break;
            }
            ans[qi] = med;
        }
        return ans;
    }
}
