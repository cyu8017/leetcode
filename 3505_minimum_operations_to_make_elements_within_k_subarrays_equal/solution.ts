// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

export function minOperations(nums: any, x: any, k: any): any {
    const n = nums.length;
    const minOps = new Array(n - x + 1);
    for (let i = 0; i + x <= n; i++) {
        const w = nums.slice(i, i + x).sort((a, b) => a - b);
        const med = w[Math.floor((x - 1) / 2)];
        let ops = 0;
        for (const v of w) ops += Math.abs(v - med);
        minOps[i] = ops;
    }
    const Inf = Number.MAX_SAFE_INTEGER;
    const dp = Array.from({length: n + 1}, () => new Array(k + 1).fill(Inf));
    dp[n][0] = 0;
    for (let i = n - 1; i >= 0; i--) {
        for (let j = 0; j <= k; j++) {
            dp[i][j] = dp[i + 1][j];
            if (j > 0 && i + x <= n && minOps[i] + dp[i + x][j - 1] < dp[i][j])
                dp[i][j] = minOps[i] + dp[i + x][j - 1];
        }
    }
    return dp[0][k];
}
