// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution {
    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        val INF = Int.MAX_VALUE / 4
        var dist = IntArray(n)
        dist.fill(INF)
        dist[src] = 0
        for (i in 0 until = k) {
            var nxt = dist.clone()
            for (flight in flights) {
                var u = flight[0]
                var v = flight[1]
                var price = flight[2]
                if (dist[u] != INF && dist[u] + price < nxt[v]) {
                    nxt[v] = dist[u] + price
                }
            }
            dist = nxt
        }
        return dist[dst] ==if (INF) -1 else dist[dst]
    }
}
