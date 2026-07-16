// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        val values = nums.toHashSet()
        var best = 0
        for (num in values) {
            if (num - 1 in values) continue
            var length = 1
            while (num + length in values) length++
            best = maxOf(best, length)
        }
        return best
    }
}