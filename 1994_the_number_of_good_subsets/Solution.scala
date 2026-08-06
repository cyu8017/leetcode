// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

object Solution {
  def numberOfGoodSubsets(nums: Array[Int]): Int = {
    val MOD = 1000000007L
    val primes = Array(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    val masks = Array.fill(31)(0)
    for (x <- 2 until 31) {
      var m = 0
      var y = x
      var ok = true
      for (i <- primes.indices if ok) {
        val p = primes(i)
        if (y % p == 0) {
          if ((y / p) % p == 0) ok = false
          else {
            m |= 1 << i
            y /= p
          }
        }
      }
      masks(x) = if (ok) m else -1
    }
    val cnt = Array.ofDim[Int](31)
    for (v <- nums) cnt(v) += 1
    val dp = Array.ofDim[Long](1 << primes.length)
    dp(0) = 1
    for (x <- 2 until 31 if cnt(x) > 0 && masks(x) >= 0) {
      val m = masks(x)
      for (state <- ((1 << primes.length) - 1) to 0 by -1 if (state & m) == 0) {
        dp(state | m) = (dp(state | m) + dp(state) * cnt(x)) % MOD
      }
    }
    var ans = dp.drop(1).sum % MOD
    def modPow(base: Long, exp: Int): Long = {
      var b = base
      var e = exp
      var res = 1L
      while (e > 0) {
        if ((e & 1) == 1) res = res * b % MOD
        b = b * b % MOD
        e >>= 1
      }
      res
    }
    ans = ans * modPow(2, cnt(1)) % MOD
    ans.toInt
  }
}
