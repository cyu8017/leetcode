// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

var colorGrid = function(n, m, sources) {
    const ans = Array.from({length: n}, () => new Array(m).fill(0));
    let q = sources.map(s => s.slice());
    const dirs = [-1, 0, 1, 0, -1];
    for (const s of q) ans[s[0]][s[1]] = s[2];
    while (q.length) {
        const vis = new Map();
        for (const curr of q) {
            const r = curr[0], c = curr[1], color = curr[2];
            for (let i = 0; i < 4; i++) {
                const x = r + dirs[i], y = c + dirs[i + 1];
                if (x >= 0 && x < n && y >= 0 && y < m && ans[x][y] === 0) {
                    const key = (BigInt(x) << 32n) | BigInt(y >>> 0);
                    if (!vis.has(key) || color > vis.get(key)) vis.set(key, color);
                }
            }
        }
        q = [];
        for (const [key, color] of vis.entries()) {
            const x = Number(key >> 32n);
            const y = Number(key & 0xffffffffn);
            ans[x][y] = color;
            q.push([x, y, color]);
        }
    }
    return ans;
};
