// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

object Solution {
  def kthPalindrome(queries: Array[Int], intLength: Int): Array[Long] = {
    val half = (intLength + 1) / 2
    var start = 1
    var i = 1
    while (i < half) {
      start *= 10
      i += 1
    }
    val total = start * 9
    val ans = new Array[Long](queries.length)
    i = 0
    while (i < queries.length) {
      val q = queries(i)
      if (q > total) ans(i) = -1L
      else {
        val left = start + q - 1
        var pal = left.toLong
        var x = left
        if (intLength % 2 != 0) x /= 10
        while (x > 0) {
          pal = pal * 10 + x % 10
          x /= 10
        }
        ans(i) = pal
      }
      i += 1
    }
    ans
  }
}
