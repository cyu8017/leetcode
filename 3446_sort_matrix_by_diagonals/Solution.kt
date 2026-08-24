// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

class Solution {
    fun sortMatrix(grid: Array<IntArray>): Array<IntArray> {
        val n = grid.size
        val diags = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            for (j in 0 until n) {
                diags.getOrPut(i - j) { ArrayList() }.add(grid[i][j])
            }
        }
        for ((key, value) in diags) {
            if (key >= 0) value.sortDescending() else value.sort()
        }
        val idx = HashMap<Int, Int>()
        for (i in 0 until n) {
            for (j in 0 until n) {
                val k = i - j
                val pos = idx.getOrDefault(k, 0)
                grid[i][j] = diags[k]!![pos]
                idx[k] = pos + 1
            }
        }
        return grid
    }
}
