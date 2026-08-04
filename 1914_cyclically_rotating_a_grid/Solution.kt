// LeetCode 1914 - Cyclically Rotating A Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

class Solution {
    fun rotateGrid(grid: Array<IntArray>, k: Int): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val layers = minOf(m, n) / 2
        for (layer in 0 until layers) {
            val vals = mutableListOf<Int>()
            for (c in layer until n - layer) vals.add(grid[layer][c])
            for (r in layer + 1 until m - layer) vals.add(grid[r][n - layer - 1])
            if (m - 2 * layer > 1) {
                for (c in n - layer - 2 downTo layer) vals.add(grid[m - layer - 1][c])
            }
            if (n - 2 * layer > 1) {
                for (r in m - layer - 2 downTo layer + 1) vals.add(grid[r][layer])
            }
            val shift = k % vals.size
            val rotated = vals.drop(shift) + vals.take(shift)
            var idx = 0
            for (c in layer until n - layer) grid[layer][c] = rotated[idx++]
            for (r in layer + 1 until m - layer) grid[r][n - layer - 1] = rotated[idx++]
            if (m - 2 * layer > 1) {
                for (c in n - layer - 2 downTo layer) grid[m - layer - 1][c] = rotated[idx++]
            }
            if (n - 2 * layer > 1) {
                for (r in m - layer - 2 downTo layer + 1) grid[r][layer] = rotated[idx++]
            }
        }
        return grid
    }
}
