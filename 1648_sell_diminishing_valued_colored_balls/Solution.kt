// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution {
    fun maxProfit(inventory: IntArray, orders: Int): Int {
        val MOD = 1_000_000_007L
        inventory.sortDescending()
        val inv = inventory + intArrayOf(0)
        var remain = orders.toLong()
        var ans = 0L
        for (i in 0 until inv.size - 1) {
            val width = (i + 1).toLong()
            val high = inv[i].toLong()
            val low = inv[i + 1].toLong()
            val balls = width * (high - low)
            val take = minOf(remain, balls)
            val full = take / width
            val rem = take % width
            val bottom = high - full
            ans += width * (high + bottom + 1) * full / 2 + rem * bottom
            remain -= take
            if (remain == 0L) break
        }
        return (ans % MOD).toInt()
    }
}
