// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

object Solution {
  def numberOfSubmatrices(grid: Array[Array[Char]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val s = Array.ofDim[Int](m + 1, n + 1, 2)
    var ans = 0
    var i = 1
    while (i <= m) {
      var j = 1
      while (j <= n) {
        s(i)(j)(0) = s(i - 1)(j)(0) + s(i)(j - 1)(0) - s(i - 1)(j - 1)(0)
        if (grid(i - 1)(j - 1) == 'X') s(i)(j)(0) += 1
        s(i)(j)(1) = s(i - 1)(j)(1) + s(i)(j - 1)(1) - s(i - 1)(j - 1)(1)
        if (grid(i - 1)(j - 1) == 'Y') s(i)(j)(1) += 1
        if (s(i)(j)(0) > 0 && s(i)(j)(0) == s(i)(j)(1)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
