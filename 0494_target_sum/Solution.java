// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        if ((total + target) % 2 != 0 || Math.abs(target) > total) {
            return 0;
        }
        int need = (total + target) / 2;
        int[] dp = new int[need + 1];
        dp[0] = 1;
        for (int num : nums) {
            for (int amount = need; amount >= num; amount--) {
                dp[amount] += dp[amount - num];
            }
        }
        return dp[need];
    }
}
