// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

export function equalPairs(grid: number[][]): number {
    const n = grid.length;
    const freq = new Map();
    for (let i = 0; i < n; i++) {
        const key = grid[i].join(',');
        freq.set(key, (freq.get(key) || 0) + 1);
    }
    let ans = 0;
    for (let j = 0; j < n; j++) {
        const col = [];
        for (let i = 0; i < n; i++) col.push(grid[i][j]);
        ans += freq.get(col.join(',')) || 0;
    }
    return ans;
}
