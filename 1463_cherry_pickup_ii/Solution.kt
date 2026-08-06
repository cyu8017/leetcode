// LeetCode 1463 - Cherry Pickup II
// https://leetcode.com/problems/cherry-pickup-ii/

class Solution {
    fun cherryPickup(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var dp = mutableMapOf((0 to n - 1) to grid[0][0] + if (n > 1) grid[0][n - 1] else 0)
        for (r in 1 until m) {
            val nxt = mutableMapOf<Pair<Int, Int>, Int>()
            for ((pair, score) in dp) {
                val (a, b) = pair
                for (na in a - 1..a + 1) {
                    for (nb in b - 1..b + 1) {
                        if (na in 0 until n && nb in 0 until n) {
                            val value = score + grid[r][na] + if (na != nb) grid[r][nb] else 0
                            nxt[na to nb] = maxOf(nxt.getOrDefault(na to nb, -1), value)
                        }
                    }
                }
            }
            dp = nxt
        }
        return dp.values.maxOrNull() ?: 0
    }
}
