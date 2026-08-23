// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

using System.Collections.Generic;

public class Solution {
    public int MinMaxWeight(int n, int[][] edges, int threshold) {
        _ = threshold;
        bool Ok(int mid) {
            var g = new List<int>[n];
            for (int i = 0; i < n; i++) g[i] = new List<int>();
            foreach (var e in edges) {
                int a = e[0], b = e[1], w = e[2];
                if (w <= mid) g[b].Add(a);
            }
            var vis = new bool[n];
            var q = new Queue<int>();
            q.Enqueue(0);
            vis[0] = true;
            int cnt = 1;
            while (q.Count > 0) {
                int u = q.Dequeue();
                foreach (int v in g[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        cnt++;
                        q.Enqueue(v);
                    }
                }
            }
            return cnt == n;
        }
        int lo = 1, hi = 1000001, ans = -1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Ok(mid)) {
                ans = mid;
                hi = mid;
            } else lo = mid + 1;
        }
        return ans;
    }
}
