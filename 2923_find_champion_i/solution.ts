// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

export function findChampion(grid: number[][]): number {
    const n = grid.length;
    for (let i = 0; i < n; i++) {
        let win = true;
        for (let j = 0; j < n; j++)
            if (i !== j && grid[i][j] === 0) { win = false; break; }
        if (win) return i;
    }
    return -1;
}
