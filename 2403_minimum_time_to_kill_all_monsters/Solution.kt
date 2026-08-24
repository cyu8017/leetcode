// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

class Solution {
    fun minimumTime(power: IntArray): Long {
        val n = power.size
        val N = 1 shl n
        val dp = LongArray(N) { Long.MAX_VALUE / 4 }
        dp[0] = 0
        for (mask in 0 until N) {
            val killed = Integer.bitCount(mask)
            val gain = killed + 1L
            for (i in 0 until n) {
                if ((mask and (1 shl i)) != 0) continue
                val need = (power[i] + gain - 1) / gain
                val nm = mask or (1 shl i)
                dp[nm] = minOf(dp[nm], dp[mask] + need)
            }
        }
        return dp[N - 1]
    }
}
