// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

object Solution {
  def countSortedMatrices(grid: Array[Array[Int]], k: Int): Long = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0L
    var r1 = 0
    while (r1 < m) {
      var r2 = r1
      while (r2 < m) {
        var c1 = 0
        while (c1 < n) {
          var c2 = c1
          while (c2 < n) {
            var ok = true
            var i = r1
            while (i <= r2 && ok) {
              var j = c1
              while (j <= c2 && ok) {
                if (grid(i)(j) > k) ok = false
                else if (j > c1 && grid(i)(j) < grid(i)(j - 1)) ok = false
                else if (i > r1 && grid(i)(j) < grid(i - 1)(j)) ok = false
                j += 1
              }
              i += 1
            }
            if (ok) ans += 1
            c2 += 1
          }
          c1 += 1
        }
        r2 += 1
      }
      r1 += 1
    }
    ans
  }
}
