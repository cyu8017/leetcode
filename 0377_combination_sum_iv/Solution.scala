// LeetCode 0377 - Combination Sum IV

// https://leetcode.com/problems/combination-sum-iv/



object Solution {

  def combinationSum4(nums: Array[Int], target: Int): Int = {

    val dp = Array.fill(target + 1)(0)

    dp(0) = 1



    for (amount <- 1 to target) {

      for (num <- nums) {

        if (amount >= num) {

          dp(amount) += dp(amount - num)

        }

      }

    }



    dp(target)

  }

}
