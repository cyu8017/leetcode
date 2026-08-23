// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

using System.Collections.Generic;

public class Solution {
    List<int>[] BuildTree(int n, int[][] edges) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        return g;
    }

    int CountWithin(List<int>[] g, int start, int k) {
        if (k < 0) return 0;
        int n = g.Length;
        bool[] vis = new bool[n];
        var q = new Queue<(int, int)>();
        q.Enqueue((start, 0));
        vis[start] = true;
        int cnt = 0;
        while (q.Count > 0) {
            var (u, d) = q.Dequeue();
            cnt++;
            if (d == k) continue;
            foreach (int v in g[u]) {
                if (!vis[v]) {
                    vis[v] = true;
                    q.Enqueue((v, d + 1));
                }
            }
        }
        return cnt;
    }

    public int[] MaxTargetNodes(int[][] edges1, int[][] edges2, int k) {
        int n = edges1.Length + 1;
        int m = edges2.Length + 1;
        var g1 = BuildTree(n, edges1);
        var g2 = BuildTree(m, edges2);
        int[] cnt1 = new int[n];
        for (int i = 0; i < n; i++) cnt1[i] = CountWithin(g1, i, k);
        int best2 = 0;
        if (k > 0) {
            for (int i = 0; i < m; i++) {
                int c = CountWithin(g2, i, k - 1);
                if (c > best2) best2 = c;
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = cnt1[i] + best2;
        return ans;
    }
}
