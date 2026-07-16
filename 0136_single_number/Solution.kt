// LeetCode 0136 - Single Number
// https://leetcode.com/problems/single-number/

class Solution {
    fun singleNumber(nums: IntArray): Int {
        var result = 0
        for (num in nums) result = result xor num
        return result
    }
}
