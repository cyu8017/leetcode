// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

/**
 * @param {number[][]} grid
 * @param {number[][]} hits
 * @return {number[]}
 */
var hitBricks = function(grid, hits) {
    const m = grid.length, n = grid[0].length;
    const roof = m * n;
    const parent = new Array(roof + 1);
    const size = new Array(roof + 1);
    for (let i = 0; i <= roof; i++) {
        parent[i] = i;
        size[i] = 1;
    }
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const unite = (a, b) => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        parent[ra] = rb;
        size[rb] += size[ra];
    };
    const idx = (r, c) => r * n + c;
    const status = grid.map(row => row.slice());
    for (const [hr, hc] of hits) status[hr][hc] = 0;
    const dr = [-1, 1, 0, 0], dc = [0, 0, -1, 1];
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (status[r][c] === 0) continue;
            if (r === 0) unite(idx(r, c), roof);
            for (let k = 0; k < 4; k++) {
                const nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] === 1) {
                    unite(idx(r, c), idx(nr, nc));
                }
            }
        }
    }
    const answer = new Array(hits.length).fill(0);
    for (let i = hits.length - 1; i >= 0; i--) {
        const r = hits[i][0], c = hits[i][1];
        if (grid[r][c] === 0) continue;
        const prev = size[find(roof)];
        status[r][c] = 1;
        if (r === 0) unite(idx(r, c), roof);
        for (let k = 0; k < 4; k++) {
            const nr = r + dr[k], nc = c + dc[k];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] === 1) {
                unite(idx(r, c), idx(nr, nc));
            }
        }
        const curr = size[find(roof)];
        answer[i] = Math.max(0, curr - prev - 1);
    }
    return answer;
};
