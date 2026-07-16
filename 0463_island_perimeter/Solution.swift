// LeetCode 0463 - Island Perimeter
// https://leetcode.com/problems/island-perimeter/

class Solution {
    func islandPerimeter(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        let cols = grid[0].count
        var perimeter = 0

        for row in 0..<rows {
            for col in 0..<cols {
                if grid[row][col] == 0 {
                    continue
                }
                perimeter += 4
                if row > 0 && grid[row - 1][col] == 1 {
                    perimeter -= 2
                }
                if col > 0 && grid[row][col - 1] == 1 {
                    perimeter -= 2
                }
            }
        }

        return perimeter
    }
}
