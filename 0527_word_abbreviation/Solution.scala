// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

import scala.collection.mutable

object Solution {
  def wordsAbbreviation(words: Array[String]): Array[String] = {
    val prefixes = Array.fill(words.length)(1)
    var changed = true
    while (changed) {
      changed = false
      val groups = mutable.Map.empty[String, mutable.ArrayBuffer[Int]]
      for ((word, index) <- words.zipWithIndex) {
        val key = abbreviate(word, prefixes(index))
        groups.getOrElseUpdate(key, mutable.ArrayBuffer.empty[Int]) += index
      }
      for (indices <- groups.values if indices.size > 1) {
        changed = true
        for (index <- indices) {
          prefixes(index) += 1
        }
      }
    }
    words.indices.map(index => abbreviate(words(index), prefixes(index))).toArray
  }

  private def abbreviate(word: String, prefix: Int): String = {
    if (prefix + 2 >= word.length) {
      return word
    }
    val middle = word.length - prefix - 1
    val candidate = word.substring(0, prefix) + middle + word.last
    if (candidate.length < word.length) candidate else word
  }
}
