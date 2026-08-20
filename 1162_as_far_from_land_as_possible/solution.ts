// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

function maxDistance(grid: number[][]): number {
    const n = grid.length;
    const queue = [];
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 1) queue.push([r, c]);
        }
    }
    if (!queue.length || queue.length === n * n) return -1;
    let dist = -1, qi = 0;
    while (qi < queue.length) {
        const size = queue.length - qi;
        dist++;
        for (let s = 0; s < size; s++) {
            const [r, c] = queue[qi++];
            for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] === 0) {
                    grid[nr][nc] = 1;
                    queue.push([nr, nc]);
                }
            }
        }
    }
    return dist;
}
