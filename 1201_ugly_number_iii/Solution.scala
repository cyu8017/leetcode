// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

object Solution {
  def nthUglyNumber(n: Int, a: Int, b: Int, c: Int): Int = {
    def gcd(x: Long, y: Long): Long = if (y == 0) x else gcd(y, x % y)
    def lcm(x: Long, y: Long): Long = x / gcd(x, y) * y
    val aa = a.toLong
    val bb = b.toLong
    val cc = c.toLong
    val ab = lcm(aa, bb)
    val ac = lcm(aa, cc)
    val bc = lcm(bb, cc)
    val abc = lcm(ab, cc)
    def count(x: Long): Long =
      x / aa + x / bb + x / cc - x / ab - x / ac - x / bc + x / abc
    var lo = 1L
    var hi = 2000000000L
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (count(mid) >= n) hi = mid else lo = mid + 1
    }
    lo.toInt
  }
}
