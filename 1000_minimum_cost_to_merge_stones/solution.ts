// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

function mergeStones(stones: number[], k: number): number {
    const n = stones.length;
    if ((n - 1) % (k - 1) !== 0) return -1;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + stones[i];
    const dp = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let length = k; length <= n; length++) {
        for (let i = 0; i + length - 1 < n; i++) {
            const j = i + length - 1;
            let best = Infinity;
            for (let m = i; m < j; m += k - 1) {
                best = Math.min(best, dp[i][m] + dp[m + 1][j]);
            }
            dp[i][j] = best;
            if ((length - 1) % (k - 1) === 0) {
                dp[i][j] += prefix[j + 1] - prefix[i];
            }
        }
    }
    return dp[0][n - 1];
}
