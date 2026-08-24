// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

object Solution {
  def numDecodings(s: String): Int = {
    val mod = 1000000007
    var prev2 = 1L
    var prev1 = one(s.charAt(0)).toLong
    var i = 1
    while (i < s.length) {
      val cur = (one(s.charAt(i)) * prev1 + two(s.charAt(i - 1), s.charAt(i)) * prev2) % mod
      prev2 = prev1
      prev1 = cur
      i += 1
    }
    prev1.toInt
  }

  private def one(ch: Char): Int = {
    if (ch == '*') 9
    else if (ch == '0') 0
    else 1
  }

  private def two(a: Char, b: Char): Int = {
    if (a == '*' && b == '*') return 15
    if (a == '*') return if (b <= '6') 2 else 1
    if (b == '*') {
      if (a == '1') return 9
      if (a == '2') return 6
      return 0
    }
    val value = (a - '0') * 10 + (b - '0')
    if (value >= 10 && value <= 26) 1 else 0
  }
}
