// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution {
    fun longestMonotonicSubarray(nums: IntArray): Int {
        var ans = 1
        var t = 1
        for (i in 1 until nums.size) {
            if (nums[i - 1] < nums[i]) {
                t++
                ans = maxOf(ans, t)
            } else t = 1
        }
        t = 1
        for (i in 1 until nums.size) {
            if (nums[i - 1] > nums[i]) {
                t++
                ans = maxOf(ans, t)
            } else t = 1
        }
        return ans
    }
}
