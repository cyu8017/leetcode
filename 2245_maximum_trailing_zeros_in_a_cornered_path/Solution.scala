// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

object Solution {
  def maxTrailingZeros(grid: Array[Array[Int]]): Int = {
    def fact(x0: Int): Array[Int] = {
      var x = x0
      var t = 0
      var f = 0
      while (x % 2 == 0) { t += 1; x /= 2 }
      while (x % 5 == 0) { f += 1; x /= 5 }
      Array(t, f)
    }
    val m = grid.length
    val n = grid(0).length
    val left2 = Array.ofDim[Int](m, n)
    val left5 = Array.ofDim[Int](m, n)
    val up2 = Array.ofDim[Int](m, n)
    val up5 = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val p = fact(grid(i)(j))
        left2(i)(j) = p(0)
        up2(i)(j) = p(0)
        left5(i)(j) = p(1)
        up5(i)(j) = p(1)
        if (j > 0) {
          left2(i)(j) += left2(i)(j - 1)
          left5(i)(j) += left5(i)(j - 1)
        }
        if (i > 0) {
          up2(i)(j) += up2(i - 1)(j)
          up5(i)(j) += up5(i - 1)(j)
        }
        j += 1
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val cell = fact(grid(i)(j))
        val L2 = left2(i)(j)
        val L5 = left5(i)(j)
        val R2 = left2(i)(n - 1) - left2(i)(j) + cell(0)
        val R5 = left5(i)(n - 1) - left5(i)(j) + cell(1)
        val U2 = up2(i)(j)
        val U5 = up5(i)(j)
        val D2 = up2(m - 1)(j) - up2(i)(j) + cell(0)
        val D5 = up5(m - 1)(j) - up5(i)(j) + cell(1)
        val cands = Array(
          Array(L2 + U2 - cell(0), L5 + U5 - cell(1)),
          Array(L2 + D2 - cell(0), L5 + D5 - cell(1)),
          Array(R2 + U2 - cell(0), R5 + U5 - cell(1)),
          Array(R2 + D2 - cell(0), R5 + D5 - cell(1))
        )
        for (c <- cands) ans = math.max(ans, math.min(c(0), c(1)))
        j += 1
      }
      i += 1
    }
    ans
  }
}
