// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

object Solution {
  def tictactoe(moves: Array[Array[Int]]): String = {
    val board = Array.fill(3, 3)(0)
    for (i <- moves.indices) {
      board(moves(i)(0))(moves(i)(1)) = if (i % 2 == 0) 1 else -1
    }
    val lines = board.map(_.toSeq).toSeq ++ board(0).indices.map(c => board.map(_(c)).toSeq) ++
      Seq((0 until 3).map(i => board(i)(i)), (0 until 3).map(i => board(i)(2 - i)))
    for (line <- lines) {
      val s = line.sum
      if (math.abs(s) == 3) return if (s == 3) "A" else "B"
    }
    if (moves.length == 9) "Draw" else "Pending"
  }
}
