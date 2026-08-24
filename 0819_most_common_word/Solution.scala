// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

object Solution {
  def mostCommonWord(paragraph: String, banned: Array[String]): String = {
    val bannedSet = banned.toSet
    val counts = scala.collection.mutable.Map.empty[String, Int]
    val word = new StringBuilder
    var best = ""
    var bestCount = 0
    var i = 0
    while (i <= paragraph.length) {
      val ch = if (i < paragraph.length) paragraph.charAt(i) else ' '
      if (ch.isLetter) word.append(ch.toLower)
      else if (word.nonEmpty) {
        val w = word.toString
        word.clear()
        if (!bannedSet.contains(w)) {
          val c = counts.getOrElse(w, 0) + 1
          counts(w) = c
          if (c > bestCount) {
            bestCount = c
            best = w
          }
        }
      }
      i += 1
    }
    best
  }
}
