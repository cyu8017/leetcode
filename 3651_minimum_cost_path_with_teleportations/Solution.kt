// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

import java.util.TreeMap

class Solution {
    fun minCost(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        val inf = Int.MAX_VALUE / 4
        val f = Array(k + 1) { Array(m) { IntArray(n) { inf } } }
        f[0][0][0] = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i > 0) f[0][i][j] = minOf(f[0][i][j], f[0][i - 1][j] + grid[i][j])
                if (j > 0) f[0][i][j] = minOf(f[0][i][j], f[0][i][j - 1] + grid[i][j])
            }
        }
        val g = TreeMap<Int, ArrayList<IntArray>>(compareByDescending { it })
        for (i in 0 until m) {
            for (j in 0 until n) {
                g.getOrPut(grid[i][j]) { ArrayList() }.add(intArrayOf(i, j))
            }
        }
        for (t in 1..k) {
            var mn = inf
            for (pos in g.values) {
                for (p in pos) mn = minOf(mn, f[t - 1][p[0]][p[1]])
                for (p in pos) f[t][p[0]][p[1]] = mn
            }
            for (i in 0 until m) {
                for (j in 0 until n) {
                    if (i > 0) f[t][i][j] = minOf(f[t][i][j], f[t][i - 1][j] + grid[i][j])
                    if (j > 0) f[t][i][j] = minOf(f[t][i][j], f[t][i][j - 1] + grid[i][j])
                }
            }
        }
        var ans = inf
        for (t in 0..k) ans = minOf(ans, f[t][m - 1][n - 1])
        return ans
    }
}
