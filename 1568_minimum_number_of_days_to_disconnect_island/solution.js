// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minDays = function(grid) {
    const m = grid.length, n = grid[0].length;
    const islands = () => {
        const seen = new Set();
        let count = 0;
        for (let r = 0; r < m; r++) {
            for (let c = 0; c < n; c++) {
                if (grid[r][c] && !seen.has(r + "," + c)) {
                    count++;
                    const stack = [[r, c]];
                    seen.add(r + "," + c);
                    while (stack.length) {
                        const [x, y] = stack.pop();
                        for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
                            const nx = x + dx, ny = y + dy;
                            const key = nx + "," + ny;
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] && !seen.has(key)) {
                                seen.add(key);
                                stack.push([nx, ny]);
                            }
                        }
                    }
                }
            }
        }
        return count;
    };
    if (islands() !== 1) return 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c]) {
                grid[r][c] = 0;
                if (islands() !== 1) {
                    grid[r][c] = 1;
                    return 1;
                }
                grid[r][c] = 1;
            }
        }
    }
    return 2;
};
