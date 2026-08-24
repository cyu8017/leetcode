// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

class Solution {
    fun longestNiceSubarray(nums: IntArray): Int {
        var used = 0
        var left = 0
        var ans = 0
        for (right in nums.indices) {
            while ((used and nums[right]) != 0) {
                used = used xor nums[left]
                left++
            }
            used = used or nums[right]
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }
}
