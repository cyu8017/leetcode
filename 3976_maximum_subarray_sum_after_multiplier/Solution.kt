// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

class Solution {
    fun maxSubarraySum(nums: IntArray, k: Int): Long {
        val n = nums.size
        val inf = Long.MIN_VALUE / 4
        val f = Array(n + 1) { LongArray(4) { inf } }
        f[0][0] = 0
        var ans = inf
        for (i in 1..n) {
            val x = nums[i - 1].toLong()
            f[i][0] = maxOf(f[i - 1][0], 0L) + x
            f[i][1] = maxOf(maxOf(f[i - 1][0], f[i - 1][1]), 0L) + x * k
            f[i][2] = maxOf(maxOf(f[i - 1][0], f[i - 1][2]), 0L) + x / k
            f[i][3] = maxOf(maxOf(f[i - 1][1], f[i - 1][2]), f[i - 1][3]) + x
            ans = maxOf(ans, maxOf(maxOf(f[i][0], f[i][1]), maxOf(f[i][2], f[i][3])))
        }
        return ans
    }
}
