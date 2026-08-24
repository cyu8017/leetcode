// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

object Solution {
  def countPyramids(grid: Array[Array[Int]]): Int = {
    def count(g: Array[Array[Int]]): Int = {
      val m = g.length
      val n = g(0).length
      val dp = Array.tabulate(m)(i => g(i).clone())
      var ans = 0
      var i = m - 2
      while (i >= 0) {
        var j = 1
        while (j < n - 1) {
          if (g(i)(j) == 1) {
            dp(i)(j) = 1 + math.min(dp(i + 1)(j - 1), math.min(dp(i + 1)(j), dp(i + 1)(j + 1)))
            ans += dp(i)(j) - 1
          }
          j += 1
        }
        i -= 1
      }
      ans
    }
    val m = grid.length
    val rev = Array.tabulate(m)(i => grid(m - 1 - i))
    count(grid) + count(rev)
  }
}
