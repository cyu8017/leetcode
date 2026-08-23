// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        final int INF = Integer.MAX_VALUE / 4;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;
        for (int i = 0; i <= k; i++) {
            int[] nxt = dist.clone();
            for (int[] flight : flights) {
                int u = flight[0], v = flight[1], price = flight[2];
                if (dist[u] != INF && dist[u] + price < nxt[v]) {
                    nxt[v] = dist[u] + price;
                }
            }
            dist = nxt;
        }
        return dist[dst] == INF ? -1 : dist[dst];
    }
}
