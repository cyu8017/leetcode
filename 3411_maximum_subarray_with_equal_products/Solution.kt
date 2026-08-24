// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

class Solution {
    private fun gcd(a: Int, b: Int): Int {
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }

    fun maxLength(nums: IntArray): Int {
        var n = nums.size
        var ans = 1
        for (i in 0 until n) {
            var prod = 1
            var g = 0
            var l = 1
            for (j in i until n) {
                if (prod > 1_000_000_000L / nums[j]) break
                prod *= nums[j]
                if (g == 0) {
                    g = nums[j]
                    l = nums[j]
                } else {
                    g = gcd(g, nums[j])
                    l = l / gcd(l, nums[j]) * nums[j]
                }
                if (prod == l * g && j - i + 1 > ans) ans = j - i + 1
            }
        }
        return ans
    }
}
