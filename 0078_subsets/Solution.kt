// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>(emptyList())

        for (num in nums) {
            val size = result.size
            for (i in 0 until size) {
                result.add(result[i] + num)
            }
        }

        return result
    }
}
