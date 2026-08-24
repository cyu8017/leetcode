// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

object Solution {
  def countStableSubsequences(nums: Array[Int]): Int = {
    val MOD = 1000000007
    var a1 = 0
    var a2 = 0
    var b1 = 0
    var b2 = 0
    for (x <- nums) {
      if (x % 2 == 1) {
        val na1 = (1 + b1 + b2) % MOD
        val na2 = a1
        a1 = (a1 + na1) % MOD
        a2 = (a2 + na2) % MOD
      } else {
        val nb1 = (1 + a1 + a2) % MOD
        val nb2 = b1
        b1 = (b1 + nb1) % MOD
        b2 = (b2 + nb2) % MOD
      }
    }
    (((a1 + a2) % MOD + b1) % MOD + b2) % MOD
  }
}
