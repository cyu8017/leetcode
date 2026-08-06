// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

object Solution {
  def areOccurrencesEqual(s: String): Boolean = {
    val freq = s.groupBy(identity).map(_._2.length)
    freq.toSet.size == 1
  }
}
