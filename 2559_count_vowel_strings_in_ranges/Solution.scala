// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

object Solution {
  def vowelStrings(words: Array[String], queries: Array[Array[Int]]): Array[Int] = {
    val n = words.length
    val pref = Array.fill(n + 1)(0)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i)
      val w = words(i)
      if (w.nonEmpty && isV(w.head) && isV(w.last)) pref(i + 1) += 1
      i += 1
    }
    val ans = Array.fill(queries.length)(0)
    i = 0
    while (i < queries.length) {
      ans(i) = pref(queries(i)(1) + 1) - pref(queries(i)(0))
      i += 1
    }
    ans
  }

  private def isV(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
