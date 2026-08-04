// LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution {
    fun longestSubarray(nums: IntArray): Int {
        var left = 0
        var zeros = 0
        var ans = 0
        for (right in nums.indices) {
            if (nums[right] == 0) zeros++
            while (zeros > 1) {
                if (nums[left] == 0) zeros--
                left++
            }
            ans = maxOf(ans, right - left)
        }
        return ans
    }
}
