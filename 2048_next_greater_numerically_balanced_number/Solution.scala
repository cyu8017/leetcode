// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

object Solution {
  def nextBeautifulNumber(n: Int): Int = {
    def balanced(x0: Int): Boolean = {
      val cnt = Array.ofDim[Int](10)
      var x = x0
      while (x > 0) { cnt(x % 10) += 1; x /= 10 }
      var d = 0
      while (d < 10) {
        if (cnt(d) != 0 && cnt(d) != d) return false
        d += 1
      }
      true
    }
    var x = n + 1
    while (true) {
      if (balanced(x)) return x
      x += 1
    }
    0
  }
}
