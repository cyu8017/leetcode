// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

class Solution {
    fun orangesRotting(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val q = ArrayDeque<IntArray>()
        var fresh = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 2) q.add(intArrayOf(i, j))
                else if (grid[i][j] == 1) fresh++
            }
        }
        var minutes = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (q.isNotEmpty() && fresh > 0) {
            repeat(q.size) {
                val cur = q.removeFirst()
                for (d in dirs) {
                    val nr = cur[0] + d[0]
                    val nc = cur[1] + d[1]
                    if (nr in 0 until m && nc in 0 until n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2
                        fresh--
                        q.add(intArrayOf(nr, nc))
                    }
                }
            }
            minutes++
        }
        return if (fresh == 0) minutes else -1
    }
}
