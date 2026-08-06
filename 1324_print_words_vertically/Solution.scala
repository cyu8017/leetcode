// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

object Solution {
  def printVertically(s: String): List[String] = {
    val words = s.split(" ")
    val maxLen = words.map(_.length).max
    (0 until maxLen).map { i =>
      words.map(word => if (i < word.length) word(i).toString else " ").mkString.replaceAll("\\s+$", "")
    }.toList
  }
}
