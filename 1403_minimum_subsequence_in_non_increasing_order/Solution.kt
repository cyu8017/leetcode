// LeetCode 1403 - Minimum Subsequence in Non-Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution {
    fun minSubsequence(nums: IntArray): List<Int> {
        val sorted = nums.sortedDescending()
        val total = nums.sum()
        val answer = ArrayList<Int>()
        var chosen = 0
        for (value in sorted) {
            answer.add(value)
            chosen += value
            if (chosen > total - chosen) return answer
        }
        return answer
    }
}
