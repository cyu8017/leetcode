// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

private struct MinHeap3 {
    private var a: [(Int, Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].2 <= a[i].2 { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int, Int) {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rgt = 2 * i + 2
                if l < a.count && a[l].2 < a[s].2 { s = l }
                if rgt < a.count && a[rgt].2 < a[s].2 { s = rgt }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}

class Solution {
    func shortestPathWithHops(_ n: Int, _ edges: [[Int]], _ s: Int, _ d: Int, _ k: Int) -> Int {
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        var dist = Array(repeating: Array(repeating: Int.max / 4, count: k + 1), count: n)
        dist[s][0] = 0
        var pq = MinHeap3()
        pq.push((s, 0, 0))
        while !pq.isEmpty {
            let (u, hops, cd) = pq.pop()
            if u == d { return cd }
            if cd > dist[u][hops] { continue }
            for e in g[u] {
                let to = e.0, w = e.1
                if cd + w < dist[to][hops] {
                    dist[to][hops] = cd + w
                    pq.push((to, hops, dist[to][hops]))
                }
                if hops < k && cd < dist[to][hops + 1] {
                    dist[to][hops + 1] = cd
                    pq.push((to, hops + 1, cd))
                }
            }
        }
        return -1
    }
}
