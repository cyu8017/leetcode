// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

class Solution {
    fun maxProduct(nums: IntArray): Long {
        nums.sort()
        var n = nums.size
        var a = nums[0]
        var b = nums[1]
        var c = nums[n - 2]
        var d = nums[n - 1]
        val x = 100000
        return maxOf(maxOf(a * b * x, c * d * x), -a * d * x)
    }
}
