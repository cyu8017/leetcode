// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution {
    fun getMaximumXor(nums: IntArray, maximumBit: Int): IntArray {
        val limit = (1 shl maximumBit) - 1
        var current = 0
        for (num in nums) current = current xor num
        val result = IntArray(nums.size)
        for (i in nums.indices.reversed()) {
            result[nums.size - 1 - i] = current xor limit
            current = current xor nums[i]
        }
        return result
    }
}
