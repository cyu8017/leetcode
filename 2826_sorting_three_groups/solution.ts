// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

export function minimumOperations(nums: number[]): number {
    const n = nums.length;
    const INF = 1e9;
    const dp = Array.from({length: n + 1}, () => Array(4).fill(INF));
    dp[0][1] = dp[0][2] = dp[0][3] = 0;
    for (let i = 1; i <= n; i++) {
        const v = nums[i - 1];
        for (let g = 1; g <= 3; g++) {
            const cost = v !== g ? 1 : 0;
            for (let prev = 1; prev <= g; prev++)
                dp[i][g] = Math.min(dp[i][g], dp[i - 1][prev] + cost);
        }
    }
    return Math.min(dp[n][1], dp[n][2], dp[n][3]);
}
