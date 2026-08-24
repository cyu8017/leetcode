// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

class Solution {
    fun evenProduct(nums: IntArray): Long {
            var n: Long = nums.size
            var total: Long = n * (n + 1) / 2
            var oddLen: Long = 0
            var odd: Long = 0
            for (x in nums) {
                if (x % 2 == 1) {
                    odd = odd + 1
                    oddLen +=odd
                } else {
                    odd = 0
                }
            }
            return total - oddLen
    }
}
