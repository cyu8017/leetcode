// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

export function validSubarraySplit(nums: number[]): number {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const n = nums.length;
    const INF = 1 << 30;
    const dp = Array(n + 1).fill(INF);
    dp[0] = 0;
    for (let i = 0; i < n; i++) {
        if (dp[i] >= INF) continue;
        for (let j = i; j < n; j++) {
            if (gcd(nums[i], nums[j]) > 1) {
                if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
            }
        }
    }
    return dp[n] >= INF ? -1 : dp[n];
}
