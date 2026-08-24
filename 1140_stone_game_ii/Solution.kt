// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

class Solution {
    fun stoneGameII(piles: IntArray): Int {
        val n = piles.size
        val suffix = IntArray(n + 1)
        for (i in n - 1 downTo 0) suffix[i] = suffix[i + 1] + piles[i]
        val memo = Array(n) { IntArray(n + 1) { -1 } }
        fun dfs(i: Int, m: Int): Int {
            if (i >= n) return 0
            if (i + m >= n) return suffix[i]
            if (memo[i][m] != -1) return memo[i][m]
            var best = Int.MAX_VALUE
            for (x in 1..minOf(2 * m, n - i)) {
                best = minOf(best, dfs(i + x, maxOf(x, m)))
            }
            memo[i][m] = suffix[i] - best
            return memo[i][m]
        }
        return dfs(0, 1)
    }
}
