// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

object Solution {
  private val MX = 200000
  private var isPrime: Array[Boolean] = _
  private var primes: Array[Int] = _
  private var ready = false

  private def init(): Unit = {
    if (ready) return
    isPrime = Array.fill(MX + 1)(true)
    isPrime(0) = false
    isPrime(1) = false
    var i = 2
    while (i <= MX / i) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= MX) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }
    val buf = scala.collection.mutable.ArrayBuffer.empty[Int]
    i = 2
    while (i <= MX) {
      if (isPrime(i)) buf += i
      i += 1
    }
    primes = buf.toArray
    ready = true
  }

  def minOperations(nums: Array[Int]): Int = {
    init()
    var ans = 0
    var i = 0
    while (i < nums.length) {
      val x = nums(i)
      if (i % 2 == 0) {
        var lo = 0
        var hi = primes.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (primes(mid) < x) lo = mid + 1
          else hi = mid
        }
        ans += primes(lo) - x
      } else if (isPrime(x)) {
        ans += (if (x == 2) 2 else 1)
      }
      i += 1
    }
    ans
  }
}
