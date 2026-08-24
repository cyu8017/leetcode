// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

class Solution {
    fun countCells(grid: Array<CharArray>, pattern: String): Int {
        val m = grid.size
        val n = grid[0].size
        val row = StringBuilder(m * n)
        val col = StringBuilder(m * n)
        for (i in 0 until m) for (j in 0 until n) row.append(grid[i][j])
        for (j in 0 until n) for (i in 0 until m) col.append(grid[i][j])
        val rowS = row.toString()
        val colS = col.toString()
        val hMark = Array(m) { BooleanArray(n) }
        val vMark = Array(m) { BooleanArray(n) }
        val plen = pattern.length
        var i = 0
        while (i + plen <= rowS.length) {
            if (rowS.substring(i, i + plen) == pattern) {
                for (t in 0 until plen) {
                    val pos = i + t
                    hMark[pos / n][pos % n] = true
                }
            }
            i++
        }
        i = 0
        while (i + plen <= colS.length) {
            if (colS.substring(i, i + plen) == pattern) {
                for (t in 0 until plen) {
                    val pos = i + t
                    vMark[pos % m][pos / m] = true
                }
            }
            i++
        }
        var ans = 0
        for (ii in 0 until m) for (jj in 0 until n)
            if (hMark[ii][jj] && vMark[ii][jj]) ans++
        return ans
    }
}
