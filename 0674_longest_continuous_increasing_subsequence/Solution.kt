// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/


class Solution {
    fun findLengthOfLCIS(nums: IntArray): Int {
        var best = 1
        var cur = 1
        for (i in 1 until nums.size) {
            if (nums[i] > nums[i - 1]) {
                cur++
                best = maxOf(best, cur)
            } else {
                cur = 1
            }
        }
        return if (nums.isEmpty()) 0 else best
    }
}
