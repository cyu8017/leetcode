// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

import scala.collection.mutable

class AutocompleteSystem(sentences: Array[String], times: Array[Int]) {
  private val counts = mutable.Map.empty[String, Int]
  private val current = new StringBuilder

  {
    var i = 0
    while (i < sentences.length) {
      counts(sentences(i)) = counts.getOrElse(sentences(i), 0) + times(i)
      i += 1
    }
  }

  def input(c: Char): List[String] = {
    if (c == '#') {
      val sentence = current.toString
      counts(sentence) = counts.getOrElse(sentence, 0) + 1
      current.setLength(0)
      return List.empty
    }
    current.append(c)
    val prefix = current.toString
    val matches = mutable.ArrayBuffer.empty[String]
    counts.keys.foreach { sentence =>
      if (sentence.startsWith(prefix)) matches += sentence
    }
    val sorted = matches.sortWith { (a, b) =>
      val ca = counts(a)
      val cb = counts(b)
      if (ca != cb) ca > cb else a < b
    }
    if (sorted.size > 3) sorted.take(3).toList else sorted.toList
  }
}
