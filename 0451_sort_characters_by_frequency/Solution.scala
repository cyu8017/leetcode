// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

import scala.collection.mutable

object Solution {
  def frequencySort(s: String): String = {
    val counts = mutable.Map.empty[Char, Int]
    s.foreach(ch => counts(ch) = counts.getOrElse(ch, 0) + 1)
    counts.toSeq
      .sortBy { case (ch, count) => (-count, ch) }
      .map { case (ch, count) => ch.toString * count }
      .mkString
  }
}
