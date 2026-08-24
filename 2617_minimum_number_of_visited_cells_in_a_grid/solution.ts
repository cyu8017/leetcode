// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

export function minimumVisitedCells(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const dist = Array.from({ length: m }, () => new Array(n).fill(-1));
    const q = [[0, 0]];
    dist[0][0] = 1;
    while (q.length) {
        const cur = q.shift();
        const r = cur[0], c = cur[1];
        if (r === m - 1 && c === n - 1) return dist[r][c];
        for (let nc = c + 1; nc <= c + grid[r][c] && nc < n; ++nc) {
            if (dist[r][nc] === -1) {
                dist[r][nc] = dist[r][c] + 1;
                q.push([r, nc]);
            }
        }
        for (let nr = r + 1; nr <= r + grid[r][c] && nr < m; ++nr) {
            if (dist[nr][c] === -1) {
                dist[nr][c] = dist[r][c] + 1;
                q.push([nr, c]);
            }
        }
    }
    return -1;
}
