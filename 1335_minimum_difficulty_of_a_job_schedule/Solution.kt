// LeetCode 1335 - Minimum Difficulty of a Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution {
    fun minDifficulty(jobDifficulty: IntArray, d: Int): Int {
        val n = jobDifficulty.size
        if (n < d) return -1
        val dp = IntArray(n) { 1_000_000_000 }
        var hardest = 0
        for (i in 0 until n) {
            hardest = maxOf(hardest, jobDifficulty[i])
            dp[i] = hardest
        }
        for (day in 1 until d) {
            val nxt = IntArray(n) { 1_000_000_000 }
            for (end in day until n) {
                hardest = 0
                for (start in end downTo day) {
                    hardest = maxOf(hardest, jobDifficulty[start])
                    nxt[end] = minOf(nxt[end], dp[start - 1] + hardest)
                }
            }
            for (i in 0 until n) dp[i] = nxt[i]
        }
        return dp[n - 1]
    }
}
