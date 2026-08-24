// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

object Solution {
  def findKthSmallest(coins: Array[Int], k: Int): Long = {
    val r = 100000000000L
    val n = coins.length
    var lo = 1L
    var hi = r
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (check(coins, n, mid, k)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def gcdll(a0: Long, b0: Long): Long = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  private def lcmll(a: Long, b: Long): Long = a / gcdll(a, b) * b

  private def bitCount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) {
      c += x & 1
      x >>= 1
    }
    c
  }

  private def check(coins: Array[Int], n: Int, mx: Long, k: Int): Boolean = {
    var cnt = 0L
    var i = 1
    while (i < (1 << n)) {
      var v = 1L
      var j = 0
      while (j < n) {
        if (((i >> j) & 1) != 0) {
          v = lcmll(v, coins(j))
          if (v > mx) j = n
        }
        j += 1
      }
      val m = bitCount(i)
      if (m % 2 == 1) cnt += mx / v
      else cnt -= mx / v
      i += 1
    }
    cnt >= k
  }
}
