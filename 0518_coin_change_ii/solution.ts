// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

export class Solution {
    change(amount: number, coins: number[]): number {
        const dp = Array<number>(amount + 1).fill(0);
        dp[0] = 1;
        for (const coin of coins) {
            for (let value = coin; value <= amount; value += 1) {
                dp[value] += dp[value - coin];
            }
        }
        return dp[amount];
    }
}
