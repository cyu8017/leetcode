// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

using System.Collections.Generic;

public class Solution {
    private List<int>[] adj;
    private int[] vals;
    private int[] ans;
    private List<(int Depth, int Node)>[] path;

    public int[] GetCoprimes(int[] nums, int[][] edges) {
        int n = nums.Length;
        vals = nums;
        adj = new List<int>[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new List<int>();
        }
        foreach (var e in edges) {
            adj[e[0]].Add(e[1]);
            adj[e[1]].Add(e[0]);
        }
        ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = -1;
        }
        path = new List<(int, int)>[51];
        for (int v = 0; v <= 50; v++) {
            path[v] = new List<(int, int)>();
        }
        Dfs(0, -1, 0);
        return ans;
    }

    private void Dfs(int node, int parent, int depth) {
        int bestDepth = -1;
        int bestNode = -1;
        int val = vals[node];
        for (int d = 1; d <= 50; d++) {
            if (Gcd(val, d) == 1 && path[d].Count > 0) {
                var cand = path[d][path[d].Count - 1];
                if (cand.Depth > bestDepth) {
                    bestDepth = cand.Depth;
                    bestNode = cand.Node;
                }
            }
        }
        ans[node] = bestNode;
        path[val].Add((depth, node));
        foreach (int nxt in adj[node]) {
            if (nxt != parent) {
                Dfs(nxt, node, depth + 1);
            }
        }
        path[val].RemoveAt(path[val].Count - 1);
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
