// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

object Solution {
  private val rows = Array(
    "qwertyuiop".toSet,
    "asdfghjkl".toSet,
    "zxcvbnm".toSet,
  )

  def findWords(words: Array[String]): Array[String] = {
    words.filter { word =>
      val letters = word.filter(_.isLetter).map(_.toLower).toSet
      rows.exists(row => letters.subsetOf(row))
    }
  }
}
