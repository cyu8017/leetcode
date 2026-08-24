// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

object Solution {
  def vowelStrings(words: Array[String], left: Int, right: Int): Int = {
    var ans = 0
    var i = left
    while (i <= right) {
      val w = words(i)
      if (isV(w.charAt(0)) && isV(w.charAt(w.length - 1))) ans += 1
      i += 1
    }
    ans
  }

  private def isV(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
