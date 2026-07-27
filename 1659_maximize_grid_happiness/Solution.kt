// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

class Solution {
    fun getMaxGridHappiness(m: Int, n: Int, introvertsCount: Int, extrovertsCount: Int): Int {
        var states = 1
        repeat(n) { states *= 3 }
        val cells = Array(states) { IntArray(n) }
        val intro = IntArray(states)
        val extro = IntArray(states)
        val row = IntArray(states)
        for (s in 0 until states) {
            var x = s
            for (j in 0 until n) {
                cells[s][j] = x % 3
                x /= 3
            }
            var value = 0
            for (j in 0 until n) {
                when (cells[s][j]) {
                    1 -> { intro[s]++; value += 120 }
                    2 -> { extro[s]++; value += 40 }
                }
            }
            for (j in 1 until n) value += pair(cells[s][j - 1], cells[s][j])
            row[s] = value
        }
        val compat = Array(states) { IntArray(states) }
        for (a in 0 until states) {
            for (b in 0 until states) {
                var v = 0
                for (j in 0 until n) v += pair(cells[a][j], cells[b][j])
                compat[a][b] = v
            }
        }
        val memo = IntArray((m + 1) * states * (introvertsCount + 1) * (extrovertsCount + 1)) { -1 }
        fun dfs(r: Int, prev: Int, i: Int, e: Int): Int {
            if (r == m) return 0
            val id = (((r * states + prev) * (introvertsCount + 1) + i) * (extrovertsCount + 1)) + e
            if (memo[id] >= 0) return memo[id]
            var best = 0
            for (s in 0 until states) {
                if (intro[s] > i || extro[s] > e) continue
                best = maxOf(best, row[s] + compat[prev][s] + dfs(r + 1, s, i - intro[s], e - extro[s]))
            }
            memo[id] = best
            return best
        }
        return dfs(0, 0, introvertsCount, extrovertsCount)
    }

    private fun pair(a: Int, b: Int): Int {
        if (a == 0 || b == 0) return 0
        val va = if (a == 1) -30 else 20
        val vb = if (b == 1) -30 else 20
        return va + vb
    }
}
