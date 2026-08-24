// LeetCode 3871 - Count Commas In Range Ii
// https://leetcode.com/problems/count-commas-in-range-ii/

object Solution {
  def countCommas(n: Long): Long = {
    var ans = 0L
    var x = 1000L
    while (x <= n) {
      ans += n - x + 1
      x *= 1000
    }
    ans
  }
}
