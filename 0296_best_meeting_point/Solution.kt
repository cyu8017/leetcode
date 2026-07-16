// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

import kotlin.math.abs

class Solution {
    fun minTotalDistance(grid: Array<IntArray>): Int {
        val rows = mutableListOf<Int>()
        val cols = mutableListOf<Int>()
        for (rowIndex in grid.indices) {
            for (colIndex in grid[rowIndex].indices) {
                if (grid[rowIndex][colIndex] == 1) {
                    rows.add(rowIndex)
                    cols.add(colIndex)
                }
            }
        }
        cols.sort()
        val rowMedian = rows[rows.size / 2]
        val colMedian = cols[cols.size / 2]
        return rows.sumOf { abs(it - rowMedian) } + cols.sumOf { abs(it - colMedian) }
    }
}
