// LeetCode 0075 - Sort Colors
// https://leetcode.com/problems/sort-colors/

class Solution {
    fun sortColors(nums: IntArray) {
        var low = 0
        var mid = 0
        var high = nums.size - 1

        while (mid <= high) {
            when (nums[mid]) {
                0 -> {
                    val tmp = nums[low]
                    nums[low] = nums[mid]
                    nums[mid] = tmp
                    low++
                    mid++
                }
                1 -> mid++
                else -> {
                    val tmp = nums[mid]
                    nums[mid] = nums[high]
                    nums[high] = tmp
                    high--
                }
            }
        }
    }
}
