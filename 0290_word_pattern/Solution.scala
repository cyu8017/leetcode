// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

import scala.collection.mutable

object Solution {
  def wordPattern(pattern: String, s: String): Boolean = {
    val words = s.split(" ")
    if (pattern.length != words.length) {
      return false
    }
    val charToWord = mutable.Map.empty[Char, String]
    val wordToChar = mutable.Map.empty[String, Char]
    for (index <- pattern.indices) {
      val ch = pattern(index)
      val word = words(index)
      if (charToWord.contains(ch)) {
        if (charToWord(ch) != word) {
          return false
        }
      } else {
        if (wordToChar.contains(word)) {
          return false
        }
        charToWord(ch) = word
        wordToChar(word) = ch
      }
    }
    true
  }
}
