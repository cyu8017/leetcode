// LeetCode 1953
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

class Solution {
    fun numberOfWeeks(milestones: IntArray): Long {
        val total = milestones.sumOf { it.toLong() }
        val mx = milestones.maxOrNull()!!.toLong()
        val rest = total - mx
        return if (mx > rest + 1) 2 * rest + 1 else total
    }
}
