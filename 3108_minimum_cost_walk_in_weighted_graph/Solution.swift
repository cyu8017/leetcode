// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

class Solution {
    func minimumCost(_ n: Int, _ edges: [[Int]], _ query: [[Int]]) -> [Int] {
        var p = Array(0..<n)
        var size = Array(repeating: 1, count: n)
        func find(_ x: Int) -> Int {
            if p[x] != x { p[x] = find(p[x]) }
            return p[x]
        }
        func unite(_ a: Int, _ b: Int) {
            var pa = find(a), pb = find(b)
            if pa == pb { return }
            if size[pa] > size[pb] {
                p[pb] = pa
                size[pa] += size[pb]
            } else {
                p[pa] = pb
                size[pb] += size[pa]
            }
        }
        for e in edges { unite(e[0], e[1]) }
        var g = Array(repeating: -1, count: n)
        for e in edges {
            g[find(e[0])] &= e[2]
        }
        return query.map { q in
            if q[0] == q[1] { return 0 }
            let a = find(q[0]), b = find(q[1])
            return a == b ? g[a] : -1
        }
    }
}
