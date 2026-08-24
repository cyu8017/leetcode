// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

class Solution {
    fun missingNumber(nums: IntArray): Int {
        val length = nums.size
        val expected = length * (length + 1) / 2
        var total = 0
        for (num in nums) {
            total += num
        }
        return expected - total
    }
}
