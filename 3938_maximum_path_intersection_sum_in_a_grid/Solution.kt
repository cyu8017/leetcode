// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

class Solution {
    fun maxPathSum(grid: Array<IntArray>): Int {
        val rows = grid.size
        val cols = grid[0].size
        var answer = Int.MIN_VALUE
        for (row in 0 until rows) {
            answer = maxOf(answer, checkLine(cols) { col -> grid[row][col] })
        }
        for (col in 0 until cols) {
            answer = maxOf(answer, checkLine(rows) { row -> grid[row][col] })
        }
        for (row in 1 until rows - 1) {
            for (col in 1 until cols - 1) {
                if (grid[row][col] > answer) answer = grid[row][col]
            }
        }
        return answer
    }

    private fun checkLine(length: Int, value: (Int) -> Int): Int {
        var answer = Int.MIN_VALUE
        var bestEnding = value(0) + value(1)
        if (bestEnding > answer) answer = bestEnding
        for (i in 2 until length) {
            if (value(i - 1) + value(i) > bestEnding + value(i)) bestEnding = value(i - 1) + value(i)
            else bestEnding += value(i)
            if (bestEnding > answer) answer = bestEnding
        }
        return answer
    }
}
