// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

object Solution {
  def minCostToEqualizeArray(nums: Array[Int], cost1: Int, cost2: Int): Int = {
    val MOD = 1000000007
    val n = nums.length
    var minNum = nums(0)
    var maxNum = nums(0)
    var sum = 0L
    nums.foreach { v =>
      minNum = math.min(minNum, v)
      maxNum = math.max(maxNum, v)
      sum += v
    }
    if (cost1 * 2L <= cost2 || n < 3) {
      val totalGap = maxNum.toLong * n - sum
      return ((cost1.toLong * totalGap) % MOD).toInt
    }
    var ans = Long.MaxValue
    var target = maxNum
    while (target < 2 * maxNum) {
      val maxGap = target - minNum
      val totalGap = target.toLong * n - sum
      var pairs = totalGap / 2
      val alt = totalGap - maxGap
      if (alt < pairs) pairs = alt
      val cost = cost1.toLong * (totalGap - 2 * pairs) + cost2.toLong * pairs
      ans = math.min(ans, cost)
      target += 1
    }
    (ans % MOD).toInt
  }
}
