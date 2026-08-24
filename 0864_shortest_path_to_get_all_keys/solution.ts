// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

export function shortestPathAllKeys(grid: string[]): number {
    const m = grid.length, n = grid[0].length;
    let allKeys = 0, sr = 0, sc = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const ch = grid[i][j];
            if (ch === '@') { sr = i; sc = j; }
            else if (ch >= 'a' && ch <= 'f') allKeys |= 1 << (ch.charCodeAt(0) - 97);
        }
    }
    const encode = (r, c, mask) => (r << 20) | (c << 10) | mask;
    const queue = [[sr, sc, 0, 0]];
    const seen = new Set([encode(sr, sc, 0)]);
    const dr = [1, -1, 0, 0], dc = [0, 0, 1, -1];
    while (queue.length) {
        const [r, c, mask, dist] = queue.shift();
        if (mask === allKeys) return dist;
        for (let k = 0; k < 4; k++) {
            const nr = r + dr[k], nc = c + dc[k];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] === '#') continue;
            const cell = grid[nr][nc];
            let nmask = mask;
            if (cell >= 'a' && cell <= 'f') nmask |= 1 << (cell.charCodeAt(0) - 97);
            if (cell >= 'A' && cell <= 'F' && (mask & (1 << (cell.charCodeAt(0) - 65))) === 0) continue;
            const key = encode(nr, nc, nmask);
            if (!seen.has(key)) {
                seen.add(key);
                queue.push([nr, nc, nmask, dist + 1]);
            }
        }
    }
    return -1;
}
