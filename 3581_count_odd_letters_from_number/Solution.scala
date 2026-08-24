// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

object Solution {
  def countOddLetters(n0: Int): Int = {
    val d = Array("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    var n = n0
    var mask = 0
    while (n > 0) {
      for (c <- d(n % 10).toCharArray) mask ^= 1 << (c - 'a')
      n /= 10
    }
    Integer.bitCount(mask)
  }
}
