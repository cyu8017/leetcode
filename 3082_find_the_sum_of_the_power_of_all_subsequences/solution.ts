// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

export function sumOfPower(nums: number[], k: number): number {
    const MOD = 1000000007;
    const n = nums.length;
    const f = Array.from({ length: n + 1 }, () => new Array(k + 1).fill(0));
    f[0][0] = 1;
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j <= k; j++) {
            f[i][j] = (f[i - 1][j] * 2) % MOD;
            if (j >= nums[i - 1])
                f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % MOD;
        }
    }
    return f[n][k];
}
