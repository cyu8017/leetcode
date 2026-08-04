// LeetCode 1909 - Remove One Element To Make The Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution {
    fun canBeIncreasing(nums: IntArray): Boolean {
        fun check(skip: Int): Boolean {
            var prev: Int? = null
            for (i in nums.indices) {
                if (i == skip) continue
                val x = nums[i]
                if (prev != null && x <= prev) return false
                prev = x
            }
            return true
        }
        for (i in 1 until nums.size) {
            if (nums[i] <= nums[i - 1]) return check(i - 1) || check(i)
        }
        return true
    }
}
