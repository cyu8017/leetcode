// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize_cyclic_partition_score/

export function maximumScore(nums: any, k: any): any {
    const n = nums.length;
    const a = nums.concat(nums);
    if (k > n) k = n;
    let best = 0;
    const NEG = Number.MIN_SAFE_INTEGER;
    for (let start = 0; start < n; start++) {
        const seg = a.slice(start, start + n);
        const dp = Array.from({length: n + 1}, () => new Array(k + 1).fill(NEG));
        dp[0][0] = 0;
        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= k && j <= i; j++) {
                let mx = NEG;
                for (let t = i; t >= j; t--) {
                    if (seg[t - 1] > mx) mx = seg[t - 1];
                    if (dp[t - 1][j - 1] > NEG) {
                        const cand = dp[t - 1][j - 1] + mx;
                        if (cand > dp[i][j]) dp[i][j] = cand;
                    }
                }
            }
        }
        if (dp[n][k] > best) best = dp[n][k];
    }
    return best;
}
