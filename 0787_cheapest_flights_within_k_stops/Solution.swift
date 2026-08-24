// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution {
    func findCheapestPrice(_ n: Int, _ flights: [[Int]], _ src: Int, _ dst: Int, _ k: Int) -> Int {
        let inf = Int.max / 4
        var dist = Array(repeating: inf, count: n)
        dist[src] = 0
        for _ in 0...k {
            var nxt = dist
            for flight in flights {
                let u = flight[0], v = flight[1], price = flight[2]
                if dist[u] != inf && dist[u] + price < nxt[v] {
                    nxt[v] = dist[u] + price
                }
            }
            dist = nxt
        }
        return dist[dst] == inf ? -1 : dist[dst]
    }
}
