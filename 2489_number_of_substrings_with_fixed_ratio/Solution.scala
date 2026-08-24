// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

object Solution {
  def fixedRatio(s: String, num1: Int, num2: Int): Long = {
    val pref = scala.collection.mutable.Map[Long, Int](0L -> 1)
    var zeros = 0
    var ones = 0
    var ans = 0L
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') zeros += 1 else ones += 1
      val key = zeros.toLong * num2 - ones.toLong * num1
      ans += pref.getOrElse(key, 0)
      pref(key) = pref.getOrElse(key, 0) + 1
      i += 1
    }
    ans
  }
}
