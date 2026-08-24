// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

object Solution {
  def f(x0: Int, k: Int): String = {
    var x = x0
    val res = new StringBuilder
    while (x > 0) {
      val v = x % k
      res.append(if (v <= 9) ('0' + v).toChar else ('A' + v - 10).toChar)
      x /= k
    }
    res.reverse.toString
  }

  def concatHex36(n: Int): String = f(n * n, 16) + f(n * n * n, 36)
}
