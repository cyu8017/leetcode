// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

object Solution {
  def maximumRemovals(s: String, p: String, removable: Array[Int]): Int = {
    def stillSubsequence(k: Int): Boolean = {
      val removed = removable.take(k).toSet
      var index = 0
      for (position <- s.indices if !removed.contains(position)) {
        if (index < p.length && s(position) == p(index)) index += 1
      }
      index == p.length
    }

    var lo = 0
    var hi = removable.length
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (stillSubsequence(mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
