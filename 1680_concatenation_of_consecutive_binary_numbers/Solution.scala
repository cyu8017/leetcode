// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

object Solution {
  def concatenatedBinary(n: Int): Int = {
    var ans = 0L
    var bits = 0
    val mod = 1000000007L
    for (x <- 1 to n) {
      if ((x & (x - 1)) == 0) bits += 1
      ans = ((ans << bits) % mod + x) % mod
    }
    ans.toInt
  }
}
