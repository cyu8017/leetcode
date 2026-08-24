// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

object Solution {
  val MOD = 1000000007

  def qpow(x0: Long, n0: Int): Long = {
    var x = x0
    var n = n0
    var res = 1L
    while (n > 0) {
      if ((n & 1) != 0) res = res * x % MOD
      x = x * x % MOD
      n >>= 1
    }
    res
  }

  def queryConversions(conversions: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val n = conversions.length + 1
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- conversions) g(e(0)).add(Array(e(1), e(2)))
    val res = new Array[Int](n)
    def dfs(s: Int, mul: Int): Unit = {
      res(s) = mul
      val it = g(s).iterator()
      while (it.hasNext) {
        val e = it.next()
        dfs(e(0), ((1L * mul * e(1)) % MOD).toInt)
      }
    }
    dfs(0, 1)
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      ans(i) = ((1L * res(queries(i)(1)) * qpow(res(queries(i)(0)), MOD - 2)) % MOD).toInt
      i += 1
    }
    ans
  }
}
