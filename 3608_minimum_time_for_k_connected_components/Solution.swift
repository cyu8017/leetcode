// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

class Solution {
    class UnionFind {
        var p: [Int]
        var size: [Int]
        init(_ n: Int) {
            p = Array(0..<n)
            size = Array(repeating: 1, count: n)
        }
        func find(_ x: Int) -> Int {
            if p[x] != x { p[x] = find(p[x]) }
            return p[x]
        }
        func unite(_ a: Int, _ b: Int) -> Bool {
            var pa = find(a), pb = find(b)
            if pa == pb { return false }
            if size[pa] > size[pb] {
                p[pb] = pa
                size[pa] += size[pb]
            } else {
                p[pa] = pb
                size[pb] += size[pa]
            }
            return true
        }
    }

    func minTime(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        var edges = edges.sorted { $0[2] < $1[2] }
        let uf = UnionFind(n)
        var cnt = n
        for i in stride(from: edges.count - 1, through: 0, by: -1) {
            if uf.unite(edges[i][0], edges[i][1]) {
                cnt -= 1
                if cnt < k { return edges[i][2] }
            }
        }
        return 0
    }
}
