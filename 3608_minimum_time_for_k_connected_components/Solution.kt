// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

class Solution {
    class UnionFind(n: Int) {
        val p = IntArray(n) { it }
        val size = IntArray(n) { 1 }
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
            return true
        }
    }

    fun minTime(n: Int, edges: Array<IntArray>, k: Int): Int {
        edges.sortBy { it[2] }
        val uf = UnionFind(n)
        var cnt = n
        for (i in edges.size - 1 downTo 0) {
            if (uf.unite(edges[i][0], edges[i][1])) {
                cnt--
                if (cnt < k) return edges[i][2]
            }
        }
        return 0
    }
}
