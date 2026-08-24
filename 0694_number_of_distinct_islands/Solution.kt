// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

class Solution {
    private fun dfs(grid: Array<IntArray>, r: Int, c: Int, br: Int, bc: Int, path: MutableList<String>) {
        if (r < 0 || r >= grid.size || c < 0 || c >= grid[0].size || grid[r][c] == 0) return
        grid[r][c] = 0
        path.add((r - br) + "," + (c - bc))
        dfs(grid, r + 1, c, br, bc, path)
        dfs(grid, r - 1, c, br, bc, path)
        dfs(grid, r, c + 1, br, bc, path)
        dfs(grid, r, c - 1, br, bc, path)
    }

    fun numDistinctIslands(grid: Array<IntArray>): Int {
        if (grid == null || grid.size == 0) return 0
        var shapes = HashSet<String>()
        for (i in 0 until grid.size) {
            for (j in 0 until grid[0].size) {
                if (grid[i][j] == 1) {
                    var path = ArrayList<String>()
                    dfs(grid, i, j, i, j, path)
                    shapes.add(String.join(";", path))
                }
            }
        }
        return shapes.size
    }
}
