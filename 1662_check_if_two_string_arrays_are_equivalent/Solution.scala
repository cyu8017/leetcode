// LeetCode 1662 - Check If Two String Arrays are Equivalent
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

object Solution {
  def arrayStringsAreEqual(word1: Array[String], word2: Array[String]): Boolean =
    word1.mkString == word2.mkString
}
