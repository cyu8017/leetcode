// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

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
    func minimumCost(_ start: [Int], _ target: [Int], _ specialRoads: [[Int]]) -> Int {
        var points: [[Int]] = [start, target]
        for r in specialRoads {
            points.append([r[0], r[1]])
            points.append([r[2], r[3]])
        }
        let N = points.count
        var g = Array(repeating: [(Int, Int)](), count: N)
        for i in 0..<N {
            for j in 0..<N where i != j {
                g[i].append((j, man(points[i], points[j])))
            }
        }
        for r in specialRoads {
            var u = -1, v = -1
            for i in 0..<N {
                if points[i][0] == r[0] && points[i][1] == r[1] { u = i }
                if points[i][0] == r[2] && points[i][1] == r[3] { v = i }
            }
            if u >= 0 && v >= 0 { g[u].append((v, r[4])) }
        }
        var dist = Array(repeating: Int.max / 4, count: N)
        dist[0] = 0
        var pq = MinHeap()
        pq.push((0, 0))
        while !pq.isEmpty {
            let (id, cost) = pq.pop()
            if cost > dist[id] { continue }
            for e in g[id] {
                if cost + e.1 < dist[e.0] {
                    dist[e.0] = cost + e.1
                    pq.push((e.0, dist[e.0]))
                }
            }
        }
        return dist[1]
    }

    private func man(_ a: [Int], _ b: [Int]) -> Int {
        abs(a[0] - b[0]) + abs(a[1] - b[1])
    }
}
