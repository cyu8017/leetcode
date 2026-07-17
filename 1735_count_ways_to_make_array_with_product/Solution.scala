// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

object Solution {
  private val Mod = 1000000007L

  def waysToFillArray(queries: Array[Array[Int]]): Array[Int] = {
    queries.map { query =>
      val n = query(0).toLong
      var value = query(1).toLong
      var ways = 1L
      var d = 2L
      while (d * d <= value) {
        if (value % d == 0) {
          var exp = 0L
          while (value % d == 0) {
            value /= d
            exp += 1
          }
          ways = ways * combMod(n + exp - 1, exp) % Mod
        }
        d += (if (d == 2) 1 else 2)
      }
      if (value > 1) {
        ways = ways * (n % Mod) % Mod
      }
      ways.toInt
    }
  }

  private def combMod(a: Long, b: Long): Long = {
    var num = 1L
    var den = 1L
    var i = 1L
    while (i <= b) {
      num = num * ((a - b + i) % Mod) % Mod
      den = den * (i % Mod) % Mod
      i += 1
    }
    num * powMod(den, Mod - 2) % Mod
  }

  private def powMod(base: Long, exp: Long): Long = {
    var result = 1L
    var b = base % Mod
    var e = exp
    while (e > 0) {
      if ((e & 1L) == 1L) {
        result = result * b % Mod
      }
      b = b * b % Mod
      e >>= 1
    }
    result
  }
}
