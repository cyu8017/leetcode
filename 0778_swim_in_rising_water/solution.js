// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var swimInWater = function(grid) {
    const n = grid.length;
    const heap = [[grid[0][0], 0, 0]];
    const seen = Array.from({length: n}, () => new Array(n).fill(false));
    seen[0][0] = true;
    const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    while (heap.length > 0) {
        heap.sort((a, b) => a[0] - b[0]);
        const [time, r, c] = heap.shift();
        if (r === n - 1 && c === n - 1) return time;
        for (const d of dirs) {
            const nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[nr][nc]) {
                seen[nr][nc] = true;
                const nt = Math.max(time, grid[nr][nc]);
                heap.push([nt, nr, nc]);
            }
        }
    }
    return -1;
};
