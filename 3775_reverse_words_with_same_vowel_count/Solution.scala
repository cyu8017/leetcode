// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

object Solution {
  private def calc(w: String): Int = {
    var cnt = 0
    w.foreach { c =>
      if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt += 1
    }
    cnt
  }

  def reverseWords(s: String): String = {
    val words = s.trim.split("\\s+")
    val cnt = calc(words(0))
    val ans = new StringBuilder
    ans.append(words(0))
    var i = 1
    while (i < words.length) {
      var w = words(i)
      if (calc(w) == cnt) w = new java.lang.StringBuilder(w).reverse().toString
      ans.append(' ').append(w)
      i += 1
    }
    ans.toString
  }
}
