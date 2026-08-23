// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

/**
 * @param {number} n
 * @param {number[][]} corridors
 * @return {number}
 */
var numberOfPaths = function(n, corridors) {
    const g = Array.from({length: n + 1}, () => new Set());
    for (const e of corridors) {
        g[e[0]].add(e[1]);
        g[e[1]].add(e[0]);
    }
    let ans = 0;
    for (const e of corridors) {
        const a = e[0], b = e[1];
        for (const c of g[a]) if (g[b].has(c)) ans++;
    }
    return Math.floor(ans / 3);
};
