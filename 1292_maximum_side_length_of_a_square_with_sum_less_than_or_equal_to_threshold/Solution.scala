// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

object Solution {
  def maxSideLength(mat: Array[Array[Int]], threshold: Int): Int = {
    val m = mat.length
    val n = mat(0).length
    val prefix = Array.ofDim[Int](m + 1, n + 1)
    for (r <- 0 until m; c <- 0 until n) {
      prefix(r + 1)(c + 1) = mat(r)(c) + prefix(r)(c + 1) + prefix(r + 1)(c) - prefix(r)(c)
    }
    def possible(size: Int): Boolean = {
      for (r <- size to m; c <- size to n) {
        val sum = prefix(r)(c) - prefix(r - size)(c) - prefix(r)(c - size) + prefix(r - size)(c - size)
        if (sum <= threshold) return true
      }
      false
    }
    var lo = 0
    var hi = math.min(m, n)
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (possible(mid)) lo = mid else hi = mid - 1
    }
    lo
  }
}
