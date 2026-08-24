// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

object Solution {
  def closestPrimes(left: Int, right: Int): Array[Int] = {
    val isPrime = Array.fill(right + 1)(true)
    if (right >= 0) isPrime(0) = false
    if (right >= 1) isPrime(1) = false
    var i = 2
    while (i.toLong * i <= right) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= right) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }
    val primes = scala.collection.mutable.ArrayBuffer.empty[Int]
    var p = left
    while (p <= right) {
      if (isPrime(p)) primes += p
      p += 1
    }
    if (primes.size < 2) return Array(-1, -1)
    var bestDiff = Int.MaxValue
    var best = Array(-1, -1)
    var idx = 0
    while (idx + 1 < primes.size) {
      val d = primes(idx + 1) - primes(idx)
      if (d < bestDiff) {
        bestDiff = d
        best = Array(primes(idx), primes(idx + 1))
      }
      idx += 1
    }
    best
  }
}
