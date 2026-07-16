// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution {
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        for (number in nums) {
            val index = kotlin.math.abs(number) - 1
            if (nums[index] > 0) {
                nums[index] = -nums[index]
            }
        }
        return nums.indices.filter { nums[it] > 0 }.map { it + 1 }
    }
}
