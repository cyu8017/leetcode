// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

class Solution {
    func movesToChessboard(_ board: [[Int]]) -> Int {
        let n = board.count
        for i in 0..<n {
            for j in 0..<n {
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0 { return -1 }
            }
        }
        var rowSum = 0, colSum = 0
        for i in 0..<n {
            rowSum += board[0][i]
            colSum += board[i][0]
        }
        if rowSum < n / 2 || rowSum > (n + 1) / 2 { return -1 }
        if colSum < n / 2 || colSum > (n + 1) / 2 { return -1 }
        var rowSwap = 0, colSwap = 0
        for i in 0..<n {
            if board[0][i] != i % 2 { rowSwap += 1 }
            if board[i][0] != i % 2 { colSwap += 1 }
        }
        if n % 2 == 1 {
            if rowSwap % 2 == 1 { rowSwap = n - rowSwap }
            if colSwap % 2 == 1 { colSwap = n - colSwap }
        } else {
            rowSwap = min(rowSwap, n - rowSwap)
            colSwap = min(colSwap, n - colSwap)
        }
        return (rowSwap + colSwap) / 2
    }
}
