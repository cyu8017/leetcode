// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

object Solution {
  def addBoldTag(s: String, words: Array[String]): String = {
    val n = s.length
    val bold = Array.fill(n)(false)
    words.foreach { word =>
      var start = s.indexOf(word)
      while (start >= 0) {
        var i = start
        while (i < start + word.length) { bold(i) = true; i += 1 }
        start = s.indexOf(word, start + 1)
      }
    }
    val parts = new StringBuilder
    var i = 0
    while (i < n) {
      if (bold(i)) {
        parts.append("<b>")
        while (i < n && bold(i)) { parts.append(s.charAt(i)); i += 1 }
        parts.append("</b>")
      } else {
        parts.append(s.charAt(i))
        i += 1
      }
    }
    parts.toString
  }
}
