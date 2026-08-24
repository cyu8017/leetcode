// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

class Solution {
    fun sortByAbsoluteValue(nums: IntArray): IntArray {
        val boxed = nums.toTypedArray()
        boxed.sortBy { kotlin.math.abs(it) }
        for (i in nums.indices) nums[i] = boxed[i]
        return nums
    }
}
