// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

object Solution {
  def countValidWords(sentence: String): Int = {
    sentence.split(" ").count(valid)
  }

  private def valid(w: String): Boolean = {
    if (w.isEmpty) return false
    var hyphen = 0
    var i = 0
    while (i < w.length) {
      val c = w.charAt(i)
      if (c >= '0' && c <= '9') return false
      if (c == '-') {
        hyphen += 1
        if (hyphen > 1 || i == 0 || i == w.length - 1) return false
        if (w.charAt(i - 1) < 'a' || w.charAt(i - 1) > 'z' || w.charAt(i + 1) < 'a' || w.charAt(i + 1) > 'z') return false
      } else if (c == '!' || c == '.' || c == ',') {
        if (i != w.length - 1) return false
      } else if (c < 'a' || c > 'z') return false
      i += 1
    }
    true
  }
}
