// LeetCode 1368 - Minimum Cost to Make at Least One Valid Path in a Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

class Solution {
    fun minCost(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dist = Array(m) { IntArray(n) { 1_000_000_000 } }
        dist[0][0] = 0
        val dq = ArrayDeque<IntArray>()
        dq.add(intArrayOf(0, 0))
        val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(0, -1), intArrayOf(1, 0), intArrayOf(-1, 0))
        while (dq.isNotEmpty()) {
            val cur = dq.removeFirst()
            val r = cur[0]
            val c = cur[1]
            for (k in dirs.indices) {
                val x = r + dirs[k][0]
                val y = c + dirs[k][1]
                if (x in 0 until m && y in 0 until n) {
                    val w = if (k + 1 != grid[r][c]) 1 else 0
                    val nd = dist[r][c] + w
                    if (nd < dist[x][y]) {
                        dist[x][y] = nd
                        if (w == 0) dq.addFirst(intArrayOf(x, y)) else dq.addLast(intArrayOf(x, y))
                    }
                }
            }
        }
        return dist[m - 1][n - 1]
    }
}
