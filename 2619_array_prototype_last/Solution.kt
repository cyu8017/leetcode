// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

class Solution {
    fun last(nums: IntArray): Int {
        if (nums.isEmpty()) return -1
        return nums[nums.size - 1]
    }
}
