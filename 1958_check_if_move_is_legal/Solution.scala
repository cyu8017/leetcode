// LeetCode 1958 - Check if Move is Legal
// https://leetcode.com/problems/check-if-move-is-legal/

object Solution {
  def checkMove(board: Array[Array[Char]], rMove: Int, cMove: Int, color: Char): Boolean = {
    val opp = if (color == 'B') 'W' else 'B'
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
    for ((dr, dc) <- dirs) {
      var r = rMove + dr
      var c = cMove + dc
      var steps = 0
      while (r >= 0 && r < 8 && c >= 0 && c < 8 && board(r)(c) == opp) {
        r += dr
        c += dc
        steps += 1
      }
      if (steps > 0 && r >= 0 && r < 8 && c >= 0 && c < 8 && board(r)(c) == color) return true
    }
    false
  }
}
