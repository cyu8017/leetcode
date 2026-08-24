// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

class Solution {
    fun longestSubarray(nums: IntArray): Int {
        var f = 2
        var ans = f
        for (i in 2 until nums.size) {
            if (nums[i] == nums[i - 1] + nums[i - 2]) {
                f++
                ans = maxOf(ans, f)
            } else f = 2
        }
        return ans
    }
}
