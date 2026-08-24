// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

object Solution {
  private val MOD = 1000000007

  private def modPow(a0: Long, b0: Int): Int = {
    var a = a0
    var b = b0
    var res = 1L
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res.toInt
  }

  def numberOfSequence(n: Int, sick: Array[Int]): Int = {
    val fact = Array.ofDim[Int](n + 1)
    val invFact = Array.ofDim[Int](n + 1)
    fact(0) = 1
    var i = 1
    while (i <= n) { fact(i) = ((1L * fact(i - 1) * i) % MOD).toInt; i += 1 }
    invFact(n) = modPow(fact(n).toLong, MOD - 2)
    i = n
    while (i > 0) { invFact(i - 1) = ((1L * invFact(i) * i) % MOD).toInt; i -= 1 }
    val m = sick.length
    val totalEmpty = n - m
    var ans = fact(totalEmpty).toLong
    var prev = -1
    for (s <- sick) {
      val gap = s - prev - 1
      if (prev == -1) ans = ans * invFact(gap) % MOD
      else if (gap > 0) ans = ans * invFact(gap) % MOD * modPow(2, gap - 1) % MOD
      prev = s
    }
    val gap2 = n - prev - 1
    ans = ans * invFact(gap2) % MOD
    ans.toInt
  }
}
