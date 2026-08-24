// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

object Solution {
  def sumOfPower(nums: Array[Int], k: Int): Int = {
    val MOD = 1000000007
    val n = nums.length
    val f = Array.ofDim[Int](n + 1, k + 1)
    f(0)(0) = 1
    var i = 1
    while (i <= n) {
      var j = 0
      while (j <= k) {
        f(i)(j) = ((f(i - 1)(j).toLong * 2) % MOD).toInt
        if (j >= nums(i - 1)) f(i)(j) = (f(i)(j) + f(i - 1)(j - nums(i - 1))) % MOD
        j += 1
      }
      i += 1
    }
    f(n)(k)
  }
}
