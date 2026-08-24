// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

export function minRemovals(nums: any, target: any): any {
    let mx = 0;
    for (const x of nums) mx = Math.max(mx, x);
    let m = 0;
    if (mx > 0) {
        let u = mx;
        while (u !== 0) { m++; u >>= 1; }
    }
    if ((1 << m) <= target) return -1;
    const n = nums.length;
    const N = 1 << m;
    const NEG = -Infinity;
    const f = Array.from({length: n + 1}, () => new Array(N).fill(NEG));
    f[0][0] = 0;
    for (let i = 1; i <= n; i++) {
        const x = nums[i - 1];
        for (let j = 0; j < N; j++) {
            f[i][j] = f[i - 1][j];
            if (f[i - 1][j ^ x] !== NEG) {
                f[i][j] = Math.max(f[i][j], f[i - 1][j ^ x] + 1);
            }
        }
    }
    if (f[n][target] < 0) return -1;
    return n - f[n][target];
}
