// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

object Solution {
  def splitWordsBySeparator(words: List[String], separator: Char): List[String] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    words.foreach { w =>
      var start = 0
      var i = 0
      while (i <= w.length) {
        if (i == w.length || w.charAt(i) == separator) {
          if (i > start) ans += w.substring(start, i)
          start = i + 1
        }
        i += 1
      }
    }
    ans.toList
  }
}
