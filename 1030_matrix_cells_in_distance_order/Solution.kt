// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution {
    fun allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array<IntArray> {
        val cells = Array(rows * cols) { IntArray(2) }
        var idx = 0
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                cells[idx][0] = r
                cells[idx++][1] = c
            }
        }
        cells.sortBy { kotlin.math.abs(it[0] - rCenter) + kotlin.math.abs(it[1] - cCenter) }
        return cells
    }
}
