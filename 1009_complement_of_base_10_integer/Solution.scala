// LeetCode 1009 - Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/

object Solution {
  def bitwiseComplement(n: Int): Int = {
    if (n == 0) return 1
    val bits = 32 - Integer.numberOfLeadingZeros(n)
    val mask = (1 << bits) - 1
    n ^ mask
  }
}
