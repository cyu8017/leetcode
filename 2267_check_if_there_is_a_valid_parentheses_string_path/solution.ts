// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

export function hasValidPath(grid: string[][]): boolean {
    const m = grid.length, n = grid[0].length;
    if ((m + n - 1) % 2 === 1 || grid[0][0] === ')' || grid[m - 1][n - 1] === '(') return false;
    const vis = new Set();
    const dfs = (r, c, bal) => {
        if (r >= m || c >= n) return false;
        bal += (grid[r][c] === '(') ? 1 : -1;
        if (bal < 0) return false;
        if (r === m - 1 && c === n - 1) return bal === 0;
        const k = ((r * n + c) << 10) | bal;
        if (vis.has(k)) return false;
        vis.add(k);
        return dfs(r + 1, c, bal) || dfs(r, c + 1, bal);
    };
    return dfs(0, 0, 0);
}
