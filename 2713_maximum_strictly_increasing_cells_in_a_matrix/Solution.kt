// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

class Solution {
    fun maxIncreasingCells(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val cells = ArrayList<IntArray>()
        for (i in 0 until m)
            for (j in 0 until n)
                cells.add(intArrayOf(mat[i][j], i, j))
        cells.sortBy { it[0] }
        val rowMax = IntArray(m)
        val colMax = IntArray(n)
        val dp = Array(m) { IntArray(n) }
        var ans = 0
        var i = 0
        while (i < cells.size) {
            var j = i
            while (j < cells.size && cells[j][0] == cells[i][0]) j++
            val buf = ArrayList<IntArray>()
            for (k in i until j) {
                val r = cells[k][1]
                val c = cells[k][2]
                val best = maxOf(rowMax[r], colMax[c])
                dp[r][c] = best + 1
                ans = maxOf(ans, dp[r][c])
                buf.add(intArrayOf(r, c, dp[r][c]))
            }
            for (b in buf) {
                rowMax[b[0]] = maxOf(rowMax[b[0]], b[2])
                colMax[b[1]] = maxOf(colMax[b[1]], b[2])
            }
            i = j
        }
        return ans
    }
}
