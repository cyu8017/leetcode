// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

class Solution {
    fun numDistinctIslands2(grid: Array<IntArray>): Int {
        if (grid.isEmpty()) return 0
        val m = grid.size
        val n = grid[0].size
        val shapes = HashSet<String>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    val cells = ArrayList<IntArray>()
                    dfs(grid, i, j, m, n, cells)
                    shapes.add(canonical(cells))
                }
            }
        }
        return shapes.size
    }

    private fun dfs(grid: Array<IntArray>, r: Int, c: Int, m: Int, n: Int, cells: MutableList<IntArray>) {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return
        grid[r][c] = 0
        cells.add(intArrayOf(r, c))
        dfs(grid, r + 1, c, m, n, cells)
        dfs(grid, r - 1, c, m, n, cells)
        dfs(grid, r, c + 1, m, n, cells)
        dfs(grid, r, c - 1, m, n, cells)
    }

    private fun canonical(cells: List<IntArray>): String {
        val signs = arrayOf(
            intArrayOf(1, 1, 0), intArrayOf(1, -1, 0), intArrayOf(-1, 1, 0), intArrayOf(-1, -1, 0),
            intArrayOf(1, 1, 1), intArrayOf(1, -1, 1), intArrayOf(-1, 1, 1), intArrayOf(-1, -1, 1)
        )
        var best: String? = null
        for (s in signs) {
            val pts = ArrayList<IntArray>()
            for (p in cells) {
                val x = p[0]
                val y = p[1]
                val nx: Int
                val ny: Int
                if (s[2] == 0) {
                    nx = s[0] * x
                    ny = s[1] * y
                } else {
                    nx = s[0] * y
                    ny = s[1] * x
                }
                pts.add(intArrayOf(nx, ny))
            }
            var minX = Int.MAX_VALUE
            var minY = Int.MAX_VALUE
            for (p in pts) {
                minX = minOf(minX, p[0])
                minY = minOf(minY, p[1])
            }
            for (p in pts) {
                p[0] -= minX
                p[1] -= minY
            }
            pts.sortWith(compareBy({ it[0] }, { it[1] }))
            val sb = StringBuilder()
            for (p in pts) {
                if (sb.isNotEmpty()) sb.append(';')
                sb.append(p[0]).append(',').append(p[1])
            }
            val key = sb.toString()
            if (best == null || key < best) best = key
        }
        return best!!
    }
}
