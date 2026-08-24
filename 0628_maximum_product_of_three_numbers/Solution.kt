// LeetCode 0628 - Maximum Product of Three Numbers
// https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution {
    fun maximumProduct(nums: IntArray): Int {
        nums.sort()
        val n = nums.size
        return maxOf(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[0] * nums[1] * nums[n - 1])
    }
}
