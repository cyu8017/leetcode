// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

class Solution {
    fun subarrayGCD(nums: IntArray, k: Int): Int {
        var ans = 0
        val n = nums.size
        for (i in 0 until n) {
            var g = 0
            for (j in i until n) {
                g = gcd(g, nums[j])
                if (g < k) break
                if (g == k) ans++
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
