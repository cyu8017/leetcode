// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

object Solution {
  def uniqueOccurrences(arr: Array[Int]): Boolean = {
    val counts = arr.groupBy(identity).values.map(_.length).toSeq
    counts.size == counts.toSet.size
  }
}
