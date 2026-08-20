// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

function largest1BorderedSquare(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const left = Array.from({ length: m }, () => Array(n).fill(0));
    const up = Array.from({ length: m }, () => Array(n).fill(0));
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c]) {
                left[r][c] = 1 + (c ? left[r][c - 1] : 0);
                up[r][c] = 1 + (r ? up[r - 1][c] : 0);
            }
        }
    }
    let best = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (!grid[r][c]) continue;
            const limit = Math.min(left[r][c], up[r][c]);
            for (let size = limit; size >= 1; size--) {
                if (left[r - size + 1][c] >= size && up[r][c - size + 1] >= size) {
                    best = Math.max(best, size);
                    break;
                }
            }
        }
    }
    return best * best;
}
