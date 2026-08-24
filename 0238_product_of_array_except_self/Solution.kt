// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val length = nums.size
        val result = IntArray(length) { 1 }
        var prefix = 1
        for (index in 0 until length) {
            result[index] = prefix
            prefix *= nums[index]
        }
        var suffix = 1
        for (index in length - 1 downTo 0) {
            result[index] *= suffix
            suffix *= nums[index]
        }
        return result
    }
}
