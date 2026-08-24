// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

object Solution {
  def minimumPossibleSum(n: Int, target: Int): Int = {
    val MOD = 1000000007
    val m = target / 2
    if (n <= m) return (1L * n * (n + 1) / 2 % MOD).toInt
    var sum = 1L * m * (m + 1) / 2
    val remain = n - m
    sum += 1L * remain * target + 1L * remain * (remain - 1) / 2
    (sum % MOD).toInt
  }
}
