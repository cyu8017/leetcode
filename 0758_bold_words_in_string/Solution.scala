// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

object Solution {
  def boldWords(words: Array[String], s: String): String = {
    val n = s.length
    val bold = Array.fill(n)(false)
    for (word <- words) {
      var start = s.indexOf(word)
      while (start >= 0) {
        var i = start
        while (i < start + word.length) {
          bold(i) = true
          i += 1
        }
        start = s.indexOf(word, start + 1)
      }
    }
    val parts = new StringBuilder
    var i = 0
    while (i < n) {
      if (bold(i)) {
        parts.append("**")
        while (i < n && bold(i)) {
          parts.append(s.charAt(i))
          i += 1
        }
        parts.append("**")
      } else {
        parts.append(s.charAt(i))
        i += 1
      }
    }
    parts.toString
  }
}
