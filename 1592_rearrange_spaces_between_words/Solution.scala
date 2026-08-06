// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

object Solution {
  def reorderSpaces(text: String): String = {
    val words = text.split("\\s+").filter(_.nonEmpty)
    val spaces = text.count(_ == ' ')
    if (words.length == 1) return words(0) + (" " * spaces)
    val between = spaces / (words.length - 1)
    val trailing = spaces % (words.length - 1)
    words.mkString(" " * between) + (" " * trailing)
  }
}
