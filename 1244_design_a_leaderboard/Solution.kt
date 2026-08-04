// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard {
    private val scores = mutableMapOf<Int, Int>()

    fun addScore(playerId: Int, score: Int) {
        scores[playerId] = scores.getOrDefault(playerId, 0) + score
    }

    fun top(K: Int): Int {
        val values = scores.values.sortedDescending()
        return values.take(minOf(K, values.size)).sum()
    }

    fun reset(playerId: Int) {
        scores.remove(playerId)
    }
}
