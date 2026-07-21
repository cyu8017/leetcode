// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution {
    fun arraySign(nums: IntArray): Int {
        var sign = 1
        for (num in nums) {
            if (num == 0) return 0
            if (num < 0) sign = -sign
        }
        return sign
    }
}
