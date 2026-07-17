// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

function getFood(grid: string[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;
    const queue: [number, number, number][] = [];
    const seen: boolean[][] = Array.from({ length: rows }, () => new Array(cols).fill(false));
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '*') {
                queue.push([r, c, 0]);
                seen[r][c] = true;
            }
        }
    }
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let head = 0;
    while (head < queue.length) {
        const [r, c, d] = queue[head++];
        if (grid[r][c] === '#') {
            return d;
        }
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr][nc] && grid[nr][nc] !== 'X') {
                seen[nr][nc] = true;
                queue.push([nr, nc, d + 1]);
            }
        }
    }
    return -1;
}
