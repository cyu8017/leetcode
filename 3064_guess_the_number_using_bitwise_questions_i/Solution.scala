// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

object Solution {
  def commonSetBits(num: Int): Int = throw new NotImplementedError()

  def findNumber(): Int = {
    var n = 0
    var i = 0
    while (i < 32) {
      if (commonSetBits(1 << i) > 0) n |= 1 << i
      i += 1
    }
    n
  }
}
