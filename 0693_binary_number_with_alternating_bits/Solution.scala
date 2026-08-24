// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

object Solution {
  def hasAlternatingBits(n: Int): Boolean = {
    val x = n ^ (n >>> 1)
    (x & (x + 1)) == 0
  }
}
