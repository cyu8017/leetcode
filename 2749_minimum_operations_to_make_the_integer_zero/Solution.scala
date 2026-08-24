// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

object Solution {
  def makeTheIntegerZero(num1: Int, num2: Int): Int = {
    var k = 1
    while (k <= 60) {
      val rem = num1.toLong - k.toLong * num2
      if (rem >= k && java.lang.Long.bitCount(rem) <= k) return k
      k += 1
    }
    -1
  }
}
