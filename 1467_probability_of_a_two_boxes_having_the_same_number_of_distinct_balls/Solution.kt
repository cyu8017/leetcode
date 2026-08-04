// LeetCode 1467 - Probability of a Two Boxes Having the Same Number of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

class Solution {
    private var good = 0L
    private var total = 0L
    private var half = 0
    private lateinit var balls: IntArray
    private lateinit var comb: Array<LongArray>

    fun getProbability(balls: IntArray): Double {
        this.balls = balls
        half = balls.sum() / 2
        val max = balls.maxOrNull() ?: 0
        comb = Array(max + 1) { LongArray(max + 1) }
        for (i in 0..max) {
            comb[i][0] = 1
            comb[i][i] = 1
            for (j in 1 until i) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
            }
        }
        good = 0
        total = 0
        dfs(0, 0, 0, 1L)
        return good.toDouble() / total
    }

    private fun dfs(i: Int, left: Int, dl: Int, ways: Long) {
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
}
