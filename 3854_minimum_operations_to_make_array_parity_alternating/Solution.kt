// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

class Solution {
    fun makeParityAlternating(nums: IntArray): IntArray {
        if (nums.size == 1) return intArrayOf(0, 0)
        var mn = nums[0]
        var mx = nums[0]
        for (x in nums) {
            mn = minOf(mn, x)
            mx = maxOf(mx, x)
        }
        val r0 = f(nums, 0, mn, mx)
        val r1 = f(nums, 1, mn, mx)
        if (r0[0] != r1[0]) return if (r0[0] < r1[0]) r0 else r1
        return if (r0[1] <= r1[1]) r0 else r1
    }

    private fun f(nums: IntArray, k: Int, mn: Int, mx: Int): IntArray {
        var cnt = 0
        var a = Int.MAX_VALUE
        var b = Int.MIN_VALUE
        for (i in nums.indices) {
            var x = nums[i]
            if (((x - i) and 1) != k) {
                cnt++
                if (x == mn) x++
                else if (x == mx) x--
            }
            a = minOf(a, x)
            b = maxOf(b, x)
        }
        return intArrayOf(cnt, maxOf(1, b - a))
    }
}
