// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

object Solution {
  def matrixScore(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    grid.foreach { row =>
      if (row(0) == 0) {
        var j = 0
        while (j < n) {
          row(j) ^= 1
          j += 1
        }
      }
    }
    var ans = m * (1 << (n - 1))
    var j = 1
    while (j < n) {
      var ones = 0
      var i = 0
      while (i < m) {
        ones += grid(i)(j)
        i += 1
      }
      ans += math.max(ones, m - ones) * (1 << (n - 1 - j))
      j += 1
    }
    ans
  }
}
