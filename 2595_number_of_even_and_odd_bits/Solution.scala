// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

object Solution {
  def evenOddBit(n0: Int): Array[Int] = {
    var n = n0
    var even = 0
    var odd = 0
    var i = 0
    while (n > 0) {
      if ((n & 1) != 0) {
        if (i % 2 == 0) even += 1
        else odd += 1
      }
      i += 1
      n >>= 1
    }
    Array(even, odd)
  }
}
