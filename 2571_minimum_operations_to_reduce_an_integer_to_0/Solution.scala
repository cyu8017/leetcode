// LeetCode 2571 - Minimum Operations to Reduce an Integer to 0
// https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

object Solution {
  def minOperations(n0: Int): Int = {
    var n = n0
    var ans = 0
    while (n > 0) {
      if ((n & 3) == 3) {
        n += 1
        ans += 1
      } else if ((n & 1) != 0) {
        n -= 1
        ans += 1
      } else {
        n >>= 1
      }
    }
    ans
  }
}
