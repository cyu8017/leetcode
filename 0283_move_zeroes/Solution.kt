// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

class Solution {
    fun moveZeroes(nums: IntArray) {
        var insert = 0
        for (num in nums) {
            if (num != 0) {
                nums[insert] = num
                insert++
            }
        }
        for (index in insert until nums.size) {
            nums[index] = 0
        }
    }
}
