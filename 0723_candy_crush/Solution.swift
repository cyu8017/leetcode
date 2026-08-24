// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

class Solution {
    func candyCrush(_ board: [[Int]]) -> [[Int]] {
        var board = board
        let m = board.count, n = board[0].count
        var stable = false
        while !stable {
            stable = true
            for i in 0..<m {
                if n >= 3 {
                    for j in 0..<(n - 2) {
                        let value = abs(board[i][j])
                        if value != 0 && value == abs(board[i][j + 1]) && value == abs(board[i][j + 2]) {
                            board[i][j] = -value
                            board[i][j + 1] = -value
                            board[i][j + 2] = -value
                            stable = false
                        }
                    }
                }
            }
            for j in 0..<n {
                if m >= 3 {
                    for i in 0..<(m - 2) {
                        let value = abs(board[i][j])
                        if value != 0 && value == abs(board[i + 1][j]) && value == abs(board[i + 2][j]) {
                            board[i][j] = -value
                            board[i + 1][j] = -value
                            board[i + 2][j] = -value
                            stable = false
                        }
                    }
                }
            }
            for j in 0..<n {
                var write = m - 1
                for i in stride(from: m - 1, through: 0, by: -1) where board[i][j] > 0 {
                    board[write][j] = board[i][j]
                    write -= 1
                }
                if write >= 0 {
                    for i in stride(from: write, through: 0, by: -1) { board[i][j] = 0 }
                }
            }
        }
        return board
    }
}
