// LeetCode 0231 - Power of Two
// https://leetcode.com/problems/power-of-two/

object Solution {
  def isPowerOfTwo(n: Int): Boolean = {
    n > 0 && (n & (n - 1)) == 0
  }
}
