// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

public class Solution {
    public int FindTargetSumWays(int[] nums, int target) {
        int total = 0;
        foreach (int num in nums) {
            total += num;
        }
        if ((total + target) % 2 != 0 || Math.Abs(target) > total) {
            return 0;
        }
        int need = (total + target) / 2;
        int[] dp = new int[need + 1];
        dp[0] = 1;
        foreach (int num in nums) {
            for (int amount = need; amount >= num; amount--) {
                dp[amount] += dp[amount - num];
            }
        }
        return dp[need];
    }
}
