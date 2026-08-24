// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

class Solution {
    fun maximumScore(nums: IntArray, multipliers: IntArray): Int {
        val n = nums.size
        val m = multipliers.size
        var next = IntArray(m + 1)
        for (i in m - 1 downTo 0) {
            val cur = IntArray(m + 1)
            for (left in i downTo 0) {
                val right = n - 1 - (i - left)
                val takeLeft = nums[left] * multipliers[i] + next[left + 1]
                val takeRight = nums[right] * multipliers[i] + next[left]
                cur[left] = maxOf(takeLeft, takeRight)
            }
            next = cur
        }
        return next[0]
    }
}
