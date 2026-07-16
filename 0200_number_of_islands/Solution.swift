// LeetCode 0200 - Number of Islands
class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        guard !grid.isEmpty else { return 0 }
        var grid = grid
        let rows = grid.count
        let cols = grid[0].count
        var count = 0

        func dfs(_ row: Int, _ col: Int) {
            guard row >= 0, row < rows, col >= 0, col < cols, grid[row][col] == "1" else {
                return
            }
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        }

        for row in 0..<rows {
            for col in 0..<cols where grid[row][col] == "1" {
                count += 1
                dfs(row, col)
            }
        }
        return count
    }
}