// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

object Solution {
  private def popcount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def maxPalindromesAfterOperations(words: Array[String]): Int = {
    var s = 0
    var mask = 0
    for (w <- words) {
      s += w.length
      var i = 0
      while (i < w.length) { mask ^= 1 << (w.charAt(i) - 'a'); i += 1 }
    }
    s -= popcount(mask)
    val sorted = words.sortBy(_.length)
    var ans = 0
    for (w <- sorted) {
      s -= w.length / 2 * 2
      if (s < 0) return ans
      ans += 1
    }
    ans
  }
}
