// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

object Solution {
  def countSymmetricIntegers(low: Int, high: Int): Int = {
    var ans = 0
    for (x <- low to high) {
      val s = x.toString
      if (s.length % 2 == 0) {
        val mid = s.length / 2
        var a = 0
        var b = 0
        for (i <- 0 until mid) {
          a += s.charAt(i) - '0'
          b += s.charAt(mid + i) - '0'
        }
        if (a == b) ans += 1
      }
    }
    ans
  }
}
