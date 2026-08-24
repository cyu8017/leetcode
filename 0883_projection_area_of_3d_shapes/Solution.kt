// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution {
    fun projectionArea(grid: Array<IntArray>): Int {
        var n = grid.size
        var top = 0
        var front = 0
        var side = 0
        for (i in 0 until n) {
            var rowMax = 0
            var colMax = 0
            for (j in 0 until n) {
                if (grid[i][j] != 0) top++
                rowMax = maxOf(rowMax, grid[i][j])
                colMax = maxOf(colMax, grid[j][i])
            }
            front += rowMax
            side += colMax
        }
        return top + front + side
    }
}
