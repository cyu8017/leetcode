// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution {
    fun subsetXORSum(nums: IntArray): Int {
        var bits = 0
        for (num in nums) bits = bits or num
        var total = 0
        var bit = 1
        while (bit <= bits) {
            if (bits and bit != 0) total += bit
            bit = bit shl 1
        }
        return total shl (nums.size - 1)
    }
}
