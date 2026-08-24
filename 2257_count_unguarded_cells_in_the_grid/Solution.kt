// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution {

    fun countUnguarded(m: Int, n: Int, guards: Array<IntArray>, walls: Array<IntArray>): Int {

            var grid = Array(m) { IntArray(n) }
            for (w in walls) grid[w[0]][w[1]] = 2
            for (g in guards) grid[g[0]][g[1]] = 2
            var dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } }
            for (g in guards) {
                for (d in dirs) {
                    var r = g[0] + d[0]; var c = g[1] + d[1]
                    while (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] != 2) {
                        grid[r][c] = 1
                        r += d[0]
                        c += d[1]
                    }
                }
            }
            var ans = 0
            for (i in 0 until m) { for (var j = 0 } j < n; j++)
                    if (grid[i][j] == 0) ans++
            return ans

    }

}
