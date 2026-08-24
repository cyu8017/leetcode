// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/


class Solution {
    fun findLHS(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (num in nums) freq[num] = freq.getOrDefault(num, 0) + 1
        var best = 0
        for ((num, count) in freq) {
            val next = freq[num + 1]
            if (next != null) best = maxOf(best, count + next)
        }
        return best
    }
}
