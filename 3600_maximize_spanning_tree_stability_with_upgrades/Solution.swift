// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

class Solution {
    class UnionFind {
        var p: [Int]
        var size: [Int]
        var cnt: Int
        init(_ n: Int) {
            p = Array(0..<n)
            size = Array(repeating: 1, count: n)
            cnt = n
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
            cnt -= 1
            return true
        }
    }

    var N = 0, K = 0
    var E = [[Int]]()

    func check(_ lim: Int) -> Bool {
        let uf = UnionFind(N)
        for e in E where e[2] >= lim { _ = uf.unite(e[0], e[1]) }
        var rem = K
        for e in E {
            if e[2] * 2 >= lim && rem > 0 {
                if uf.unite(e[0], e[1]) { rem -= 1 }
            }
        }
        return uf.cnt == 1
    }

    func maxStability(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        N = n
        E = edges
        K = k
        let uf = UnionFind(n)
        var mn = 1000000
        for e in edges {
            if e[3] == 1 {
                mn = min(mn, e[2])
                if !uf.unite(e[0], e[1]) { return -1 }
            }
        }
        for e in edges { _ = uf.unite(e[0], e[1]) }
        if uf.cnt > 1 { return -1 }
        var l = 1, r = mn
        while l < r {
            let mid = (l + r + 1) >> 1
            if check(mid) { l = mid } else { r = mid - 1 }
        }
        return l
    }
}
