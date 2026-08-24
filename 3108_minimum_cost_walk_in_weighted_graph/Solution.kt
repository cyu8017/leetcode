// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

class Solution {
    static class UnionFind {
        int[] p, size
        constructor(n: Int) {
            p = IntArray(n)
            size = IntArray(n)
            for (i in 0 until n) {
                p[i] = i
                size[i] = 1
            }
        }
        fun find(x: Int): Int {
            if (p[x] != x) p[x] = find(p[x])
            return p[x]
        }
        fun unite(a: Int, b: Int) {
            var pa = find(a), pb = find(b)
            if (pa == pb) return
            if (size[pa] > size[pb]) {
                p[pb] = pa
                size[pa] += size[pb]
            } else {
                p[pa] = pb
                size[pb] += size[pa]
            }
        }
    }

    fun minimumCost(n: Int, edges: Array<IntArray>, query: Array<IntArray>): IntArray {
        UnionFind uf = UnionFind(n)
        var g = IntArray(n)
        for (i in 0 until n) { g[i] = -1 }
        for (e in edges) { uf.unite(e[0], e[1]) }
        for (e in edges) {
            var root = uf.find(e[0])
            g[root] &= e[2]
        }
        var ans = IntArray(query.size)
        for (i in 0 until query.size) {
            var u = query[i][0]
            var v = query[i][1]
            if (u == v) ans[i] = 0
            else {
                var a = uf.find(u), b = uf.find(v)
                ans[i] =if ((a == b)) g[a] else -1
            }
        }
        return ans
    }
}
