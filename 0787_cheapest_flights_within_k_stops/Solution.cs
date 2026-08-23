// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

using System;

public class Solution {
    public int FindCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        const int INF = int.MaxValue / 4;
        int[] dist = new int[n];
        Array.Fill(dist, INF);
        dist[src] = 0;
        for (int i = 0; i <= k; i++) {
            int[] nxt = (int[])dist.Clone();
            foreach (var flight in flights) {
                int u = flight[0], v = flight[1], price = flight[2];
                if (dist[u] != INF && dist[u] + price < nxt[v]) nxt[v] = dist[u] + price;
            }
            dist = nxt;
        }
        return dist[dst] == INF ? -1 : dist[dst];
    }
}
