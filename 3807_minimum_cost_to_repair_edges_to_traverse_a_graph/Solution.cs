// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinCost(int n, int[][] edges, int k) {
        Array.Sort(edges, (a, b) => a[2].CompareTo(b[2]));
        bool Check(int idx) {
            var g = new List<int>[n];
            for (int i = 0; i < n; i++) g[i] = new List<int>();
            for (int i = 0; i <= idx; i++) {
                g[edges[i][0]].Add(edges[i][1]);
                g[edges[i][1]].Add(edges[i][0]);
            }
            var q = new List<int> { 0 };
            bool[] vis = new bool[n];
            vis[0] = true;
            int dist = 0;
            while (q.Count > 0) {
                var nq = new List<int>();
                foreach (int u in q) {
                    if (u == n - 1) return dist <= k;
                    foreach (int v in g[u]) {
                        if (!vis[v]) {
                            vis[v] = true;
                            nq.Add(v);
                        }
                    }
                }
                q = nq;
                dist++;
            }
            return false;
        }
        int m = edges.Length;
        if (m == 0) return -1;
        int l = 0, r = m - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (Check(mid)) r = mid;
            else l = mid + 1;
        }
        if (Check(l)) return edges[l][2];
        return -1;
    }
}
