// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

class Solution {
    fun singleNumber(nums: IntArray): IntArray {
        var xorAll = 0
        for (num in nums) {
            xorAll = xorAll xor num
        }
        val diff = xorAll and -xorAll
        var first = 0
        var second = 0
        for (num in nums) {
            if (num and diff != 0) {
                first = first xor num
            } else {
                second = second xor num
            }
        }
        return intArrayOf(first, second)
    }
}
