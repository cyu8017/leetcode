// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

export function canPartitionGrid(grid: any): any {
    let s = 0;
    for (const row of grid) for (const x of row) s += x;
    if (s % 2 !== 0) return false;
    const m = grid.length, n = grid[0].length;
    let pre = 0;
    for (let i = 0; i < m; i++) {
        for (const x of grid[i]) pre += x;
        if (pre * 2 === s && i + 1 < m) return true;
    }
    pre = 0;
    for (let j = 0; j < n; j++) {
        for (let i = 0; i < m; i++) pre += grid[i][j];
        if (pre * 2 === s && j + 1 < n) return true;
    }
    return false;
}
