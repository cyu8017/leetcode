// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/


class Solution {
    private lateinit var g: Array<MutableList<Int>>
    private lateinit var coins: IntArray
    private var k = 0
    private val memo = HashMap<Long, Int>()

    fun maximumPoints(edges: Array<IntArray>, coins: IntArray, k: Int): Int {
        val n = coins.size
        this.coins = coins
        this.k = k
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        memo.clear()
        return dfs(0, -1, 0)
    }

    private fun dfs(u: Int, p: Int, shifts0: Int): Int {
        var shifts = shifts0
        if (shifts > 14) shifts = 14
        val key = (u.toLong() shl 5) or shifts.toLong()
        memo[key]?.let { return it }
        val c = coins[u] shr shifts
        var opt1 = c - k
        var opt2 = c / 2
        for (v in g[u]) {
            if (v == p) continue
            opt1 += dfs(v, u, shifts)
            opt2 += dfs(v, u, shifts + 1)
        }
        val best = maxOf(opt1, opt2)
        memo[key] = best
        return best
    }
}
