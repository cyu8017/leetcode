// LeetCode 1391: Check If There Is A Valid Path In A Grid

function hasValidPath(grid: any): any {
    const connections = [[], [[0, -1], [0, 1]], [[-1, 0], [1, 0]], [[0, -1], [1, 0]], [[0, 1], [1, 0]], [[0, -1], [-1, 0]], [[0, 1], [-1, 0]]];
    const rows = grid.length, cols = grid[0].length, queue = [[0, 0]], seen = new Set(["0,0"]);
    for (let head = 0; head < queue.length; head++) {
        const [r, c] = queue[head];
        if (r === rows - 1 && c === cols - 1) return true;
        for (const [dr, dc] of connections[grid[r][c]]) {
            const nr = r + dr, nc = c + dc, key = `${nr},${nc}`;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || seen.has(key)) continue;
            if (connections[grid[nr][nc]].some(([rr, cc]: any): any => rr === -dr && cc === -dc)) { seen.add(key); queue.push([nr, nc]); }
        }
    }
    return false;
}
