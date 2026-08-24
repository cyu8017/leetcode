// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

class Solution {
    fun maximumProduct(nums: IntArray, m: Int): Long {
        var ans = Long.MIN_VALUE
        var mx = Int.MIN_VALUE
        var mi = Int.MAX_VALUE
        for (i in m - 1 until nums.size) {
            var x = nums[i]
            var y = nums[i - m + 1]
            mi = minOf(mi, y)
            mx = maxOf(mx, y)
            ans = maxOf(ans, maxOf(1L * x * mi, 1L * x * mx))
        }
        return ans
    }
}
