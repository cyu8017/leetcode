// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

class Solution {
    private var num: String = ""
    private lateinit var f: Array<Array<Array<LongArray>>>
    private var n = 0

    private fun check(s: Int): Boolean {
        if (s < 100) return s % 11 != 0
        val mid = (s / 10) % 10
        val last = s % 10
        return mid > 1 && mid < last
    }

    fun countFancy(l: Long, r: Long): Long {
        return calc(r) - calc(l - 1)
    }

    private fun calc(x: Long): Long {
        num = x.toString()
        n = num.length
        f = Array(n) { Array(9 * n + 1) { Array(10) { LongArray(4) { -1L } } } }
        return dfs(0, 0, 0, 0, true)
    }

    private fun dfs(pos: Int, s: Int, prev: Int, st: Int, lim: Boolean): Long {
        if (pos >= n) {
            if (st != 3) return 1
            return if (check(s)) 1 else 0
        }
        if (!lim && f[pos][s][prev][st] != -1L) return f[pos][s][prev][st]
        val up = if (lim) num[pos] - '0' else 9
        var res = 0L
        for (i in 0..up) {
            var nxtSt = st
            when (st) {
                0 -> {
                    nxtSt = when {
                        prev == 0 -> 0
                        i > prev -> 1
                        i < prev -> 2
                        else -> 3
                    }
                }
                1 -> nxtSt = if (i > prev) 1 else 3
                2 -> nxtSt = if (i < prev) 2 else 3
                else -> nxtSt = 3
            }
            res += dfs(pos + 1, s + i, i, nxtSt, lim && i == up)
        }
        if (!lim) f[pos][s][prev][st] = res
        return res
    }
}
