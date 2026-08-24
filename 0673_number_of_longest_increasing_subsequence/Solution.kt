// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/


class Solution {
    fun findNumberOfLIS(nums: IntArray): Int {
        val n = nums.size
        val len = IntArray(n) { 1 }
        val cnt = IntArray(n) { 1 }
        var best = 1
        for (i in 0 until n) {
            for (j in 0 until i) {
                if (nums[j] < nums[i]) {
                    if (len[j] + 1 > len[i]) {
                        len[i] = len[j] + 1
                        cnt[i] = cnt[j]
                    } else if (len[j] + 1 == len[i]) {
                        cnt[i] += cnt[j]
                    }
                }
            }
            best = maxOf(best, len[i])
        }
        var answer = 0
        for (i in 0 until n) if (len[i] == best) answer += cnt[i]
        return answer
    }
}
