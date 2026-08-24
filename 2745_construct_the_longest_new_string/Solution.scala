// LeetCode 2745 - Construct the Longest New String
// https://leetcode.com/problems/construct-the-longest-new-string/

object Solution {
  def longestString(x: Int, y: Int, z: Int): Int = {
    if (x < y) (2 * x + 1 + z) * 2
    else if (y < x) (2 * y + 1 + z) * 2
    else (x + y + z) * 2
  }
}
