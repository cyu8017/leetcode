// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

class Solution {
    private fun gcd(a0: Long, b0: Long): Long {
        var a = a0
        var b = b0
        while (b != 0L) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }

    fun maxPairStrength(nums: IntArray): Long {
        val n = nums.size
        var ans = 0L
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val g = gcd(nums[i].toLong(), nums[j].toLong())
                val x = nums[i].toLong() * nums[j] / (g * g)
                ans = maxOf(ans, x)
            }
        }
        return ans
    }
}
