// LeetCode 1464 - Maximum Product of Two Elements in an Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution {
    fun maxProduct(nums: IntArray): Int {
        val sorted = nums.sorted()
        val a = sorted[sorted.size - 2]
        val b = sorted[sorted.size - 1]
        return (a - 1) * (b - 1)
    }
}
