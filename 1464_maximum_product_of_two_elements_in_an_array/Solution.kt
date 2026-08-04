// LeetCode 1464 - Maximum Product of Two Elements in an Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution {
    fun maxProduct(nums: IntArray): Int {
        nums.sort()
        val n = nums.size
        return (nums[n - 2] - 1) * (nums[n - 1] - 1)
    }
}
