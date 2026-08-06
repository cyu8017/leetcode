// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

object Solution {
  def minFlips(target: String): Int = {
    var ans = 0
    var prev = '0'
    for (ch <- target) {
      if (ch != prev) {
        ans += 1
        prev = ch
      }
    }
    ans
  }
}
