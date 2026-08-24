// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

object Solution {
  def maxNumber(n: Long): Long = {
    val len = 64 - java.lang.Long.numberOfLeadingZeros(n)
    (1L << (len - 1)) - 1
  }
}
