// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

object Solution {
  private def bitsOnes(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x > 0) { c += x & 1; x >>= 1 }
    c
  }

  def findMinimumTime(strength: Array[Int]): Int = {
    val n = strength.length
    val N = 1 << n
    val inf = 1000000000000000000L
    val dp = Array.fill(N)(inf)
    dp(0) = 0
    val k = 1
    var mask = 0
    while (mask < N) {
      if (dp(mask) != inf) {
        val opened = bitsOnes(mask)
        val x = 1 + opened * k
        var i = 0
        while (i < n) {
          if ((mask & (1 << i)) == 0) {
            val t = (strength(i) + x - 1) / x
            val nmask = mask | (1 << i)
            if (dp(mask) + t < dp(nmask)) dp(nmask) = dp(mask) + t
          }
          i += 1
        }
      }
      mask += 1
    }
    dp(N - 1).toInt
  }
}
