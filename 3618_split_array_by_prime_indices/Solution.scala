// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

object Solution {
  private val M = 100010
  private var primesCache: Array[Boolean] = null

  private def primes(): Array[Boolean] = {
    if (primesCache == null) {
      primesCache = Array.fill(M)(true)
      primesCache(0) = false
      primesCache(1) = false
      var i = 2
      while (i < M) {
        if (primesCache(i)) {
          var j = i + i
          while (j < M) {
            primesCache(j) = false
            j += i
          }
        }
        i += 1
      }
    }
    primesCache
  }

  def splitArray(nums: Array[Int]): Long = {
    val pr = primes()
    var ans = 0L
    var i = 0
    while (i < nums.length) {
      if (pr(i)) ans += nums(i)
      else ans -= nums(i)
      i += 1
    }
    math.abs(ans)
  }
}
