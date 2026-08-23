// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

using System.Collections.Generic;

public class Solution {
    public int SecondMinimum(int n, int[][] edges, int time, int change) {
        var g = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        int[] dist1 = new int[n + 1], dist2 = new int[n + 1];
        System.Array.Fill(dist1, -1);
        System.Array.Fill(dist2, -1);
        var q = new Queue<(int u, int d)>();
        q.Enqueue((1, 0));
        dist1[1] = 0;
        while (q.Count > 0) {
            var (u, d) = q.Dequeue();
            foreach (int v in g[u]) {
                int nd = d + 1;
                if (dist1[v] == -1) { dist1[v] = nd; q.Enqueue((v, nd)); }
                else if (dist2[v] == -1 && nd > dist1[v]) { dist2[v] = nd; q.Enqueue((v, nd)); }
            }
        }
        int steps = dist2[n], ans = 0;
        for (int i = 0; i < steps; i++) {
            if ((ans / change) % 2 == 1) ans += change - ans % change;
            ans += time;
        }
        return ans;
    }
}
