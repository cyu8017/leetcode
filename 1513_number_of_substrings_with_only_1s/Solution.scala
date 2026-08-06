// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

object Solution {
  def numSub(s: String): Int = {
    var ans = 0L
    var run = 0
    for (ch <- s) {
      run = if (ch == '1') run + 1 else 0
      ans += run
    }
    (ans % 1000000007L).toInt
  }
}
