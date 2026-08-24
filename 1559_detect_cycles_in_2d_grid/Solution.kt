// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

class Solution {
    fun containsCycle(grid: Array<CharArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        val seen = Array(m) { BooleanArray(n) }
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (!seen[r][c] && dfs(grid, seen, r, c, -1, -1)) return true
            }
        }
        return false
    }

    private fun dfs(grid: Array<CharArray>, seen: Array<BooleanArray>, r: Int, c: Int, pr: Int, pc: Int): Boolean {
        seen[r][c] = true
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        for (d in dirs) {
            val nr = r + d[0]
            val nc = c + d[1]
            if (nr < 0 || nr >= grid.size || nc < 0 || nc >= grid[0].size) continue
            if (grid[nr][nc] != grid[r][c] || (nr == pr && nc == pc)) continue
            if (seen[nr][nc] || dfs(grid, seen, nr, nc, r, c)) return true
        }
        return false
    }
}
