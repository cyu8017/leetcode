// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }
  private def lcm(a: Int, b: Int): Int = a / gcd(a, b) * b

  def minimumIncrements(nums: Array[Int], target: Array[Int]): Int = {
    val m = target.length
    val N = 1 << m
    val inf = 1e18.toLong
    var dp = Array.fill(N)(inf)
    dp(0) = 0
    nums.foreach { x =>
      val ndp = dp.clone()
      var mask = 0
      while (mask < N) {
        var sub = 1
        while (sub < N) {
          var L = 1
          var ok = true
          var i = 0
          while (i < m && ok) {
            if ((sub & (1 << i)) != 0) {
              L = lcm(L, target(i))
              if (L > 1000000000) ok = false
            }
            i += 1
          }
          if (ok) {
            val cost = (L - x % L) % L
            val nmask = mask | sub
            if (dp(mask) + cost < ndp(nmask)) ndp(nmask) = dp(mask) + cost
          }
          sub += 1
        }
        mask += 1
      }
      dp = ndp
    }
    dp(N - 1).toInt
  }
}
