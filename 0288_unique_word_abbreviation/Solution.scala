// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

import scala.collection.mutable

class ValidWordAbbr(dictionary: Array[String]) {
  private val groups = mutable.Map.empty[String, mutable.Set[String]].withDefaultValue(mutable.Set.empty)

  dictionary.foreach { word =>
    val key = ValidWordAbbr.abbreviate(word)
    groups(key).add(word)
  }

  def isUnique(word: String): Boolean = {
    val key = ValidWordAbbr.abbreviate(word)
    val words = groups.getOrElse(key, mutable.Set.empty)
    words.isEmpty || (words.size == 1 && words.contains(word))
  }
}

object ValidWordAbbr {
  private def abbreviate(word: String): String = {
    if (word.length <= 2) {
      word
    } else {
      s"${word.head}${word.length - 2}${word.last}"
    }
  }
}
