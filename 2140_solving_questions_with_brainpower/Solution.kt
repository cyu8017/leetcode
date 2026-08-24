// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution {
    fun mostPoints(questions: Array<IntArray>): Long {
        var n: Int = questions.size
        var dp: LongArray = LongArray(n + 1)
        for (i in n - 1 downTo 0) {
            var pts: Int = questions[i][0], brain = questions[i][1]
            var next: Int = i + brain + 1
            var take: Long = if (pts + (next < n) dp[next] else 0)
            dp[i] = maxOf(dp[i + 1], take)
        }
        return dp[0]
    }
}
