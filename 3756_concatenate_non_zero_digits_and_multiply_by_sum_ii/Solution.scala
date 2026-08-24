// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum II
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

object Solution {
  private val MX = 100001
  private val MOD = 1000000007L
  private val PW: Array[Long] = {
    val arr = new Array[Long](MX)
    arr(0) = 1
    var i = 1
    while (i < MX) {
      arr(i) = arr(i - 1) * 10 % MOD
      i += 1
    }
    arr
  }

  def sumAndMultiply(s: String, queries: Array[Array[Int]]): Array[Int] = {
    val n = s.length
    val sumD = new Array[Int](n + 1)
    val cntN0 = new Array[Int](n + 1)
    val p = new Array[Long](n + 1)
    var i = 1
    while (i <= n) {
      val d = (s.charAt(i - 1) - '0').toLong
      sumD(i) = sumD(i - 1) + d.toInt
      cntN0(i) = cntN0(i - 1)
      if (d > 0) {
        cntN0(i) += 1
        p(i) = (p(i - 1) * 10 + d) % MOD
      } else p(i) = p(i - 1)
      i += 1
    }
    val ans = new Array[Int](queries.length)
    i = 0
    while (i < queries.length) {
      val l = queries(i)(0)
      val r = queries(i)(1)
      val n0 = cntN0(r + 1) - cntN0(l)
      val sd = (sumD(r + 1) - sumD(l)).toLong
      val x = (p(r + 1) - p(l) * PW(n0) % MOD + MOD) % MOD
      ans(i) = (x * sd % MOD).toInt
      i += 1
    }
    ans
  }
}
