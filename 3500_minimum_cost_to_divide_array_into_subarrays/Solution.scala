// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

object Solution {
  def minimumCost(nums: Array[Int], cost: Array[Int], k: Int): Long = {
    val n = nums.length
    val pn = new Array[Long](n + 1)
    val pc = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pn(i + 1) = pn(i) + nums(i)
      pc(i + 1) = pc(i) + cost(i)
      i += 1
    }
    val inf = 1L << 62
    val dp = Array.fill(n + 1)(0L)
    i = 0
    while (i < n) { dp(i) = inf; i += 1 }
    i = n - 1
    while (i >= 0) {
      var j = i
      while (j < n) {
        val cand = pn(j + 1) * (pc(j + 1) - pc(i)) + k.toLong * (pc(n) - pc(i)) + dp(j + 1)
        if (cand < dp(i)) dp(i) = cand
        j += 1
      }
      i -= 1
    }
    dp(0)
  }
}
