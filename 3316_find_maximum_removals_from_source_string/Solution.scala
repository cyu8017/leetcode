// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

object Solution {
  def maxRemovals(source: String, pattern: String, targetIndices: Array[Int]): Int = {
    val n = source.length
    var lo = 0
    var hi = targetIndices.length
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid, source, pattern, targetIndices, n)) lo = mid
      else hi = mid - 1
    }
    lo
  }

  private def ok(removeFirst: Int, source: String, pattern: String, targetIndices: Array[Int], n: Int): Boolean = {
    val mark = new Array[Boolean](n)
    var i = 0
    while (i < removeFirst) {
      mark(targetIndices(i)) = true
      i += 1
    }
    var j = 0
    i = 0
    while (i < n && j < pattern.length) {
      if (!mark(i) && source.charAt(i) == pattern.charAt(j)) j += 1
      i += 1
    }
    j == pattern.length
  }
}
