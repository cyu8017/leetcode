// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

class Solution {
    class UnionFind(n: Int) {
        val p = IntArray(n) { it }
        val size = IntArray(n) { 1 }
        var cnt = n
        fun find(x0: Int): Int {
            var x = x0
            if (p[x] != x) p[x] = find(p[x])
            return p[x]
        }
        fun unite(a: Int, b: Int): Boolean {
            var pa = find(a)
            var pb = find(b)
            if (pa == pb) return false
            if (size[pa] > size[pb]) {
                p[pb] = pa
                size[pa] += size[pb]
            } else {
                p[pa] = pb
                size[pb] += size[pa]
            }
            cnt--
            return true
        }
    }

    var N = 0
    var K = 0
    lateinit var E: Array<IntArray>

    fun check(lim: Int): Boolean {
        val uf = UnionFind(N)
        for (e in E) if (e[2] >= lim) uf.unite(e[0], e[1])
        var rem = K
        for (e in E) {
            if (e[2] * 2 >= lim && rem > 0) {
                if (uf.unite(e[0], e[1])) rem--
            }
        }
        return uf.cnt == 1
    }

    fun maxStability(n: Int, edges: Array<IntArray>, k: Int): Int {
        N = n
        E = edges
        K = k
        val uf = UnionFind(n)
        var mn = 1000000
        for (e in edges) {
            if (e[3] == 1) {
                mn = minOf(mn, e[2])
                if (!uf.unite(e[0], e[1])) return -1
            }
        }
        for (e in edges) uf.unite(e[0], e[1])
        if (uf.cnt > 1) return -1
        var l = 1
        var r = mn
        while (l < r) {
            val mid = (l + r + 1) shr 1
            if (check(mid)) l = mid
            else r = mid - 1
        }
        return l
    }
}
