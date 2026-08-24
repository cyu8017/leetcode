// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

class Solution {
    private class UnionFind {
        val p = HashMap<Long, Long>()
        val size = HashMap<Long, Int>()

        fun find(x: Long): Long {
            if (!p.containsKey(x)) {
                p[x] = x
                size[x] = 1
            }
            if (p[x] != x) p[x] = find(p[x]!!)
            return p[x]!!
        }

        fun unite(a: Long, b: Long): Boolean {
            val pa = find(a)
            val pb = find(b)
            if (pa == pb) return false
            if (size[pa]!! > size[pb]!!) {
                p[pb] = pa
                size[pa] = size[pa]!! + size[pb]!!
            } else {
                p[pa] = pb
                size[pb] = size[pb]!! + size[pa]!!
            }
            return true
        }
    }

    fun maxActivated(points: Array<IntArray>): Int {
        val uf = UnionFind()
        val m = 3000000000L
        for (pt in points) uf.unite(pt[0].toLong(), pt[1] + m)
        val cnt = HashMap<Long, Int>()
        for (pt in points) {
            val r = uf.find(pt[0].toLong())
            cnt[r] = cnt.getOrDefault(r, 0) + 1
        }
        var mx1 = 0
        var mx2 = 0
        for (x in cnt.values) {
            if (mx1 < x) {
                mx2 = mx1
                mx1 = x
            } else if (mx2 < x) {
                mx2 = x
            }
        }
        return mx1 + mx2 + 1
    }
}
