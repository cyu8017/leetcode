// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

object Solution {
  def knightProbability(n: Int, k: Int, row: Int, column: Int): Double = {
    val moves = Array(Array(-2, -1), Array(-2, 1), Array(-1, -2), Array(-1, 2), Array(1, -2), Array(1, 2), Array(2, -1), Array(2, 1))
    var dp = Array.ofDim[Double](n, n)
    dp(row)(column) = 1.0
    var step = 0
    while (step < k) {
      val nxt = Array.ofDim[Double](n, n)
      var r = 0
      while (r < n) {
        var c = 0
        while (c < n) {
          if (dp(r)(c) != 0.0) {
            for (move <- moves) {
              val nr = r + move(0)
              val nc = c + move(1)
              if (nr >= 0 && nr < n && nc >= 0 && nc < n) nxt(nr)(nc) += dp(r)(c) / 8.0
            }
          }
          c += 1
        }
        r += 1
      }
      dp = nxt
      step += 1
    }
    var total = 0.0
    var r = 0
    while (r < n) {
      var c = 0
      while (c < n) {
        total += dp(r)(c)
        c += 1
      }
      r += 1
    }
    total
  }
}
