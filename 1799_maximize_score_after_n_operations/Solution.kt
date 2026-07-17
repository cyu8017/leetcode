// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

class Solution {
    fun maxScore(nums: IntArray): Int {
        val n = nums.size
        val memo = IntArray(1 shl n) { -1 }

        fun gcd(a: Int, b: Int): Int {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            return x
        }

        fun dp(mask: Int): Int {
            if (mask == (1 shl n) - 1) return 0
            if (memo[mask] != -1) return memo[mask]
            val step = Integer.bitCount(mask) / 2 + 1
            var best = 0
            for (i in 0 until n) {
                if (mask shr i and 1 == 1) continue
                for (j in i + 1 until n) {
                    if (mask shr j and 1 == 1) continue
                    best = maxOf(
                        best,
                        step * gcd(nums[i], nums[j]) + dp(mask or (1 shl i) or (1 shl j))
                    )
                }
            }
            memo[mask] = best
            return best
        }

        return dp(0)
    }
}
