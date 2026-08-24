
// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

class Solution {
    private lateinit var g: Array<MutableList<Int>>
    private lateinit var price: IntArray
    private lateinit var cnt: IntArray

    fun minimumTotalPrice(n: Int, edges: Array<IntArray>, price: IntArray, trips: Array<IntArray>): Int {
        this.price = price
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        cnt = IntArray(n)
        for (t in trips) path(t[0], -1, t[1])
        val res = dfs(0, -1)
        return minOf(res[0], res[1])
    }

    private fun path(u: Int, p: Int, target: Int): Boolean {
        if (u == target) {
            cnt[u]++
            return true
        }
        for (v in g[u]) {
            if (v == p) continue
            if (path(v, u, target)) {
                cnt[u]++
                return true
            }
        }
        return false
    }

    private fun dfs(u: Int, p: Int): IntArray {
        var full = price[u] * cnt[u]
        var half = full / 2
        for (v in g[u]) {
            if (v == p) continue
            val child = dfs(v, u)
            full += minOf(child[0], child[1])
            half += child[0]
        }
        return intArrayOf(full, half)
    }
}
