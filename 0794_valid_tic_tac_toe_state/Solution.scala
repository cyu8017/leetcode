// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

object Solution {
  def validTicTacToe(board: Array[String]): Boolean = {
    var x = 0
    var o = 0
    board.foreach { row =>
      row.foreach { ch =>
        if (ch == 'X') x += 1
        else if (ch == 'O') o += 1
      }
    }
    if (o > x || x - o > 1) return false
    def win(player: Char): Boolean = {
      var i = 0
      while (i < 3) {
        if (board(i).charAt(0) == player && board(i).charAt(1) == player && board(i).charAt(2) == player) return true
        if (board(0).charAt(i) == player && board(1).charAt(i) == player && board(2).charAt(i) == player) return true
        i += 1
      }
      if (board(0).charAt(0) == player && board(1).charAt(1) == player && board(2).charAt(2) == player) return true
      board(0).charAt(2) == player && board(1).charAt(1) == player && board(2).charAt(0) == player
    }
    val xWin = win('X')
    val oWin = win('O')
    if (xWin && oWin) return false
    if (xWin && x != o + 1) return false
    if (oWin && x != o) return false
    true
  }
}
