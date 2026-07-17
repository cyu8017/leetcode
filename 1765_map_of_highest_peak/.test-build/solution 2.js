"use strict";
// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/
function highestPeak(isWater) {
    const m = isWater.length;
    const n = isWater[0].length;
    const dist = Array.from({ length: m }, () => new Array(n).fill(-1));
    const queue = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (isWater[i][j]) {
                dist[i][j] = 0;
                queue.push([i, j]);
            }
        }
    }
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let head = 0;
    while (head < queue.length) {
        const [i, j] = queue[head++];
        for (const [di, dj] of dirs) {
            const x = i + di;
            const y = j + dj;
            if (x >= 0 && x < m && y >= 0 && y < n && dist[x][y] === -1) {
                dist[x][y] = dist[i][j] + 1;
                queue.push([x, y]);
            }
        }
    }
    return dist;
}
