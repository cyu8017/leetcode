// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

object Solution {
  def findValidPair(s: String): String = {
    val freq = new Array[Int](10)
    s.foreach { c => freq(c - '0') += 1 }
    var i = 0
    while (i + 1 < s.length) {
      val a = s.charAt(i) - '0'
      val b = s.charAt(i + 1) - '0'
      if (a != b && freq(a) == a && freq(b) == b) return s.substring(i, i + 2)
      i += 1
    }
    ""
  }
}
