// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution {
    fun maxSumDivThree(nums: IntArray): Int {
        val impossible = Long.MIN_VALUE / 4
        var dp = longArrayOf(0, impossible, impossible)
        for (value in nums) {
            val old = dp.copyOf()
            for (total in 0 until 3) {
                if (old[total] != impossible) {
                    val remainder = ((old[total] + value) % 3).toInt()
                    dp[remainder] = maxOf(dp[remainder], old[total] + value)
                }
            }
        }
        return dp[0].toInt()
    }
}
