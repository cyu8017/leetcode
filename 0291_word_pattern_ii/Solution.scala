// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

import scala.collection.mutable

object Solution {
  def wordPatternMatch(pattern: String, s: String): Boolean =
    backtrack(pattern, s, 0, 0, mutable.Map.empty, mutable.Map.empty)

  private def backtrack(
      pattern: String,
      s: String,
      patternIndex: Int,
      stringIndex: Int,
      charToWord: mutable.Map[Char, String],
      wordToChar: mutable.Map[String, Char],
  ): Boolean = {
    if (patternIndex == pattern.length) {
      return stringIndex == s.length
    }
    val ch = pattern(patternIndex)
    charToWord.get(ch) match {
      case Some(word) =>
        if (!s.startsWith(word, stringIndex)) {
          false
        } else {
          backtrack(pattern, s, patternIndex + 1, stringIndex + word.length, charToWord, wordToChar)
        }
      case None =>
        var end = stringIndex + 1
        while (end <= s.length) {
          val word = s.substring(stringIndex, end)
          if (!wordToChar.contains(word)) {
            charToWord(ch) = word
            wordToChar(word) = ch
            if (backtrack(pattern, s, patternIndex + 1, end, charToWord, wordToChar)) {
              return true
            }
            charToWord.remove(ch)
            wordToChar.remove(word)
          }
          end += 1
        }
        false
    }
  }
}
