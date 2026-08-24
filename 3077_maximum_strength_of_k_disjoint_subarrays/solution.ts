// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

export function maximumStrength(nums: number[], k: number): number {
    const n = nums.length;
    const INF = Number.MIN_SAFE_INTEGER / 2;
    const f = Array.from({ length: n + 1 }, () =>
        Array.from({ length: k + 1 }, () => [INF, INF]));
    f[0][0][0] = 0;
    for (let i = 1; i <= n; i++) {
        const x = nums[i - 1];
        for (let j = 0; j <= k; j++) {
            const sign = (j & 1) !== 0 ? 1 : -1;
            const val = sign * x * (k - j + 1);
            f[i][j][0] = Math.max(f[i - 1][j][0], f[i - 1][j][1]);
            f[i][j][1] = Math.max(f[i][j][1], f[i - 1][j][1] + val);
            if (j > 0) {
                const t = Math.max(f[i - 1][j - 1][0], f[i - 1][j - 1][1]) + val;
                f[i][j][1] = Math.max(f[i][j][1], t);
            }
        }
    }
    return Math.max(f[n][k][0], f[n][k][1]);
}
