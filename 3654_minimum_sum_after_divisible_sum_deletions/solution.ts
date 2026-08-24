// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

export function minArraySum(nums: any, k: any): any {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = (prefix[i] + nums[i]) % k;
    const inf = Number.MAX_SAFE_INTEGER / 2;
    const dp = new Array(n + 1).fill(0);
    const best = new Array(k).fill(inf);
    best[0] = 0;
    for (let i = 1; i <= n; i++) {
        dp[i] = dp[i - 1] + nums[i - 1];
        if (best[prefix[i]] < dp[i]) dp[i] = best[prefix[i]];
        if (dp[i] < best[prefix[i]]) best[prefix[i]] = dp[i];
    }
    return dp[n];
}
