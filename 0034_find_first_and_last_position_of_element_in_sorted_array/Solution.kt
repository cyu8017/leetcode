// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution {
    fun searchRange(nums: IntArray, target: Int): IntArray {
        if (nums.isEmpty()) {
            return intArrayOf(-1, -1)
        }

        val start = lowerBound(nums, target)
        if (start == nums.size || nums[start] != target) {
            return intArrayOf(-1, -1)
        }

        return intArrayOf(start, upperBound(nums, target) - 1)
    }

    private fun lowerBound(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size

        while (left < right) {
            val mid = (left + right) / 2
            if (nums[mid] < target) {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return left
    }

    private fun upperBound(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size

        while (left < right) {
            val mid = (left + right) / 2
            if (nums[mid] <= target) {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return left
    }
}
