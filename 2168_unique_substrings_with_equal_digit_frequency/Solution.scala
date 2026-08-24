// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

object Solution {
  def equalDigitFrequency(s: String): Int = {
    val n = s.length
    val seen = scala.collection.mutable.Set.empty[String]
    var i = 0
    while (i < n) {
      val freq = Array.fill(10)(0)
      var maxf = 0
      var kinds = 0
      var j = i
      while (j < n) {
        val d = s.charAt(j) - '0'
        if (freq(d) == 0) kinds += 1
        freq(d) += 1
        maxf = math.max(maxf, freq(d))
        if (maxf * kinds == j - i + 1) seen += s.substring(i, j + 1)
        j += 1
      }
      i += 1
    }
    seen.size
  }
}
