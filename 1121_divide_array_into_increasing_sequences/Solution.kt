// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

class Solution {
    fun canDivideIntoSubsequences(nums: IntArray, k: Int): Boolean {
        val count = mutableMapOf<Int, Int>()
        var maxFreq = 0
        for (x in nums) {
            val c = count.getOrDefault(x, 0) + 1
            count[x] = c
            maxFreq = maxOf(maxFreq, c)
        }
        return nums.size >= k * maxFreq
    }
}
