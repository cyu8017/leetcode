// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

object Solution {
  def numRollsToTarget(n: Int, k: Int, target: Int): Int = {
    val MOD = 1000000007
    var dp = Array.ofDim[Int](target + 1)
    dp(0) = 1
    for (_ <- 0 until n) {
      val neu = Array.ofDim[Int](target + 1)
      for (s <- 0 to target if dp(s) != 0; face <- 1 to k if s + face <= target) {
        neu(s + face) = (neu(s + face) + dp(s)) % MOD
      }
      dp = neu
    }
    dp(target)
  }
}
