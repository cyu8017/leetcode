// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

class Solution {
    func solve(_ board: inout [[Character]]) {
        guard !board.isEmpty, !board[0].isEmpty else { return }
        let rows = board.count
        let columns = board[0].count

        func mark(_ row: Int, _ column: Int) {
            guard row >= 0, row < rows, column >= 0, column < columns,
                  board[row][column] == "O" else { return }
            board[row][column] = "E"
            mark(row + 1, column)
            mark(row - 1, column)
            mark(row, column + 1)
            mark(row, column - 1)
        }

        for row in 0..<rows {
            mark(row, 0)
            mark(row, columns - 1)
        }
        for column in 0..<columns {
            mark(0, column)
            mark(rows - 1, column)
        }
        for row in 0..<rows {
            for column in 0..<columns {
                if board[row][column] == "O" {
                    board[row][column] = "X"
                } else if board[row][column] == "E" {
                    board[row][column] = "O"
                }
            }
        }
    }
}