// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

object Solution {
  def numPrimeArrangements(n: Int): Int = {
    val MOD = 1000000007L
    def isPrime(x: Int): Boolean = {
      if (x < 2) return false
      var d = 2
      while (d * d <= x) {
        if (x % d == 0) return false
        d += 1
      }
      true
    }
    def fact(x: Int): Long = {
      var res = 1L
      for (i <- 2 to x) res = res * i % MOD
      res
    }
    val primes = (1 to n).count(isPrime)
    ((fact(primes) * fact(n - primes)) % MOD).toInt
  }
}
