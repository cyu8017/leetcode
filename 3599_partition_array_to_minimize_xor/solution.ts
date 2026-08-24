// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

export function minXor(nums: any, k: any): any {
    const n = nums.length;
    const g = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) g[i] = g[i - 1] ^ nums[i - 1];
    const Inf = Math.floor(2147483647 / 2);
    const f = Array.from({length: n + 1}, () => new Array(k + 1).fill(Inf));
    f[0][0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= Math.min(i, k); j++) {
            for (let h = j - 1; h < i; h++) {
                f[i][j] = Math.min(f[i][j], Math.max(f[h][j - 1], g[i] ^ g[h]));
            }
        }
    }
    return f[n][k];
}
