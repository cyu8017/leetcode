// LeetCode 3370 - Smallest Number With All Set Bits
// https://leetcode.com/problems/smallest-number-with-all-set-bits/

object Solution {
  def smallestNumber(n: Int): Int = {
    var x = 1
    while (x < n) x = x * 2 + 1
    x
  }
}
