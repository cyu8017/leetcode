// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

object Solution {
  def countPartitions(nums: Array[Int], k: Int): Int = {
    val MOD = 1000000007
    var sum = 0L
    var i = 0
    while (i < nums.length) {
      sum += nums(i)
      i += 1
    }
    if (sum < 2L * k) return 0
    val dp = new Array[Int](k)
    dp(0) = 1
    i = 0
    while (i < nums.length) {
      val x = nums(i)
      var s = k - 1
      while (s >= x) {
        dp(s) = (dp(s) + dp(s - x)) % MOD
        s -= 1
      }
      i += 1
    }
    var bad = 0
    i = 0
    while (i < k) {
      bad = (bad + dp(i)) % MOD
      i += 1
    }
    var total = 1
    i = 0
    while (i < nums.length) {
      total = total * 2 % MOD
      i += 1
    }
    ((total - 2L * bad % MOD + MOD) % MOD).toInt
  }
}
