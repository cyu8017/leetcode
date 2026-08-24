// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

export function longestSubsequence(nums: any): any {
    const n = nums.length;
    let ans = 1;
    const dp = Array.from({ length: n }, () => new Array(301).fill(0));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            const d = Math.abs(nums[i] - nums[j]);
            let best = 1;
            for (let pd = d; pd <= 300; pd++) {
                if (dp[j][pd] > best) best = dp[j][pd];
            }
            if (best + 1 > dp[i][d]) dp[i][d] = best + 1;
            if (dp[i][d] > ans) ans = dp[i][d];
        }
        if (dp[i][0] < 1) dp[i][0] = 1;
    }
    return ans;
}
