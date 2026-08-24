// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

class Solution {
    var m = 0
    var n = 0
    var st = 0L
    var path: MutableList<MutableList<Int>>? = null
    var dirs = {-1, 0, 1, 0, -1}
    var grid: Array<IntArray>? = null

    fun f(i: Int, j: Int): Int { return i * n + j }

    fun dfs(i: Int, j: Int, v: Int): Boolean {
        var cell = ArrayList<Int>()
        cell.add(i); cell.add(j)
        path.add(cell)
        if (path.size == m * n) return true
        var idx = f(i, j)
        st |= 1L  shl  idx
        if (grid[i][j] == v) { v = v + 1 }
        for (t in 0 until 4) {
            var x = i + dirs[t]
            var y = j + dirs[t + 1]
            if (0 <= x && x < m && 0 <= y && y < n) {
                var idx2 = f(x, y)
                if (((st  shr  idx2) & 1L) == 0 && (grid[x][y] == 0 || grid[x][y] == v)) {
                    if (dfs(x, y, v)) return true
                }
            }
        }
        path.remove(path.size - 1)
        st ^= 1L  shl  idx
        return false
    }

    fun findPath(grid: Array<IntArray>, k: Int): MutableList<MutableList<Int>> {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        st = 0
        path = ArrayList()
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 0 || grid[i][j] == 1) {
                    if (dfs(i, j, 1)) return path
                    path.clear()
                    st = 0
                }
            }
        }
        return ArrayList()
    }
}
