// LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
// https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

object Solution {
  def minChanges(n: Int, k: Int): Int = {
    if ((n & k) != k) -1 else Integer.bitCount(n ^ k)
  }
}
