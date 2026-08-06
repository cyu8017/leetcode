// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

object Solution {
  def largest1BorderedSquare(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val left = Array.ofDim[Int](m, n)
    val up = Array.ofDim[Int](m, n)
    for (r <- 0 until m; c <- 0 until n if grid(r)(c) == 1) {
      left(r)(c) = 1 + (if (c > 0) left(r)(c - 1) else 0)
      up(r)(c) = 1 + (if (r > 0) up(r - 1)(c) else 0)
    }
    var best = 0
    for (r <- 0 until m; c <- 0 until n if grid(r)(c) == 1) {
      val limit = math.min(left(r)(c), up(r)(c))
      var size = limit
      var done = false
      while (size > 0 && !done) {
        if (left(r - size + 1)(c) >= size && up(r)(c - size + 1) >= size) {
          best = math.max(best, size)
          done = true
        }
        size -= 1
      }
    }
    best * best
  }
}
