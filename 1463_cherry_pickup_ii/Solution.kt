// LeetCode 1463 - Cherry Pickup II
// https://leetcode.com/problems/cherry-pickup-ii/

class Solution {
    fun cherryPickup(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var dp = HashMap<Long, Int>()
        dp[key(0, n - 1)] = grid[0][0] + if (n > 1) grid[0][n - 1] else 0
        for (r in 1 until m) {
            val nxt = HashMap<Long, Int>()
            for ((k, score) in dp) {
                val a = (k shr 32).toInt()
                val b = k.toInt()
                for (na in a - 1..a + 1) {
                    for (nb in b - 1..b + 1) {
                        if (na !in 0 until n || nb !in 0 until n) continue
                        val value = score + grid[r][na] + if (na != nb) grid[r][nb] else 0
                        val nk = key(na, nb)
                        nxt[nk] = maxOf(nxt.getOrDefault(nk, -1), value)
                    }
                }
            }
            dp = nxt
        }
        return dp.values.maxOrNull() ?: 0
    }

    private fun key(a: Int, b: Int): Long = (a.toLong() shl 32) or (b.toLong() and 0xffffffffL)
}
