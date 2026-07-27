// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution {
    fun getSumAbsoluteDifferences(nums: IntArray): IntArray {
        val total = nums.sum()
        var left = 0
        val n = nums.size
        val ans = IntArray(n)
        for (i in nums.indices) {
            val x = nums[i]
            ans[i] = x * i - left + (total - left - x) - x * (n - i - 1)
            left += x
        }
        return ans
    }
}
