// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

object Solution {
  def superpalindromesInRange(left: String, right: String): Int = {
    val L = left.toLong
    val R = right.toLong
    def isPal(x: Long): Boolean = {
      val s = x.toString
      val n = s.length
      var i = 0
      while (i < n / 2) {
        if (s.charAt(i) != s.charAt(n - 1 - i)) return false
        i += 1
      }
      true
    }
    var ans = 0
    var k = 1L
    var stop = false
    while (k <= 100000 && !stop) {
      val s = k.toString
      val pal = (s + s.reverse).toLong
      val sq = pal * pal
      if (sq > R) stop = true
      else {
        if (sq >= L && isPal(sq)) ans += 1
        k += 1
      }
    }
    k = 1L
    stop = false
    while (k <= 100000 && !stop) {
      val s = k.toString
      val pal = (s + s.substring(0, s.length - 1).reverse).toLong
      val sq = pal * pal
      if (sq > R) stop = true
      else {
        if (sq >= L && isPal(sq)) ans += 1
        k += 1
      }
    }
    ans
  }
}
