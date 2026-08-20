// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

function minKnightMoves(x: number, y: number): number {
    x = Math.abs(x); y = Math.abs(y);
    const memo = new Map();
    const dfs = (a, b) => {
        if (a > b) [a, b] = [b, a];
        const key = a + ',' + b;
        if (memo.has(key)) return memo.get(key);
        if (a + b === 0) return 0;
        if (a + b === 2) return 2;
        const ans = Math.min(dfs(Math.abs(a - 1), Math.abs(b - 2)), dfs(Math.abs(a - 2), Math.abs(b - 1))) + 1;
        memo.set(key, ans);
        return ans;
    };
    return dfs(x, y);
}
