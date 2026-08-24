// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

export function cherryPickup(grid: number[][]): number {
    const n = grid.length;
    const memo = Array.from({length: n}, () =>
        Array.from({length: n}, () => new Array(n).fill(-Infinity))
    );
    const dp = (r1, c1, c2) => {
        const r2 = r1 + c1 - c2;
        if (r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid[r1][c1] === -1 || grid[r2][c2] === -1)
            return -1000000000;
        if (r1 === n - 1 && c1 === n - 1) return grid[r1][c1];
        if (memo[r1][c1][c2] !== -Infinity) return memo[r1][c1][c2];
        let cherries = grid[r1][c1];
        if (r1 !== r2 || c1 !== c2) cherries += grid[r2][c2];
        cherries += Math.max(
            Math.max(dp(r1 + 1, c1, c2), dp(r1, c1 + 1, c2)),
            Math.max(dp(r1 + 1, c1, c2 + 1), dp(r1, c1 + 1, c2 + 1))
        );
        memo[r1][c1][c2] = cherries;
        return cherries;
    };
    return Math.max(0, dp(0, 0, 0));
}
