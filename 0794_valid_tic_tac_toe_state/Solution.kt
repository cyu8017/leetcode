// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution {
    fun validTicTacToe(board: Array<String>): Boolean {
        var x = 0
        var o = 0
        for (row in board) {
            for (ch in row.toCharArray()) {
                if (ch == 'X') x++
                else if (ch == 'O') o++
            }
        }
        if (o > x || x - o > 1) return false
        var xWin = win(board, 'X')
        var oWin = win(board, 'O')
        if (xWin && oWin) return false
        if (xWin && x != o + 1) return false
        if (oWin && x != o) return false
        return true
    }

    private fun win(board: Array<String>, player: Char): Boolean {
        for (i in 0 until 3) {
            if (board[i].charAt(0) == player && board[i].charAt(1) == player && board[i].charAt(2) == player)
                return true
            if (board[0].charAt(i) == player && board[1].charAt(i) == player && board[2].charAt(i) == player)
                return true
        }
        if (board[0].charAt(0) == player && board[1].charAt(1) == player && board[2].charAt(2) == player)
            return true
        if (board[0].charAt(2) == player && board[1].charAt(1) == player && board[2].charAt(0) == player)
            return true
        return false
    }
}
