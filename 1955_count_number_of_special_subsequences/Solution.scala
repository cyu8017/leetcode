// LeetCode 1955 - Count Number of Special Subsequences
// https://leetcode.com/problems/count-number-of-special-subsequences/

object Solution {
  def countSpecialSubsequences(nums: Array[Int]): Int = {
    val MOD = 1000000007
    var a = 0
    var b = 0
    var c = 0
    for (x <- nums) {
      if (x == 0) a = (a * 2 + 1) % MOD
      else if (x == 1) b = ((b * 2L + a) % MOD).toInt
      else c = ((c * 2L + b) % MOD).toInt
    }
    c
  }
}
