// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

export class Solution {
    findTargetSumWays(nums: number[], target: number): number {
        const total = nums.reduce((sum, num) => sum + num, 0);
        if ((total + target) % 2 || Math.abs(target) > total) return 0;
        const need = (total + target) / 2;
        const dp = Array<number>(need + 1).fill(0);
        dp[0] = 1;
        for (const num of nums) {
            for (let amount = need; amount >= num; amount -= 1) {
                dp[amount] += dp[amount - num];
            }
        }
        return dp[need];
    }
}
