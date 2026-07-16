// LeetCode 0081 - Search in Rotated Sorted Array II
// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution {
    fun search(nums: IntArray, target: Int): Boolean {
        var left = 0
        var right = nums.size - 1

        while (left <= right) {
            val mid = (left + right) / 2
            if (nums[mid] == target) {
                return true
            }

            if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
                left++
                right--
            } else if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }

        return false
    }
}
