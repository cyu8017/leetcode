// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

export function maximumJumps(nums: number[], target: number): number {
    const n = nums.length;
    const dp = Array(n).fill(-1);
    dp[0] = 0;
    for (let i = 0; i < n; i++) {
        if (dp[i] < 0) continue;
        for (let j = i + 1; j < n; j++) {
            if (Math.abs(nums[j] - nums[i]) <= target)
                dp[j] = Math.max(dp[j], dp[i] + 1);
        }
    }
    return dp[n - 1];
}
