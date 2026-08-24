// LeetCode 3742 - Maximum Path Score In A Grid
// https://leetcode.com/problems/maximum_path_score_in_a_grid/

class Solution {
    private lateinit var grid: Array<IntArray>
    private lateinit var f: Array<Array<IntArray>>
    private var m = 0
    private var n = 0
    private val INF = 1 shl 30

    fun maxPathScore(grid: Array<IntArray>, k: Int): Int {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        f = Array(m) { Array(n) { IntArray(k + 1) { -1 } } }
        val ans = dfs(m - 1, n - 1, k)
        return if (ans < 0) -1 else ans
    }

    private fun dfs(i: Int, j: Int, kk: Int): Int {
        if (i < 0 || j < 0 || kk < 0) return -INF
        if (i == 0 && j == 0) return 0
        if (f[i][j][kk] != -1) return f[i][j][kk]
        var res = grid[i][j]
        var nk = kk
        if (grid[i][j] != 0) nk--
        val a = dfs(i - 1, j, nk)
        val b = dfs(i, j - 1, nk)
        res += maxOf(a, b)
        f[i][j][kk] = res
        return res
    }
}
