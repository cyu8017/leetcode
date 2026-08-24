// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

object Solution {
  def checkDistances(s: String, distance: Array[Int]): Boolean = {
    val first = Array.fill(26)(-1)
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i) - 'a'
      if (first(c) == -1) first(c) = i
      else if (i - first(c) - 1 != distance(c)) return false
      i += 1
    }
    true
  }
}
