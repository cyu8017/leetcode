// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

class Solution {
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

    private fun lcm(a: Int, b: Int): Int = a / gcd(a, b) * b

    fun maxScore(nums: IntArray): Long {
        val n = nums.size
        var gcdAll = nums[0]
        var lcmAll = nums[0]
        for (i in 1 until n) {
            gcdAll = gcd(gcdAll, nums[i])
            lcmAll = lcm(lcmAll, nums[i])
        }
        var ans = gcdAll.toLong() * lcmAll
        for (skip in 0 until n) {
            var g = 0
            var l = 1
            var first = true
            for (i in 0 until n) {
                if (i == skip) continue
                if (first) {
                    g = nums[i]
                    l = nums[i]
                    first = false
                } else {
                    g = gcd(g, nums[i])
                    l = lcm(l, nums[i])
                }
            }
            if (first) continue
            val v = g.toLong() * l
            if (v > ans) ans = v
        }
        return ans
    }
}
