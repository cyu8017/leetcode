// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

object Solution {
  private var ready = false
  private var isPrime: Array[Boolean] = _

  private def init(): Unit = {
    if (ready) return
    isPrime = Array.fill(1001)(true)
    isPrime(0) = false
    isPrime(1) = false
    var i = 2
    while (i * i <= 1000) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= 1000) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }
    ready = true
  }

  def sumOfPrimesInRange(n: Int): Int = {
    init()
    var r = 0
    var x = n
    while (x > 0) {
      r = r * 10 + x % 10
      x /= 10
    }
    val low = math.min(n, r)
    val high = math.max(n, r)
    var ans = 0
    var v = low
    while (v <= high) {
      if (isPrime(v)) ans += v
      v += 1
    }
    ans
  }
}
