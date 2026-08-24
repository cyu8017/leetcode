// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

object Solution {
  def platesBetweenCandles(s: String, queries: Array[Array[Int]]): Array[Int] = {
    val n = s.length
    val pref = Array.ofDim[Int](n + 1)
    val left = Array.ofDim[Int](n)
    val right = Array.ofDim[Int](n)
    var last = -1
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + (if (s.charAt(i) == '*') 1 else 0)
      if (s.charAt(i) == '|') last = i
      left(i) = last
      i += 1
    }
    last = -1
    i = n - 1
    while (i >= 0) {
      if (s.charAt(i) == '|') last = i
      right(i) = last
      i -= 1
    }
    val ans = Array.ofDim[Int](queries.length)
    i = 0
    while (i < queries.length) {
      val l = right(queries(i)(0))
      val r = left(queries(i)(1))
      if (l != -1 && r != -1 && l < r) ans(i) = pref(r) - pref(l)
      i += 1
    }
    ans
  }
}
