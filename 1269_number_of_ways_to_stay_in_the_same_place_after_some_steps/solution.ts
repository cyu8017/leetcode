// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

function numWays(steps: number, arrLen: number): number {
    const mod = 1_000_000_007;
    const width = Math.min(arrLen, Math.floor(steps / 2) + 1);
    let dp = new Array(width).fill(0);
    dp[0] = 1;
    for (let s = 0; s < steps; s++) {
        const next = new Array(width).fill(0);
        for (let i = 0; i < width; i++) {
            next[i] = dp[i];
            if (i > 0) next[i] = (next[i] + dp[i - 1]) % mod;
            if (i + 1 < width) next[i] = (next[i] + dp[i + 1]) % mod;
        }
        dp = next;
    }
    return dp[0];
}
