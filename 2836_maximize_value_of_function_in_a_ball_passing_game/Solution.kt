// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

class Solution {
    fun getMaxFunctionValue(receiver: IntArray, k: Long): Long {
        val n = receiver.size
        val LOG = 36
        val up = Array(LOG) { IntArray(n) }
        val sum = Array(LOG) { LongArray(n) }
        for (i in 0 until n) {
            up[0][i] = receiver[i]
            sum[0][i] = receiver[i].toLong()
        }
        for (j in 1 until LOG) {
            for (i in 0 until n) {
                val mid = up[j - 1][i]
                up[j][i] = up[j - 1][mid]
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid]
            }
        }
        var ans = 0L
        for (i in 0 until n) {
            var cur = i
            var total = i.toLong()
            var kk = k
            for (j in 0 until LOG) {
                if ((kk and (1L shl j)) != 0L) {
                    total += sum[j][cur]
                    cur = up[j][cur]
                }
            }
            ans = maxOf(ans, total)
        }
        return ans
    }
}
