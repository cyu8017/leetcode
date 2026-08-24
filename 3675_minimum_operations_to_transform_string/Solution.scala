// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

object Solution {
  def minOperations(s: String): Int = {
    var ans = 0
    for (c <- s) {
      if (c != 'a') ans = math.max(ans, 26 - (c - 'a'))
    }
    ans
  }
}
