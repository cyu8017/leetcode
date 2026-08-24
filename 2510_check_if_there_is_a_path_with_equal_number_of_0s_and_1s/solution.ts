// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

export function isThereAPath(grid: number[][]): boolean {
    const m = grid.length, n = grid[0].length;
    if ((m + n - 1) % 2 !== 0) return false;
    const target = Math.floor((m + n - 1) / 2);
    const memo = new Map();
    const key = (r, c, bal) => (BigInt(r) << 40n) | (BigInt(c) << 20n) | BigInt(bal & 0xfffff);
    const dfs = (r, c, bal) => {
        if (r >= m || c >= n) return false;
        bal += grid[r][c];
        if (bal > target || bal + (m - 1 - r) + (n - 1 - c) < target) return false;
        if (r === m - 1 && c === n - 1) return bal === target;
        const k = key(r, c, bal).toString();
        if (memo.has(k)) return memo.get(k);
        const ok = dfs(r + 1, c, bal) || dfs(r, c + 1, bal);
        memo.set(k, ok);
        return ok;
    };
    return dfs(0, 0, 0);
}
