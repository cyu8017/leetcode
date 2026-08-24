// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

export function maxSum(nums: any, k: any, m: any): any {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    const neg = Number.MIN_SAFE_INTEGER / 4;
    const dp = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(neg));
    for (let i = 0; i <= n; i++) dp[0][i] = 0;
    for (let t = 1; t <= k; t++) {
        let best = neg;
        for (let i = t * m; i <= n; i++) {
            const j = i - m;
            best = Math.max(best, dp[t - 1][j] - pref[j]);
            dp[t][i] = best + pref[i];
        }
        for (let i = 1; i <= n; i++) dp[t][i] = Math.max(dp[t][i], dp[t][i - 1]);
    }
    return dp[k][n];
}
