// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

object Solution {
  def atMostNGivenDigitSet(digits: Array[String], n: Int): Int = {
    val k = digits.length
    val s = n.toString
    val m = s.length
    def ipow(bas: Int, exp: Int): Int = {
      var r = 1
      var e = exp
      while (e > 0) { r *= bas; e -= 1 }
      r
    }
    def countUpTo(t: String): Int = {
      if (t.isEmpty) return 0
      var first = 0
      digits.foreach { d => if (d.charAt(0) < t.charAt(0)) first += 1 }
      var ways = first * ipow(k, t.length - 1)
      val found = digits.exists(_.charAt(0) == t.charAt(0))
      if (found) ways += countUpTo(t.substring(1))
      ways
    }
    var ans = 0
    var i = 1
    while (i < m) {
      ans += ipow(k, i)
      i += 1
    }
    ans + countUpTo(s)
  }
}
