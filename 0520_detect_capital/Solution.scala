// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

object Solution {
  def detectCapitalUse(word: String): Boolean = {
    word == word.toUpperCase ||
      word == word.toLowerCase ||
      word == word.head.toUpper + word.tail.toLowerCase
  }
}
