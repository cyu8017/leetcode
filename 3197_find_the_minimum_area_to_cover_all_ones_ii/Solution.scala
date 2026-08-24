// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

object Solution {
  def minimumSum(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var ans = m * n
    def area(i1: Int, j1: Int, i2: Int, j2: Int): Int = {
      val inf = Int.MaxValue / 4
      var x1 = inf
      var y1 = inf
      var x2 = -inf
      var y2 = -inf
      var i = i1
      while (i <= i2) {
        var j = j1
        while (j <= j2) {
          if (grid(i)(j) == 1) {
            x1 = math.min(x1, i)
            y1 = math.min(y1, j)
            x2 = math.max(x2, i)
            y2 = math.max(y2, j)
          }
          j += 1
        }
        i += 1
      }
      if (x1 == inf) 0 else (x2 - x1 + 1) * (y2 - y1 + 1)
    }
    var i1 = 0
    while (i1 < m - 1) {
      var i2 = i1 + 1
      while (i2 < m - 1) {
        ans = math.min(ans, area(0, 0, i1, n - 1) + area(i1 + 1, 0, i2, n - 1) + area(i2 + 1, 0, m - 1, n - 1))
        i2 += 1
      }
      i1 += 1
    }
    var j1 = 0
    while (j1 < n - 1) {
      var j2 = j1 + 1
      while (j2 < n - 1) {
        ans = math.min(ans, area(0, 0, m - 1, j1) + area(0, j1 + 1, m - 1, j2) + area(0, j2 + 1, m - 1, n - 1))
        j2 += 1
      }
      j1 += 1
    }
    var i = 0
    while (i < m - 1) {
      var j = 0
      while (j < n - 1) {
        ans = math.min(ans, area(0, 0, i, j) + area(0, j + 1, i, n - 1) + area(i + 1, 0, m - 1, n - 1))
        ans = math.min(ans, area(0, 0, i, n - 1) + area(i + 1, 0, m - 1, j) + area(i + 1, j + 1, m - 1, n - 1))
        ans = math.min(ans, area(0, 0, i, j) + area(i + 1, 0, m - 1, j) + area(0, j + 1, m - 1, n - 1))
        ans = math.min(ans, area(0, 0, m - 1, j) + area(0, j + 1, i, n - 1) + area(i + 1, j + 1, m - 1, n - 1))
        j += 1
      }
      i += 1
    }
    ans
  }
}
