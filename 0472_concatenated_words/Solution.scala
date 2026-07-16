// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

import scala.collection.mutable

object Solution {
  def findAllConcatenatedWordsInADict(words: Array[String]): List[String] = {
    val sorted = words.sortBy(_.length)
    val wordSet = mutable.Set.from(sorted)
    val result = mutable.ArrayBuffer.empty[String]

    def canForm(word: String, dictionary: mutable.Set[String]): Boolean = {
      if (word.isEmpty) return true
      val length = word.length
      val dp = Array.fill(length + 1)(false)
      dp(0) = true
      var end = 1
      while (end <= length) {
        var start = 0
        while (start < end) {
          if (dp(start) && dictionary.contains(word.substring(start, end))) {
            dp(end) = true
          }
          start += 1
        }
        end += 1
      }
      dp(length)
    }

    sorted.foreach { word =>
      wordSet -= word
      if (canForm(word, wordSet)) {
        result += word
      }
      wordSet += word
    }
    result.toList
  }
}
