// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

public class Solution {
    public int MinimumCost(int n, int[][] highways, int discounts) {
        var g = new List<(int v, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var h in highways) {
            g[h[0]].Add((h[1], h[2]));
            g[h[1]].Add((h[0], h[2]));
        }
        const int INF = 1 << 30;
        int[][] dist = new int[n][];
        for (int i = 0; i < n; i++) {
            dist[i] = new int[discounts + 1];
            Array.Fill(dist[i], INF);
        }
        var pq = new PriorityQueue<(int cost, int city, int disc), int>();
        dist[0][discounts] = 0;
        pq.Enqueue((0, 0, discounts), 0);
        while (pq.Count > 0) {
            var (cost, city, disc) = pq.Dequeue();
            if (city == n - 1) return cost;
            if (cost > dist[city][disc]) continue;
            foreach (var (v, w) in g[city]) {
                if (cost + w < dist[v][disc]) {
                    dist[v][disc] = cost + w;
                    pq.Enqueue((dist[v][disc], v, disc), dist[v][disc]);
                }
                if (disc > 0 && cost + w / 2 < dist[v][disc - 1]) {
                    dist[v][disc - 1] = cost + w / 2;
                    pq.Enqueue((dist[v][disc - 1], v, disc - 1), dist[v][disc - 1]);
                }
            }
        }
        return -1;
    }
}
