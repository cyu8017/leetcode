// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

object Solution {
  private val MX = 500000
  private val S: java.util.List[Integer] = {
    val list = new java.util.ArrayList[Integer]()
    val isPrime = Array.fill(MX + 1)(true)
    isPrime(0) = false
    isPrime(1) = false
    val primes = new java.util.ArrayList[Integer]()
    var i = 2
    while (i <= MX) {
      if (isPrime(i)) {
        primes.add(i)
        if (i.toLong * i <= MX) {
          var j = i * i
          while (j <= MX) {
            isPrime(j) = false
            j += i
          }
        }
      }
      i += 1
    }
    list.add(0)
    var t = 0
    val it = primes.iterator()
    var stop = false
    while (it.hasNext && !stop) {
      val x = it.next()
      t += x
      if (t > MX) stop = true
      else if (isPrime(t)) list.add(t)
    }
    list
  }

  def largestPrime(n: Int): Int = {
    var lo = 0
    var hi = S.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (S.get(mid) <= n) lo = mid + 1
      else hi = mid
    }
    S.get(lo - 1)
  }
}
