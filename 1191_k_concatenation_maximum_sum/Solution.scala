// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

object Solution {
  def kConcatenationMaxSum(arr: Array[Int], k: Int): Int = {
    val MOD = 1000000007
    def kadane(nums: Array[Int]): Long = {
      var best = 0L
      var cur = 0L
      for (x <- nums) {
        cur = math.max(0L, cur + x)
        best = math.max(best, cur)
      }
      best
    }
    val one = kadane(arr)
    if (k == 1) return (one % MOD).toInt
    val two = kadane(arr ++ arr)
    val total = arr.map(_.toLong).sum
    val ans = if (total > 0) math.max(one, two + total * (k - 2)) else math.max(one, two)
    (ans % MOD).toInt
  }
}
