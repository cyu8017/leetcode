// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

class Solution {
    private var extras: MutableList<IntArray>? = null
    private var zeros: MutableList<IntArray>? = null
    private var best: Int = 0

    fun minimumMoves(grid: Array<IntArray>): Int {
        extras = ArrayList()
        zeros = ArrayList()
        for (i in 0 until 3) {
            for (j in 0 until 3) {
                if (grid[i][j] == 0) zeros.add(intArrayOf(i, j))
                else if (grid[i][j] > 1) {
                    for (k in 0 until grid[i][j] - 1) { extras.add(intArrayOf(i, j)) }
                }
            }
        }
        if (zeros.isEmpty()) return 0
        best = 1  shl  30
        dfs(0, 0)
        return best
    }

    private fun dfs(i: Int, cost: Int) {
        if (cost >= best) return
        if (i == zeros.size) {
            best = cost
            return
        }
        for (j in 0 until extras.size) {
            if (extras[j][0] < 0) continue
            var e = extras[j]
            extras.set(j, intArrayOf(-1, e[1]))
            var d = kotlin.math.abs(e[0] - zeros[i][0]) + kotlin.math.abs(e[1] - zeros[i][1])
            dfs(i + 1, cost + d)
            extras.set(j, e)
        }
    }
}
