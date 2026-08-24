// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

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
    func minimumDistance(_ n: Int, _ edges: [[Int]], _ s: Int, _ marked: [Int]) -> Int {
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges { g[e[0]].append((e[1], e[2])) }
        let mark = Set(marked)
        var dist = Array(repeating: Int.max / 4, count: n)
        dist[s] = 0
        var pq = MinHeap()
        pq.push((s, 0))
        while !pq.isEmpty {
            let (u, d) = pq.pop()
            if mark.contains(u) { return d }
            if d > dist[u] { continue }
            for e in g[u] where d + e.1 < dist[e.0] {
                dist[e.0] = d + e.1
                pq.push((e.0, dist[e.0]))
            }
        }
        return -1
    }
}
