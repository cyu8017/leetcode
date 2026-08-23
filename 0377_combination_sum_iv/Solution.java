// LeetCode 0377 - Combination Sum IV

// https://leetcode.com/problems/combination-sum-iv/



class Solution {

    public int combinationSum4(int[] nums, int target) {

        int[] dp = new int[target + 1];

        dp[0] = 1;



        for (int amount = 1; amount <= target; amount++) {

            for (int num : nums) {

                if (amount >= num) {

                    dp[amount] += dp[amount - num];

                }

            }

        }



        return dp[target];

    }

}
