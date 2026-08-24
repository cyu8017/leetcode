// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

class Solution {
    fun minimumSplits(nums: IntArray): Int {
        var ans = 1
        var g = nums[0]
        for (i in 1 until nums.size) {
            val ng = gcd(g, nums[i])
            if (ng == 1) {
                ans++
                g = nums[i]
            } else {
                g = ng
            }
        }
        return ans
    }

    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }
}
