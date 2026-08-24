// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

object Solution {
  def primeSubarray(nums: Array[Int], k: Int): Int = {
    var mx = 0
    for (v <- nums) mx = math.max(mx, v)
    val isPrime = new Array[Boolean](mx + 1)
    var i = 2
    while (i <= mx) { isPrime(i) = true; i += 1 }
    i = 2
    while (i * i <= mx) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= mx) { isPrime(j) = false; j += i }
      }
      i += 1
    }
    val n = nums.length
    var ans = 0
    var l = 0
    while (l < n) {
      val primes = new java.util.ArrayList[Integer]()
      var r = l
      while (r < n) {
        if (isPrime(nums(r))) primes.add(nums(r))
        if (primes.size() >= 2) {
          var mn = primes.get(0)
          var mxp = primes.get(0)
          val it = primes.iterator()
          while (it.hasNext) {
            val p = it.next()
            mn = math.min(mn, p)
            mxp = math.max(mxp, p)
          }
          if (mxp - mn <= k) ans += 1
        }
        r += 1
      }
      l += 1
    }
    ans
  }
}
