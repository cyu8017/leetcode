// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

export function numDistinctIslands2(grid: number[][]): number {
    if (grid === null || grid.length === 0) return 0;
    const m = grid.length, n = grid[0].length;
    const dfs = (r, c, cells) => {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] === 0) return;
        grid[r][c] = 0;
        cells.push([r, c]);
        dfs(r + 1, c, cells);
        dfs(r - 1, c, cells);
        dfs(r, c + 1, cells);
        dfs(r, c - 1, cells);
    };
    const canonical = (cells) => {
        const signs = [
            [1, 1, 0], [1, -1, 0], [-1, 1, 0], [-1, -1, 0],
            [1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1]
        ];
        let best = null;
        for (const s of signs) {
            const pts = [];
            for (const p of cells) {
                const x = p[0], y = p[1];
                let nx, ny;
                if (s[2] === 0) { nx = s[0] * x; ny = s[1] * y; }
                else { nx = s[0] * y; ny = s[1] * x; }
                pts.push([nx, ny]);
            }
            let minX = Infinity, minY = Infinity;
            for (const p of pts) {
                minX = Math.min(minX, p[0]);
                minY = Math.min(minY, p[1]);
            }
            for (const p of pts) { p[0] -= minX; p[1] -= minY; }
            pts.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
            const key = pts.map((p) => p[0] + ',' + p[1]).join(';');
            if (best === null || key < best) best = key;
        }
        return best;
    };
    const shapes = new Set();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                const cells = [];
                dfs(i, j, cells);
                shapes.add(canonical(cells));
            }
        }
    }
    return shapes.size;
}
