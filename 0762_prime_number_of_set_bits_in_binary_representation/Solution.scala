// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

object Solution {
  def countPrimeSetBits(left: Int, right: Int): Int = {
    val primes = Set(2, 3, 5, 7, 11, 13, 17, 19)
    var ans = 0
    var num = left
    while (num <= right) {
      if (primes.contains(Integer.bitCount(num))) ans += 1
      num += 1
    }
    ans
  }
}
