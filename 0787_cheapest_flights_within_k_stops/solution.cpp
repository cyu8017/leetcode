// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

#include <limits>
#include <vector>

class Solution {
public:
    int findCheapestPrice(int n, std::vector<std::vector<int>>& flights, int src, int dst, int k) {
        const int INF = std::numeric_limits<int>::max() / 4;
        std::vector<int> dist(n, INF);
        dist[src] = 0;
        for (int i = 0; i <= k; ++i) {
            std::vector<int> nxt = dist;
            for (const auto& flight : flights) {
                int u = flight[0];
                int v = flight[1];
                int price = flight[2];
                if (dist[u] != INF && dist[u] + price < nxt[v]) {
                    nxt[v] = dist[u] + price;
                }
            }
            dist.swap(nxt);
        }
        return dist[dst] == INF ? -1 : dist[dst];
    }
};
