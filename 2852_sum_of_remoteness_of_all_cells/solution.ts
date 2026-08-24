// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

export function sumRemoteness(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const seen = Array.from({ length: m }, () => Array(n).fill(false));
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let total = 0;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] !== -1) total += grid[i][j];
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === -1 || seen[i][j]) continue;
            const q = [[i, j]];
            seen[i][j] = true;
            let sum = 0, cnt = 0;
            while (q.length) {
                const [x, y] = q.shift();
                sum += grid[x][y];
                cnt++;
                for (const [dx, dy] of dirs) {
                    const ni = x + dx, nj = y + dy;
                    if (ni >= 0 && nj >= 0 && ni < m && nj < n && !seen[ni][nj] && grid[ni][nj] !== -1) {
                        seen[ni][nj] = true;
                        q.push([ni, nj]);
                    }
                }
            }
            ans += (total - sum) * cnt;
        }
    }
    return ans;
}
