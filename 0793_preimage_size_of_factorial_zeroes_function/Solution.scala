// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

object Solution {
  def preimageSizeFZF(k: Int): Int = {
    def zeros(n0: Long): Long = {
      var n = n0
      var z = 0L
      while (n > 0) {
        n /= 5
        z += n
      }
      z
    }
    def firstGe(target: Long): Long = {
      var lo = 0L
      var hi = 5L * target + 5
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (zeros(mid) >= target) hi = mid
        else lo = mid + 1
      }
      lo
    }
    (firstGe(k.toLong + 1) - firstGe(k.toLong)).toInt
  }
}
