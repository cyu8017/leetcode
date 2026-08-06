// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

object Solution {
  def numOfStrings(patterns: Array[String], word: String): Int =
    patterns.count(word.contains)
}
