// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

object Solution {
  def maxProduct(s: String): Long = {
    val n = s.length
    val radius = Array.ofDim[Int](n)
    var center = 0
    var right = 0
    for (i <- 0 until n) {
      if (i < right) radius(i) = math.min(right - i, radius(2 * center - i))
      while (
        i - radius(i) - 1 >= 0 &&
        i + radius(i) + 1 < n &&
        s.charAt(i - radius(i) - 1) == s.charAt(i + radius(i) + 1)
      ) radius(i) += 1
      if (i + radius(i) > right) {
        center = i
        right = i + radius(i)
      }
    }
    val end = Array.fill(n)(1)
    val start = Array.fill(n)(1)
    for (i <- 0 until n) {
      val r = radius(i)
      end(i + r) = math.max(end(i + r), 2 * r + 1)
      start(i - r) = math.max(start(i - r), 2 * r + 1)
    }
    for (i <- n - 2 to 0 by -1) end(i) = math.max(end(i), end(i + 1) - 2)
    for (i <- 1 until n) start(i) = math.max(start(i), start(i - 1) - 2)
    val pre = Array.ofDim[Int](n)
    pre(0) = end(0)
    for (i <- 1 until n) pre(i) = math.max(pre(i - 1), end(i))
    val suf = Array.ofDim[Int](n)
    suf(n - 1) = start(n - 1)
    for (i <- n - 2 to 0 by -1) suf(i) = math.max(suf(i + 1), start(i))
    var ans = 0L
    for (i <- 0 until n - 1) ans = math.max(ans, pre(i).toLong * suf(i + 1))
    ans
  }
}
