// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

object Solution {
  def minimizeSet(divisor1: Int, divisor2: Int, uniqueCnt1: Int, uniqueCnt2: Int): Int = {
    def gcd(x: Int, y: Int): Int = {
      var a = x
      var b = y
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    val lcm = divisor1.toLong / gcd(divisor1, divisor2) * divisor2
    def ok(x: Long): Boolean = {
      val a = x - x / divisor1
      val b = x - x / divisor2
      val both = x - x / lcm
      a >= uniqueCnt1 && b >= uniqueCnt2 && both >= uniqueCnt1.toLong + uniqueCnt2
    }
    var lo = 1L
    var hi = 1L << 62
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(mid)) hi = mid else lo = mid + 1
    }
    lo.toInt
  }
}
