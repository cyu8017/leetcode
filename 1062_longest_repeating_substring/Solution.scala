// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

object Solution {
  def longestRepeatingSubstring(s: String): Int = {
    val n = s.length
    def hasDup(length: Int): Boolean = {
      val seen = scala.collection.mutable.Set.empty[String]
      for (i <- 0 to n - length) {
        val sub = s.substring(i, i + length)
        if (seen.contains(sub)) return true
        seen += sub
      }
      false
    }
    var lo = 1
    var hi = n - 1
    var ans = 0
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (hasDup(mid)) { ans = mid; lo = mid + 1 } else hi = mid - 1
    }
    ans
  }
}
