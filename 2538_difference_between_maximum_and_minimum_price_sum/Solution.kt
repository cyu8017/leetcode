// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var price: IntArray
    private var ans = 0L

    fun maxOutput(n: Int, edges: Array<IntArray>, price: IntArray): Long {
        this.price = price
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        ans = 0
        dfs(0, -1)
        return ans
    }

    private fun dfs(u: Int, p: Int): Long {
        var maxChild = 0L
        for (v in g[u]) {
            if (v == p) continue
            val child = dfs(v, u)
            if (child > maxChild) maxChild = child
            if (child > ans) ans = child
        }
        return price[u].toLong() + maxChild
    }
}
