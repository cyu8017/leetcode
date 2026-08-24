// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution {
    fun check(nums: IntArray): Boolean {
        val n = nums.size
        var drops = 0
        for (i in 0 until n) {
            if (nums[i] > nums[(i + 1) % n]) {
                drops++
            }
        }
        return drops <= 1
    }
}
