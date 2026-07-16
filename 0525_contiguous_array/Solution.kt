// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

class Solution {
    fun findMaxLength(nums: IntArray): Int {
        val counts = mutableMapOf(0 to -1)
        var balance = 0
        var best = 0
        for ((index, num) in nums.withIndex()) {
            balance += if (num == 1) 1 else -1
            val previous = counts[balance]
            if (previous != null) {
                best = maxOf(best, index - previous)
            } else {
                counts[balance] = index
            }
        }
        return best
    }
}
