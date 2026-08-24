// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

object Solution {
  val MIN = -5000

  def maxProduct(nums: Array[Int], k: Int, limit: Int): Int = {
    val memo = scala.collection.mutable.HashMap.empty[String, Int]
    var sumAll = 0
    for (v <- nums) sumAll += v
    if (math.abs(k) > sumAll) return -1

    def dp(i: Int, product: Int, state: Int, kk: Int): Int = {
      if (i == nums.length) {
        if (kk == 0 && state != 0 && product <= limit) return product
        return MIN
      }
      val key = i + "," + product + "," + state + "," + kk
      if (memo.contains(key)) return memo(key)
      var res = dp(i + 1, product, state, kk)
      if (state == 0) res = math.max(res, dp(i + 1, nums(i), 1, kk - nums(i)))
      if (state == 1) {
        var np = product * nums(i)
        if (np > limit + 1) np = limit + 1
        res = math.max(res, dp(i + 1, np, 2, kk + nums(i)))
      }
      if (state == 2) {
        var np = product * nums(i)
        if (np > limit + 1) np = limit + 1
        res = math.max(res, dp(i + 1, np, 1, kk - nums(i)))
      }
      memo(key) = res
      res
    }

    val ans = dp(0, 1, 0, k)
    if (ans == MIN) -1 else ans
  }
}
