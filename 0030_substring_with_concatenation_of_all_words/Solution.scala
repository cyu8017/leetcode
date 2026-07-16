// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

import scala.collection.mutable

object Solution {
  def findSubstring(s: String, words: Array[String]): List[Int] = {
    if (words.isEmpty || s.isEmpty) {
      return List.empty
    }

    val wordLen = words(0).length
    val wordCount = words.length
    val need = words.groupBy(identity).view.mapValues(_.length).toMap
    val result = mutable.ListBuffer.empty[Int]

    var start = 0
    while (start < wordLen) {
      var left = start
      val counts = mutable.Map.empty[String, Int].withDefaultValue(0)
      var used = 0
      var right = start

      while (right <= s.length - wordLen) {
        val word = s.substring(right, right + wordLen)
        if (!need.contains(word)) {
          counts.clear()
          used = 0
          left = right + wordLen
          right += wordLen
        } else {
          counts(word) += 1
          used += 1

          while (counts(word) > need(word)) {
            val leftWord = s.substring(left, left + wordLen)
            counts(leftWord) -= 1
            used -= 1
            left += wordLen
          }

          if (used == wordCount) {
            result += left
          }

          right += wordLen
        }
      }

      start += 1
    }

    result.sorted.toList
  }
}
