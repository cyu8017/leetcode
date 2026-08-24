// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum_score_using_exactly_k_pairs/

export function maxScore(nums1: any, nums2: any, K: any): any {
    const n = nums1.length, m = nums2.length;
    const NEG = Number.MIN_SAFE_INTEGER / 4;
    const f = Array.from({length: n + 1}, () =>
        Array.from({length: m + 1}, () => new Array(K + 1).fill(NEG)));
    f[0][0][0] = 0;
    for (let i = 0; i <= n; i++) {
        for (let j = 0; j <= m; j++) {
            for (let k = 0; k <= K; k++) {
                if (i > 0) f[i][j][k] = Math.max(f[i][j][k], f[i - 1][j][k]);
                if (j > 0) f[i][j][k] = Math.max(f[i][j][k], f[i][j - 1][k]);
                if (i > 0 && j > 0 && k > 0) {
                    f[i][j][k] = Math.max(f[i][j][k], f[i - 1][j - 1][k - 1] + nums1[i - 1] * nums2[j - 1]);
                }
            }
        }
    }
    return f[n][m][K];
}
