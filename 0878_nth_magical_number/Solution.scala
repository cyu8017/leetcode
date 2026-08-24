// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

object Solution {
  def nthMagicalNumber(n: Int, a: Int, b: Int): Int = {
    val MOD = 1000000007
    def gcd(x0: Long, y0: Long): Long = {
      var x = x0
      var y = y0
      while (y != 0) {
        val t = x % y
        x = y
        y = t
      }
      x
    }
    val lcm = a.toLong / gcd(a.toLong, b.toLong) * b
    var lo = 1L
    var hi = n.toLong * math.min(a, b)
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (mid / a + mid / b - mid / lcm >= n) hi = mid
      else lo = mid + 1
    }
    (lo % MOD).toInt
  }
}
