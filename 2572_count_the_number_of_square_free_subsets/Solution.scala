// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

object Solution {
  private val MOD = 1000000007
  private val PRIMES = Array(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)

  def squareFreeSubsets(nums: Array[Int]): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach(x => freq(x) = freq.getOrElse(x, 0) + 1)
    val dp = Array.fill(1 << 10)(0)
    dp(0) = 1
    freq.foreach { case (x, c) =>
      if (x != 1) {
        val m = maskOf(x)
        if (m >= 0) {
          var state = (1 << 10) - 1
          while (state >= 0) {
            if ((state & m) == 0) {
              dp(state | m) = ((dp(state | m) + dp(state).toLong * c) % MOD).toInt
            }
            state -= 1
          }
        }
      }
    }
    var ans = 0
    dp.foreach(v => ans = (ans + v) % MOD)
    val ones = freq.getOrElse(1, 0)
    var mul = 1
    var i = 0
    while (i < ones) {
      mul = mul * 2 % MOD
      i += 1
    }
    ans = ((ans.toLong * mul) % MOD).toInt
    ans = (ans - 1 + MOD) % MOD
    ans
  }

  private def maskOf(x0: Int): Int = {
    var x = x0
    var mask = 0
    var i = 0
    while (i < PRIMES.length) {
      val p = PRIMES(i)
      var cnt = 0
      while (x % p == 0) {
        x /= p
        cnt += 1
        if (cnt > 1) return -1
      }
      if (cnt == 1) mask |= 1 << i
      i += 1
    }
    mask
  }
}
