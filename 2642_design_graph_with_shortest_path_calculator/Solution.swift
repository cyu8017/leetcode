// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

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

class Graph {
    private var g: [[(Int, Int)]]

    init(_ n: Int, _ edges: [[Int]]) {
        g = Array(repeating: [], count: n)
        for e in edges { g[e[0]].append((e[1], e[2])) }
    }

    func addEdge(_ edge: [Int]) {
        g[edge[0]].append((edge[1], edge[2]))
    }

    func shortestPath(_ node1: Int, _ node2: Int) -> Int {
        let n = g.count
        var dist = Array(repeating: 1 << 30, count: n)
        dist[node1] = 0
        var pq = MinHeap()
        pq.push((node1, 0))
        while !pq.isEmpty {
            let (u, d) = pq.pop()
            if u == node2 { return d }
            if d > dist[u] { continue }
            for e in g[u] {
                let nd = d + e.1
                if nd < dist[e.0] {
                    dist[e.0] = nd
                    pq.push((e.0, nd))
                }
            }
        }
        return -1
    }
}
