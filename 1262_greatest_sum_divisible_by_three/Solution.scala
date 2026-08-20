// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

object Solution {
  def maxSumDivThree(nums: Array[Int]): Int = {
    val impossible = Long.MinValue / 4
    var dp = Array(0L, impossible, impossible)
    for (value <- nums) {
      val old = dp.clone()
      for (total <- old if total != impossible) {
        val rem = ((total + value) % 3).toInt
        dp(rem) = math.max(dp(rem), total + value)
      }
    }
    dp(0).toInt
  }
}
