// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

object Solution {
  def commonFactors(a: Int, b: Int): Int = {
    def gcd(x: Int, y: Int): Int = {
      var aa = x
      var bb = y
      while (bb != 0) {
        val t = aa % bb
        aa = bb
        bb = t
      }
      aa
    }
    val g = gcd(a, b)
    var ans = 0
    var i = 1
    while (i.toLong * i <= g) {
      if (g % i == 0) {
        ans += 1
        if (i.toLong * i != g) ans += 1
      }
      i += 1
    }
    ans
  }
}
