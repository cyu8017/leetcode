// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

class Solution {
    fun movesToChessboard(board: Array<IntArray>): Int {
        var n = board.size
        for (i in 0 until n) {
            for (j in 0 until n) {
                if ((board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0) return -1
            }
        }
        var rowSum = 0
        var colSum = 0
        for (i in 0 until n) {
            rowSum += board[0][i]
            colSum += board[i][0]
        }
        if (rowSum < n / 2 || rowSum > (n + 1) / 2) return -1
        if (colSum < n / 2 || colSum > (n + 1) / 2) return -1
        var rowSwap = 0
        var colSwap = 0
        for (i in 0 until n) {
            if (board[0][i] != i % 2) rowSwap++
            if (board[i][0] != i % 2) colSwap++
        }
        if (n % 2 == 1) {
            if (rowSwap % 2 == 1) rowSwap = n - rowSwap
            if (colSwap % 2 == 1) colSwap = n - colSwap
        } else {
            rowSwap = minOf(rowSwap, n - rowSwap)
            colSwap = minOf(colSwap, n - colSwap)
        }
        return (rowSwap + colSwap) / 2
    }
}
