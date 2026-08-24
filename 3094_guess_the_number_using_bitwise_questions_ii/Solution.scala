// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

object Solution {
  def commonBits(num: Int): Int = throw new NotImplementedError()

  def findNumber(): Int = {
    var n = 0
    var i = 0
    while (i < 32) {
      val count1 = commonBits(1 << i)
      val count2 = commonBits(1 << i)
      if (count1 > count2) n |= 1 << i
      i += 1
    }
    n
  }
}
