// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

object Solution {
  def numRookCaptures(board: Array[Array[Char]]): Int = {
    val m = board.length
    val n = board(0).length
    var r = -1
    var c = -1
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (board(i)(j) == 'R') { r = i; c = j }
        j += 1
      }
      i += 1
    }
    if (r < 0) return 0
    var ans = 0
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    dirs.foreach { case (dr, dc) =>
      var ii = r + dr
      var jj = c + dc
      var stop = false
      while (!stop && ii >= 0 && ii < m && jj >= 0 && jj < n) {
        if (board(ii)(jj) == 'B') stop = true
        else if (board(ii)(jj) == 'p') { ans += 1; stop = true }
        else { ii += dr; jj += dc }
      }
    }
    ans
  }
}
