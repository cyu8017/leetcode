// LeetCode 1467 - Probability of a Two Boxes Having the Same Number of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

class Solution {
    fun getProbability(balls: IntArray): Double {
        val half = balls.sum() / 2
        var good = 0.0
        var total = 0.0
        val maxB = balls.maxOrNull()!!
        val comb = Array(maxB + 1) { LongArray(maxB + 1) }
        for (i in 0..maxB) {
            comb[i][0] = 1
            for (j in 1..i) comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
        }
        fun dfs(i: Int, left: Int, dl: Int, ways: Double) {
            if (i == balls.size) {
                if (left == half) {
                    total += ways
                    if (dl == 0) good += ways
                }
                return
            }
            for (x in 0..balls[i]) {
                if (left + x <= half) {
                    val delta = (if (x > 0) 1 else 0) - (if (x < balls[i]) 1 else 0)
                    dfs(i + 1, left + x, dl + delta, ways * comb[balls[i]][x])
                }
            }
        }
        dfs(0, 0, 0, 1.0)
        return good / total
    }
}
