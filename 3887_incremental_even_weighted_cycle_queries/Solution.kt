// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

class Solution {
    private lateinit var parent: IntArray
    private lateinit var size: IntArray
    private lateinit var parity: IntArray

    private fun find(x: Int): IntArray {
        if (parent[x] == x) return intArrayOf(x, 0)
        val res = find(parent[x])
        val root = res[0]
        val p = res[1]
        parity[x] = parity[x] xor p
        parent[x] = root
        return intArrayOf(root, parity[x])
    }

    fun countValidEdges(n: Int, edges: Array<IntArray>): Int {
        parent = IntArray(n)
        size = IntArray(n)
        parity = IntArray(n)
        for (i in 0 until n) {
            parent[i] = i
            size[i] = 1
        }
        var ans = 0
        for (e in edges) {
            val fu = find(e[0])
            val fv = find(e[1])
            var ru = fu[0]
            var pu = fu[1]
            var rv = fv[0]
            var pv = fv[1]
            if (ru == rv) {
                if ((pu xor pv) == e[2]) ans++
                continue
            }
            if (size[ru] < size[rv]) {
                var t = ru; ru = rv; rv = t
                t = pu; pu = pv; pv = t
            }
            parent[rv] = ru
            parity[rv] = pu xor pv xor e[2]
            size[ru] += size[rv]
            ans++
        }
        return ans
    }
}
