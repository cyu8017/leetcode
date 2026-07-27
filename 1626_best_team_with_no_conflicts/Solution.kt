// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution {
    fun bestTeamScore(scores: IntArray, ages: IntArray): Int {
        val players = ages.indices.map { ages[it] to scores[it] }.sortedWith(compareBy({ it.first }, { it.second }))
        val dp = IntArray(players.size)
        for (i in players.indices) {
            val score = players[i].second
            var best = 0
            for (j in 0 until i) {
                if (players[j].second <= score) best = maxOf(best, dp[j])
            }
            dp[i] = score + best
        }
        return dp.maxOrNull() ?: 0
    }
}
