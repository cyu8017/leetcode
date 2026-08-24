// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

class Solution {
    private var n = 0
    private lateinit var grid: Array<IntArray>
    private val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

    fun shortestBridge(grid: Array<IntArray>): Int {
        this.grid = grid
        n = grid.size
        var found = false
        for (i in 0 until n) {
            if (found) break
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    dfs(i, j)
                    found = true
                    break
                }
            }
        }
        val q = ArrayDeque<IntArray>()
        for (i in 0 until n)
            for (j in 0 until n)
                if (grid[i][j] == 2) q.add(intArrayOf(i, j, 0))
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            val r = cur[0]
            val c = cur[1]
            val dist = cur[2]
            for (d in dirs) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue
                if (grid[nr][nc] == 1) return dist
                if (grid[nr][nc] == 0) {
                    grid[nr][nc] = 2
                    q.add(intArrayOf(nr, nc, dist + 1))
                }
            }
        }
        return -1
    }

    private fun dfs(r: Int, c: Int) {
        if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return
        grid[r][c] = 2
        for (d in dirs) dfs(r + d[0], c + d[1])
    }
}
