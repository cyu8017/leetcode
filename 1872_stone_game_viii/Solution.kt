// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

class Solution {
    fun stoneGameVIII(stones: IntArray): Int {
        val n = stones.size
        for (i in 1 until n) {
            stones[i] += stones[i - 1]
        }
        var score = stones[n - 1]
        for (i in n - 2 downTo 1) {
            score = maxOf(stones[i] - score, score)
        }
        return score
    }
}
