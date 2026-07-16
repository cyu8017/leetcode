export function combinationSum4(nums: number[], target: number): number {
    const dp = new Array<number>(target + 1).fill(0);
    dp[0] = 1;
    for (let amount = 1; amount <= target; amount += 1) {
        for (const num of nums) {
            if (amount >= num) dp[amount] += dp[amount - num];
        }
    }
    return dp[target];
}
