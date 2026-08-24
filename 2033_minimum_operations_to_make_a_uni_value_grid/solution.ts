// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

export function minOperations(grid: number[][], x: number): number {
    const vals = [];
    const bas = grid[0][0] % x;
    for (const row of grid) for (const v of row) {
        if (v % x !== bas) return -1;
        vals.push(v);
    }
    vals.sort((a, b) => a - b);
    const median = vals[Math.floor(vals.length / 2)];
    let ans = 0;
    for (const v of vals) ans += Math.abs(v - median) / x;
    return ans;
}
