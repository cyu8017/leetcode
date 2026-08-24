// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

object Solution {
  private val M = 50
  private val cnt: Array[Long] = new Array[Long](M + 1)
  private val s: Array[Long] = new Array[Long](M + 1)

  {
    var p = 1L
    cnt(0) = 0
    s(0) = 0
    var i = 1
    while (i <= M) {
      cnt(i) = cnt(i - 1) * 2 + p
      s(i) = s(i - 1) * 2 + p * (i - 1)
      p *= 2
      i += 1
    }
  }

  def findProductsOfElements(queries: Array[Array[Long]]): Array[Int] = {
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val left = queries(i)(0)
      val right = queries(i)(1)
      val mod = queries(i)(2)
      val power = f(right + 1) - f(left)
      ans(i) = qpow(2, power, mod).toInt
      i += 1
    }
    ans
  }

  private def numIdxAndSum(x0: Long): Array[Long] = {
    var x = x0
    var idx = 0L
    var totalSum = 0L
    while (x > 0) {
      val i = 63 - java.lang.Long.numberOfLeadingZeros(x)
      idx += cnt(i)
      totalSum += s(i)
      x -= 1L << i
      totalSum += (x + 1) * i
      idx += x + 1
    }
    Array(idx, totalSum)
  }

  private def f(i0: Long): Long = {
    var l = 0L
    var r = 1L << M
    while (l < r) {
      val mid = (l + r + 1) >> 1
      val p = numIdxAndSum(mid)
      if (p(0) < i0) l = mid
      else r = mid - 1
    }
    val p = numIdxAndSum(l)
    var totalSum = p(1)
    var i = i0 - p(0)
    var x = l + 1
    var j = 0L
    while (j < i) {
      val y = x & -x
      totalSum += java.lang.Long.numberOfTrailingZeros(y)
      x -= y
      j += 1
    }
    totalSum
  }

  private def qpow(a0: Long, n0: Long, mod: Long): Long = {
    var ans = 1L % mod
    var a = a0 % mod
    var n = n0
    while (n > 0) {
      if ((n & 1) != 0) ans = ans * a % mod
      a = a * a % mod
      n >>= 1
    }
    ans
  }
}
