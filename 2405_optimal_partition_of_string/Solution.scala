// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

object Solution {
  def partitionString(s: String): Int = {
    var ans = 1
    var seen = 0
    s.foreach { c =>
      val bit = 1 << (c - 'a')
      if ((seen & bit) != 0) {
        ans += 1
        seen = 0
      }
      seen |= bit
    }
    ans
  }
}
