// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

using System;
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

    int[] BipartiteCount(List<int>[] g, int[] color) {
        int n = g.Length;
        for (int i = 0; i < n; i++) color[i] = -1;
        var q = new Queue<int>();
        q.Enqueue(0);
        color[0] = 0;
        int[] cnt = new int[] { 1, 0 };
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in g[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    cnt[color[v]]++;
                    q.Enqueue(v);
                }
            }
        }
        return cnt;
    }

    public int[] MaxTargetNodes(int[][] edges1, int[][] edges2) {
        int n = edges1.Length + 1;
        int m = edges2.Length + 1;
        var g1 = BuildTree(n, edges1);
        var g2 = BuildTree(m, edges2);
        int[] color1 = new int[n], color2 = new int[m];
        var c1 = BipartiteCount(g1, color1);
        var c2 = BipartiteCount(g2, color2);
        int best2 = Math.Max(c2[0], c2[1]);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = c1[color1[i]] + best2;
        return ans;
    }
}
