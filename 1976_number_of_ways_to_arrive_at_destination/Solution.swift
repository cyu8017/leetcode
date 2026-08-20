// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution {
    func countPaths(_ n: Int, _ roads: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        var g = Array(repeating: [(Int, Int)](), count: n)
        for r in roads {
            g[r[0]].append((r[1], r[2]))
            g[r[1]].append((r[0], r[2]))
        }
        var dist = Array(repeating: Int.max / 4, count: n)
        var ways = Array(repeating: 0, count: n)
        dist[0] = 0
        ways[0] = 1
        var heap: [(Int, Int)] = [(0, 0)]
        func push(_ item: (Int, Int)) {
            heap.append(item)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p].0 <= heap[i].0 { break }
                heap.swapAt(p, i); i = p
            }
        }
        func pop() -> (Int, Int) {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var s = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count && heap[l].0 < heap[s].0 { s = l }
                    if r < heap.count && heap[r].0 < heap[s].0 { s = r }
                    if s == i { break }
                    heap.swapAt(i, s); i = s
                }
            }
            return top
        }
        while !heap.isEmpty {
            let (d, u) = pop()
            if d > dist[u] { continue }
            for (v, w) in g[u] {
                let nd = d + w
                if nd < dist[v] {
                    dist[v] = nd
                    ways[v] = ways[u]
                    push((nd, v))
                } else if nd == dist[v] {
                    ways[v] = (ways[v] + ways[u]) % MOD
                }
            }
        }
        return ways[n - 1]
    }
}
