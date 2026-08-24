// LeetCode 3993 - Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

object Solution {
  def maximumValue(n: Int, s: Int, m: Int): Long = {
    if (n == 1) s
    else s.toLong + (n / 2).toLong * (m - 1) + 1
  }
}
