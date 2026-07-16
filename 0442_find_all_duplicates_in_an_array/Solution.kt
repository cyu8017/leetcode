// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution {
    fun findDuplicates(nums: IntArray): List<Int> {
        val result = mutableListOf<Int>()
        for (number in nums) {
            val index = kotlin.math.abs(number) - 1
            if (nums[index] < 0) {
                result.add(kotlin.math.abs(number))
            } else {
                nums[index] = -nums[index]
            }
        }
        return result
    }
}
