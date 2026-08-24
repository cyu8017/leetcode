// LeetCode 0463 - Island Perimeter
// https://leetcode.com/problems/island-perimeter/

class Solution {
    fun islandPerimeter(grid: Array<IntArray>): Int {
        val rows = grid.size
        val cols = grid[0].size
        var perimeter = 0
        for (row in 0 until rows) {
            for (col in 0 until cols) {
                if (grid[row][col] == 0) {
                    continue
                }
                perimeter += 4
                if (row > 0 && grid[row - 1][col] == 1) {
                    perimeter -= 2
                }
                if (col > 0 && grid[row][col - 1] == 1) {
                    perimeter -= 2
                }
            }
        }
        return perimeter
    }
}
