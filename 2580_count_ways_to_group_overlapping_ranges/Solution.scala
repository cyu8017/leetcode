// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

object Solution {
  def countWays(ranges: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val sorted = ranges.sortBy(_(0))
    var groups = 0
    var end = -1
    sorted.foreach { r =>
      if (r(0) > end) {
        groups += 1
        end = r(1)
      } else if (r(1) > end) {
        end = r(1)
      }
    }
    var ans = 1
    var i = 0
    while (i < groups) {
      ans = ans * 2 % MOD
      i += 1
    }
    ans
  }
}
