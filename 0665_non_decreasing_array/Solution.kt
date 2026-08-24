// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/


class Solution {
    fun checkPossibility(nums: IntArray): Boolean {
        var edits = 0
        for (i in 1 until nums.size) {
            if (nums[i] < nums[i - 1]) {
                if (++edits > 1) return false
                if (i >= 2 && nums[i] < nums[i - 2]) nums[i] = nums[i - 1]
            }
        }
        return true
    }
}
