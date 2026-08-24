// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

class Solution {
    fun tallestBillboard(rods: IntArray): Int {
        val dp = HashMap<Int, Int>()
        dp[0] = 0
        for (rod in rods) {
            val cur = dp.entries.toList()
            for ((diff, taller) in cur) {
                val key1 = diff + rod
                dp[key1] = maxOf(dp.getOrDefault(key1, 0), taller + rod)
                val nd = kotlin.math.abs(diff - rod)
                val nt = if (diff >= rod) taller else taller - diff + rod
                dp[nd] = maxOf(dp.getOrDefault(nd, 0), nt)
            }
        }
        return dp.getOrDefault(0, 0)
    }
}
