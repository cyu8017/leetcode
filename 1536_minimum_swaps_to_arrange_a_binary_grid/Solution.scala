// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

object Solution {
  def minSwaps(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val zeros = grid.map { row =>
      var count = 0
      var j = n - 1
      while (j >= 0 && row(j) == 0) { count += 1; j -= 1 }
      count
    }.toBuffer
    var answer = 0
    for (i <- 0 until n) {
      val required = n - i - 1
      var j = i
      while (j < n && zeros(j) < required) j += 1
      if (j == n) return -1
      answer += j - i
      val chosen = zeros(j)
      for (t <- j until i by -1) zeros(t) = zeros(t - 1)
      zeros(i) = chosen
    }
    answer
  }
}
