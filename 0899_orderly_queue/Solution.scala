// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

object Solution {
  def orderlyQueue(s: String, k: Int): String = {
    if (k > 1) return s.sorted
    var best = s
    var i = 1
    while (i < s.length) {
      val cand = s.substring(i) + s.substring(0, i)
      if (cand < best) best = cand
      i += 1
    }
    best
  }
}
