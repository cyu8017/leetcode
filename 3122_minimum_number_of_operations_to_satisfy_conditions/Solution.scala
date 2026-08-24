// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

object Solution {
  def minimumOperations(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val INF = 1 << 29
    val f = Array.fill(n, 10)(INF)
    var i = 0
    while (i < n) {
      val cnt = new Array[Int](10)
      var j = 0
      while (j < m) {
        cnt(grid(j)(i)) += 1
        j += 1
      }
      if (i == 0) {
        j = 0
        while (j < 10) {
          f(i)(j) = m - cnt(j)
          j += 1
        }
      } else {
        j = 0
        while (j < 10) {
          var k = 0
          while (k < 10) {
            if (j != k) f(i)(j) = math.min(f(i)(j), f(i - 1)(k) + m - cnt(j))
            k += 1
          }
          j += 1
        }
      }
      i += 1
    }
    var ans = INF
    var j = 0
    while (j < 10) {
      ans = math.min(ans, f(n - 1)(j))
      j += 1
    }
    ans
  }
}
