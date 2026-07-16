// LeetCode 0377 - Combination Sum IV

// https://leetcode.com/problems/combination-sum-iv/



class Solution {

    fun combinationSum4(nums: IntArray, target: Int): Int {

        val dp = IntArray(target + 1)

        dp[0] = 1



        for (amount in 1..target) {

            for (num in nums) {

                if (amount >= num) {

                    dp[amount] += dp[amount - num]

                }

            }

        }



        return dp[target]

    }

}
