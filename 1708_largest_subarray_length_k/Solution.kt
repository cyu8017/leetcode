// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

class Solution {
    fun largestSubarray(nums: IntArray, k: Int): IntArray {
        var start = 0
        for (i in 1..(nums.size - k)) {
            if (nums[i] > nums[start]) {
                start = i
            }
        }
        return nums.copyOfRange(start, start + k)
    }
}
