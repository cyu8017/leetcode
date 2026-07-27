// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

class Solution {
    fun stoneGameVI(aliceValues: IntArray, bobValues: IntArray): Int {
        val order = aliceValues.indices.sortedByDescending { aliceValues[it] + bobValues[it] }
        var score = 0
        for ((t, i) in order.withIndex()) {
            score += if (t % 2 == 0) aliceValues[i] else -bobValues[i]
        }
        return when {
            score > 0 -> 1
            score < 0 -> -1
            else -> 0
        }
    }
}
