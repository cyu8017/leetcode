// LeetCode 2119 - A Number After a Double Reversal
// https://leetcode.com/problems/a-number-after-a-double-reversal/

object Solution {
  def isSameAfterReversals(num: Int): Boolean = {
    num == 0 || num % 10 != 0
  }
}
