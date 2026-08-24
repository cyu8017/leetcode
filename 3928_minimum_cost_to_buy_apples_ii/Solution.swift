// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/


class Solution {
    func minCostToBuyApples(_ n: Int, _ prices: [Int], _ roads: [[Int]]) -> [Int] {
        var g = Array(repeating: [(to: Int, empty: Int, full: Int)](), count: n)
        for road in roads {
            let empty = road[2], full = road[2] * road[3]
            g[road[0]].append((road[1], empty, full))
            g[road[1]].append((road[0], empty, full))
        }
        let inf = Int.max / 4
        func dijkstra(_ source: Int, _ carrying: Bool) -> [Int] {
            var dist = Array(repeating: inf, count: n)
            dist[source] = 0
            var heap = [(0, source)]
            while !heap.isEmpty {
                heap.sort { $0.0 < $1.0 }
                let cur = heap.removeFirst()
                let d = cur.0, node = cur.1
                if d != dist[node] { continue }
                for e in g[node] {
                    let weight = carrying ? e.full : e.empty
                    let next = d + weight
                    if next < dist[e.to] {
                        dist[e.to] = next
                        heap.append((next, e.to))
                    }
                }
            }
            return dist
        }
        var answer = Array(repeating: 0, count: n)
        for source in 0..<n {
            let emptyDist = dijkstra(source, false)
            let fullDist = dijkstra(source, true)
            var best = prices[source]
            for shop in 0..<n {
                if emptyDist[shop] == inf || fullDist[shop] == inf { continue }
                let total = emptyDist[shop] + fullDist[shop] + prices[shop]
                if total < best { best = total }
            }
            answer[source] = best
        }
        return answer
    }
}
