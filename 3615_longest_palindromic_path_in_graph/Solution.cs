// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

using System;
using System.Collections.Generic;

public class Solution {
    int ExpandPal(List<int>[] g, string label, int l, int r) {
        var vis = new HashSet<(int, int)>();
        var q = new Queue<(int l, int r, int length)>();
        int len0 = (l != r) ? 2 : 1;
        q.Enqueue((l, r, len0));
        int best = len0;
        vis.Add((Math.Min(l, r), Math.Max(l, r)));
        while (q.Count > 0) {
            var cur = q.Dequeue();
            foreach (int a in g[cur.l]) {
                foreach (int b in g[cur.r]) {
                    if (a == b || label[a] != label[b]) continue;
                    var p = (Math.Min(a, b), Math.Max(a, b));
                    if (vis.Contains(p)) continue;
                    vis.Add(p);
                    int nl = cur.length + 2;
                    best = Math.Max(best, nl);
                    q.Enqueue((a, b, nl));
                }
            }
        }
        return best;
    }

    public int MaxLen(int n, int[][] edges, string label) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int ans = 1;
        for (int i = 0; i < n; i++) {
            ans = Math.Max(ans, ExpandPal(g, label, i, i));
            foreach (int j in g[i]) {
                if (i < j && label[i] == label[j]) ans = Math.Max(ans, ExpandPal(g, label, i, j));
            }
        }
        return ans;
    }
}
