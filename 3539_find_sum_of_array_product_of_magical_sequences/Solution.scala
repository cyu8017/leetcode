// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

object Solution {
  val N = 31
  val MOD = 1000000007
  val f = new Array[Long](N)
  val g = new Array[Long](N)
  var inited = false

  def qpow(a0: Long, k0: Long): Long = {
    var a = a0
    var k = k0
    var res = 1L
    while (k > 0) {
      if ((k & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      k >>= 1
    }
    res
  }

  def initFact(): Unit = {
    if (inited) return
    f(0) = 1
    g(0) = 1
    var i = 1
    while (i < N) {
      f(i) = f(i - 1) * i % MOD
      g(i) = qpow(f(i), MOD - 2)
      i += 1
    }
    inited = true
  }

  def comb(m: Int, nn: Int): Long = {
    if (nn < 0 || nn > m) return 0
    f(m) * g(nn) % MOD * g(m - nn) % MOD
  }

  def magicalSum(m: Int, k: Int, nums: Array[Int]): Int = {
    initFact()
    val n = nums.length
    val dp = Array.fill(n + 1, m + 1, k + 1, N)(-1L)

    def dfs(i: Int, j: Int, kk: Int, st: Int): Long = {
      if (kk < 0 || (i == n && j > 0)) return 0
      if (i == n) {
        var k2 = kk
        var st2 = st
        while (st2 > 0) { k2 -= st2 & 1; st2 >>= 1 }
        return if (k2 == 0) 1 else 0
      }
      if (dp(i)(j)(kk)(st) != -1) return dp(i)(j)(kk)(st)
      var res = 0L
      var t = 0
      while (t <= j) {
        val nt = t + st
        val nk = kk - (nt & 1)
        val p = qpow(nums(i), t)
        val tmp = comb(j, t) * p % MOD * dfs(i + 1, j - t, nk, nt >> 1) % MOD
        res = (res + tmp) % MOD
        t += 1
      }
      dp(i)(j)(kk)(st) = res
      res
    }

    dfs(0, m, k, 0).toInt
  }
}
