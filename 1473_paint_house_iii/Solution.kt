// LeetCode 1473 - Paint House III
// https://leetcode.com/problems/paint-house-iii/

class Solution {
    fun minCost(houses: IntArray, cost: Array<IntArray>, m: Int, n: Int, target: Int): Int {
        val inf = 1e15.toLong()
        var dp = HashMap<Long, Long>()
        dp[key(0, 0)] = 0L
        for (i in houses.indices) {
            val painted = houses[i]
            val nxt = HashMap<Long, Long>()
            val colors = if (painted != 0) listOf(painted) else (1..n).toList()
            for ((state, value) in dp) {
                val prev = (state shr 32).toInt()
                val groups = state.toInt()
                for (color in colors) {
                    val ng = groups + if (color != prev) 1 else 0
                    if (ng <= target) {
                        val nv = value + if (painted != 0) 0L else cost[i][color - 1].toLong()
                        val nk = key(color, ng)
                        nxt[nk] = minOf(nxt.getOrDefault(nk, inf), nv)
                    }
                }
            }
            dp = nxt
        }
        var ans = inf
        for ((state, value) in dp) {
            if (state.toInt() == target) ans = minOf(ans, value)
        }
        return if (ans == inf) -1 else ans.toInt()
    }

    private fun key(a: Int, b: Int): Long = (a.toLong() shl 32) or (b.toLong() and 0xffffffffL)
}
