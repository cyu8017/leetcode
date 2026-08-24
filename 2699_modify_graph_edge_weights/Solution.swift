// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

private struct MinHeap {
    private var a: [(Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].1 <= a[i].1 { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int) {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rgt = 2 * i + 2
                if l < a.count && a[l].1 < a[s].1 { s = l }
                if rgt < a.count && a[rgt].1 < a[s].1 { s = rgt }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}

class Solution {
    private let INF = 2_000_000_000

    func modifiedGraphEdges(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int, _ target: Int) -> [[Int]] {
        var edges = edges
        var d = dijkstra(n, edges, source, true)
        if d[destination] < target { return [] }
        var matched = d[destination] == target
        for i in edges.indices {
            if edges[i][2] != -1 { continue }
            if matched {
                edges[i][2] = INF
                continue
            }
            edges[i][2] = 1
            d = dijkstra(n, edges, source, false)
            if d[destination] <= target {
                edges[i][2] += target - d[destination]
                matched = true
            }
        }
        d = dijkstra(n, edges, source, false)
        if d[destination] != target { return [] }
        return edges
    }

    private func dijkstra(_ n: Int, _ edges: [[Int]], _ source: Int, _ ignoreNeg: Bool) -> [Int] {
        var dist = Array(repeating: INF, count: n)
        dist[source] = 0
        var pq = MinHeap()
        pq.push((source, 0))
        while !pq.isEmpty {
            let (u, d) = pq.pop()
            if d != dist[u] { continue }
            for e in edges {
                let a = e[0], b = e[1]
                var w = e[2]
                if a != u && b != u { continue }
                let to = a == u ? b : a
                if w == -1 {
                    if ignoreNeg { continue }
                    w = 1
                }
                if d + w < dist[to] {
                    dist[to] = d + w
                    pq.push((to, dist[to]))
                }
            }
        }
        return dist
    }
}
