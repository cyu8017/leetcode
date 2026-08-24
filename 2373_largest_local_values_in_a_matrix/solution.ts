// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

export function largestLocal(grid: number[][]): number[][] {
    const n = grid.length;
    const ans = Array.from({ length: n - 2 }, () => Array(n - 2).fill(0));
    for (let i = 0; i < n - 2; i++) {
        for (let j = 0; j < n - 2; j++) {
            let mx = 0;
            for (let r = i; r < i + 3; r++)
                for (let c = j; c < j + 3; c++)
                    if (grid[r][c] > mx) mx = grid[r][c];
            ans[i][j] = mx;
        }
    }
    return ans;
}
