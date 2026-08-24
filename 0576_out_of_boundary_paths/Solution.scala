// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

object Solution {
  def findPaths(m: Int, n: Int, maxMove: Int, startRow: Int, startColumn: Int): Int = {
    val MOD = 1000000007
    var dp = Array.ofDim[Int](m, n)
    dp(startRow)(startColumn) = 1
    var result = 0
    val dirs = Array((0, 1), (0, -1), (1, 0), (-1, 0))
    var move = 0
    while (move < maxMove) {
      val nxt = Array.ofDim[Int](m, n)
      var row = 0
      while (row < m) {
        var col = 0
        while (col < n) {
          val ways = dp(row)(col)
          if (ways != 0) {
            dirs.foreach { case (dr, dc) =>
              val nr = row + dr
              val nc = col + dc
              if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                nxt(nr)(nc) = (nxt(nr)(nc) + ways) % MOD
              } else {
                result = (result + ways) % MOD
              }
            }
          }
          col += 1
        }
        row += 1
      }
      dp = nxt
      move += 1
    }
    result
  }
}
