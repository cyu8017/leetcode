// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

export function sortMatrix(grid: any): any {
    const n = grid.length;
    const diags = new Map();
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const key = i - j;
            if (!diags.has(key)) diags.set(key, []);
            diags.get(key).push(grid[i][j]);
        }
    }
    for (const [key, list] of diags) {
        if (key >= 0) list.sort((a, b) => b - a);
        else list.sort((a, b) => a - b);
    }
    const idx = new Map();
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const k = i - j;
            const pos = idx.get(k) || 0;
            grid[i][j] = diags.get(k)[pos];
            idx.set(k, pos + 1);
        }
    }
    return grid;
}
