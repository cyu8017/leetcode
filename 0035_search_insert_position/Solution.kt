// LeetCode 0035 - Search Insert Position
// https://leetcode.com/problems/search-insert-position/

class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {
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
}
