// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

export function regionsBySlashes(grid: string[]): number {
    const n = grid.length;
    const parent = Array.from({ length: n * n * 4 }, (_, i) => i);
    const find = (x) => (parent[x] === x ? x : (parent[x] = find(parent[x])));
    const unite = (a, b) => { parent[find(a)] = find(b); };
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            const root = 4 * (r * n + c);
            const ch = grid[r][c];
            if (ch === "/") {
                unite(root + 0, root + 3);
                unite(root + 1, root + 2);
            } else if (ch === "\\") {
                unite(root + 0, root + 1);
                unite(root + 2, root + 3);
            } else {
                unite(root + 0, root + 1);
                unite(root + 1, root + 2);
                unite(root + 2, root + 3);
            }
            if (r + 1 < n) unite(root + 2, root + 4 * n + 0);
            if (c + 1 < n) unite(root + 1, root + 4 + 3);
        }
    }
    let ans = 0;
    for (let i = 0; i < parent.length; i++) if (find(i) === i) ans++;
    return ans;
}
