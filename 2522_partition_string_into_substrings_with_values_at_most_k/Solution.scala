// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

object Solution {
  def minimumPartition(s: String, k: Int): Int = {
    var ans = 1
    var cur = 0L
    s.foreach { ch =>
      val d = ch - '0'
      if (d > k) return -1
      val nxt = cur * 10 + d
      if (nxt > k) {
        ans += 1
        cur = d
      } else {
        cur = nxt
      }
    }
    ans
  }
}
