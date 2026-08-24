// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

object Solution {
  def generateTag(caption: String): String = {
    val ans = new StringBuilder("#")
    val words = caption.trim.split("\\s+")
    var i = 0
    var done = false
    for (word <- words if !done) {
      if (word.nonEmpty) {
        val w = new StringBuilder(word.toLowerCase)
        if (i == 0) ans.append(w)
        else {
          if (w.length > 0) w.setCharAt(0, Character.toUpperCase(w.charAt(0)))
          ans.append(w)
        }
        if (ans.length >= 100) done = true
        else i += 1
      }
    }
    if (ans.length > 100) ans.setLength(100)
    ans.toString
  }
}
