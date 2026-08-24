// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    if (a == 0) return b
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def subsequencePairCount(nums: Array[Int]): Int = {
    val mod = 1000000007
    var maxV = 0
    for (x <- nums) if (x > maxV) maxV = x
    var dp = Array.ofDim[Int](maxV + 1, maxV + 1)
    dp(0)(0) = 1
    for (x <- nums) {
      val ndp = Array.ofDim[Int](maxV + 1, maxV + 1)
      var a = 0
      while (a <= maxV) {
        Array.copy(dp(a), 0, ndp(a), 0, maxV + 1)
        a += 1
      }
      a = 0
      while (a <= maxV) {
        var b = 0
        while (b <= maxV) {
          if (dp(a)(b) != 0) {
            val na = if (a == 0) x else gcd(a, x)
            val nb = if (b == 0) x else gcd(b, x)
            ndp(na)(b) = (ndp(na)(b) + dp(a)(b)) % mod
            ndp(a)(nb) = (ndp(a)(nb) + dp(a)(b)) % mod
          }
          b += 1
        }
        a += 1
      }
      dp = ndp
    }
    var ans = 0
    var g = 1
    while (g <= maxV) {
      ans = (ans + dp(g)(g)) % mod
      g += 1
    }
    ans
  }
}
