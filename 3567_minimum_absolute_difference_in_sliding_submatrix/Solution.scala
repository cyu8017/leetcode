// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

object Solution {
  def minAbsDiff(grid: Array[Array[Int]], k: Int): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val ans = Array.ofDim[Int](m - k + 1, n - k + 1)
    var i = 0
    while (i <= m - k) {
      var j = 0
      while (j <= n - k) {
        val nums = new java.util.ArrayList[Integer]()
        var x = i
        while (x < i + k) {
          var y = j
          while (y < j + k) { nums.add(grid(x)(y)); y += 1 }
          x += 1
        }
        nums.sort(null)
        var d = Integer.MAX_VALUE
        var t = 1
        while (t < nums.size()) {
          if (nums.get(t) != nums.get(t - 1))
            d = math.min(d, math.abs(nums.get(t) - nums.get(t - 1)))
          t += 1
        }
        if (d != Integer.MAX_VALUE) ans(i)(j) = d
        j += 1
      }
      i += 1
    }
    ans
  }
}
