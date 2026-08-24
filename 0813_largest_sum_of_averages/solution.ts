// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

export function largestSumOfAverages(nums: number[], k: number): number {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
    let dp = new Array(n).fill(0);
    for (let i = 0; i < n; i++) dp[i] = (prefix[i + 1] - prefix[0]) / (i + 1);
    for (let groups = 2; groups <= k; groups++) {
        const nxt = new Array(n).fill(0);
        for (let i = groups - 1; i < n; i++) {
            let best = 0.0;
            for (let j = groups - 2; j < i; j++) {
                best = Math.max(best, dp[j] + (prefix[i + 1] - prefix[j + 1]) / (i - j));
            }
            nxt[i] = best;
        }
        dp = nxt;
    }
    return dp[n - 1];
}
