// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

object Solution {
  private def modPow(a0: Long, e0: Long, mod: Int): Long = {
    var a = a0 % mod
    var e = e0
    var r = 1L
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r
  }

  private def comb(n: Int, k: Int, mod: Int): Int = {
    if (k < 0 || k > n) return 0
    var num = 1L
    var den = 1L
    var i = 0
    while (i < k) {
      num = num * (n - i) % mod
      den = den * (i + 1) % mod
      i += 1
    }
    (num * modPow(den, mod - 2, mod) % mod).toInt
  }

  def distanceSum(m: Int, n: Int, k: Int): Int = {
    val mod = 1000000007
    if (k < 2) return 0
    val totalCells = m * n
    val pairChoose = comb(totalCells - 2, k - 2, mod)
    var sumDist = 0L
    var d = 1
    while (d < m) {
      sumDist += d.toLong * (m - d) * n * n
      d += 1
    }
    d = 1
    while (d < n) {
      sumDist += d.toLong * (n - d) * m * m
      d += 1
    }
    (sumDist % mod * pairChoose % mod).toInt
  }
}
