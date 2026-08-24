// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number_of_balanced_integers_in_a_range/

class Solution {
    private val BASE = 90
    private var num: String = ""
    private val f = Array(20) { LongArray(181) }

    private fun dfs(pos: Int, diff: Int, lim: Boolean): Long {
        if (pos >= num.length) return if (diff == 0) 1 else 0
        if (!lim && f[pos][diff + BASE] != -1L) return f[pos][diff + BASE]
        val up = if (lim) num[pos] - '0' else 9
        var res = 0L
        for (i in 0..up) {
            res += if (pos % 2 == 0) {
                dfs(pos + 1, diff + i, lim && i == up)
            } else {
                dfs(pos + 1, diff - i, lim && i == up)
            }
        }
        if (!lim) f[pos][diff + BASE] = res
        return res
    }

    fun countBalanced(low0: Long, high: Long): Long {
        if (high < 11) return 0
        var low = low0
        if (low < 11) low = 11
        num = (low - 1).toString()
        for (row in f) row.fill(-1)
        val a = dfs(0, 0, true)
        num = high.toString()
        for (row in f) row.fill(-1)
        val b = dfs(0, 0, true)
        return b - a
    }
}
