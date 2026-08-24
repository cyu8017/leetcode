// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

object Solution {
  def largestLocal(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val n = grid.length
    val ans = Array.ofDim[Int](n - 2, n - 2)
    var i = 0
    while (i < n - 2) {
      var j = 0
      while (j < n - 2) {
        var mx = 0
        var r = i
        while (r < i + 3) {
          var c = j
          while (c < j + 3) {
            if (grid(r)(c) > mx) mx = grid(r)(c)
            c += 1
          }
          r += 1
        }
        ans(i)(j) = mx
        j += 1
      }
      i += 1
    }
    ans
  }
}
