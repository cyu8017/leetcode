// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

object Solution {
  def checkAlmostEquivalent(word1: String, word2: String): Boolean = {
    val freq = Array.ofDim[Int](26)
    var i = 0
    while (i < word1.length) {
      freq(word1.charAt(i) - 'a') += 1
      freq(word2.charAt(i) - 'a') -= 1
      i += 1
    }
    freq.forall { v => v <= 3 && v >= -3 }
  }
}
