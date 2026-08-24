// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

class Solution {
    fun wiggleSort(nums: IntArray) {
        for (index in 1 until nums.size) {
            if (index % 2 == 1 && nums[index] < nums[index - 1]) {
                val tmp = nums[index]
                nums[index] = nums[index - 1]
                nums[index - 1] = tmp
            } else if (index % 2 == 0 && nums[index] > nums[index - 1]) {
                val tmp = nums[index]
                nums[index] = nums[index - 1]
                nums[index - 1] = tmp
            }
        }
    }
}
