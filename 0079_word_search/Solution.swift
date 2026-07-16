// LeetCode 0079 - Word Search
// https://leetcode.com/problems/word-search/

class Solution {
    func exist(_ board: [[Character]], _ word: String) -> Bool {
        var grid = board
        let rows = grid.count
        let cols = grid[0].count
        let chars = Array(word)

        func dfs(_ row: Int, _ col: Int, _ index: Int) -> Bool {
            if index == chars.count {
                return true
            }
            if row < 0 || col < 0 || row >= rows || col >= cols || grid[row][col] != chars[index] {
                return false
            }

            let temp = grid[row][col]
            grid[row][col] = "#"

            let found = dfs(row + 1, col, index + 1)
                || dfs(row - 1, col, index + 1)
                || dfs(row, col + 1, index + 1)
                || dfs(row, col - 1, index + 1)

            grid[row][col] = temp
            return found
        }

        for row in 0..<rows {
            for col in 0..<cols {
                if dfs(row, col, 0) {
                    return true
                }
            }
        }

        return false
    }
}
