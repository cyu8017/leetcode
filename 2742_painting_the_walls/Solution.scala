// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

object Solution {
  def paintWalls(cost: Array[Int], time: Array[Int]): Int = {
    val n = cost.length
    val INF = 1L << 60
    val dp = Array.fill(n + 1)(INF)
    dp(0) = 0
    var i = 0
    while (i < n) {
      var j = n
      while (j >= 0) {
        val nj = math.min(n, j + time(i) + 1)
        if (dp(j) + cost(i) < dp(nj)) dp(nj) = dp(j) + cost(i)
        j -= 1
      }
      i += 1
    }
    dp(n).toInt
  }
}
