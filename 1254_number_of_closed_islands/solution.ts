// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

function closedIsland(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const flood = (sr, sc) => {
        const stack = [[sr, sc]];
        grid[sr][sc] = 1;
        let closed = true;
        while (stack.length) {
            const [r, c] = stack.pop();
            if (r === 0 || r === m - 1 || c === 0 || c === n - 1) closed = false;
            for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
                const nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === 0) {
                    grid[nr][nc] = 1;
                    stack.push([nr, nc]);
                }
            }
        }
        return closed;
    };
    let answer = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 0 && flood(r, c)) answer++;
        }
    }
    return answer;
}
