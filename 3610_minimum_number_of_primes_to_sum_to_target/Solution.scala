// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

object Solution {
  val primes = new java.util.ArrayList[Integer]()

  def ensurePrimes(): Unit = {
    if (primes.size() > 0) return
    var x = 2
    while (primes.size() < 1000) {
      var isPrime = true
      val it = primes.iterator()
      var done = false
      while (it.hasNext && !done) {
        val p = it.next()
        if (p * p > x) done = true
        else if (x % p == 0) { isPrime = false; done = true }
      }
      if (isPrime) primes.add(x)
      x += 1
    }
  }

  def minNumberOfPrimes(n: Int, m: Int): Int = {
    ensurePrimes()
    val Inf = Integer.MAX_VALUE / 2
    val f = Array.fill(n + 1)(Inf)
    f(0) = 0
    var pi = 0
    while (pi < m) {
      val x = primes.get(pi)
      var i = x
      while (i <= n) {
        if (f(i - x) + 1 < f(i)) f(i) = f(i - x) + 1
        i += 1
      }
      pi += 1
    }
    if (f(n) < Inf) f(n) else -1
  }
}
