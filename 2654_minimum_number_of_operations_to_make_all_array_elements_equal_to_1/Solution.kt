// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

class Solution {
    fun minOperations(nums: IntArray): Int {
        val n = nums.size
        var ones = 0
        for (x in nums) if (x == 1) ones++
        if (ones > 0) return n - ones
        var best = n + 1
        for (i in 0 until n) {
            var g = 0
            for (j in i until n) {
                g = gcd(g, nums[j])
                if (g == 1) {
                    best = minOf(best, j - i)
                    break
                }
            }
        }
        if (best == n + 1) return -1
        return best + n - 1
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
