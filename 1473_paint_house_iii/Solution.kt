// LeetCode 1473 - Paint House III
// https://leetcode.com/problems/paint-house-iii/

class Solution {
    fun minCost(houses: IntArray, cost: Array<IntArray>, m: Int, n: Int, target: Int): Int {
        val inf = 1e15.toLong()
        var dp = mutableMapOf((0 to 0) to 0L)
        for (i in houses.indices) {
            val painted = houses[i]
            val nxt = mutableMapOf<Pair<Int, Int>, Long>()
            val colors = if (painted != 0) listOf(painted) else (1..n).toList()
            for ((key, value) in dp) {
                val (prev, groups) = key
                for (color in colors) {
                    val ng = groups + if (color != prev) 1 else 0
                    if (ng <= target) {
                        val nv = value + if (painted != 0) 0 else cost[i][color - 1].toLong()
                        val cur = nxt.getOrDefault(color to ng, inf)
                        nxt[color to ng] = minOf(cur, nv)
                    }
                }
            }
            dp = nxt
        }
        val ans = dp.filter { it.key.second == target }.values.minOrNull() ?: inf
        return if (ans == inf) -1 else ans.toInt()
    }
}
