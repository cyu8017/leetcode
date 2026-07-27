// LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

object Solution {
  def minimumOneBitOperations(n: Int): Int = {
    var x = n
    var ans = 0
    while (x != 0) {
      ans ^= x
      x >>= 1
    }
    ans
  }
}
