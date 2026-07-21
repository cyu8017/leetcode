"use strict";
// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/
function maxBuilding(n, restrictions) {
    const points = [[1, 0], ...restrictions.map((r) => [r[0], r[1]])];
    points.sort((a, b) => a[0] - b[0]);
    if (points[points.length - 1][0] !== n)
        points.push([n, n - 1]);
    for (let i = 1; i < points.length; i++) {
        const [prevId, prevHeight] = points[i - 1];
        const [currId, currHeight] = points[i];
        points[i][1] = Math.min(currHeight, prevHeight + currId - prevId);
    }
    for (let i = points.length - 2; i >= 0; i--) {
        const [nextId, nextHeight] = points[i + 1];
        const [currId, currHeight] = points[i];
        points[i][1] = Math.min(currHeight, nextHeight + nextId - currId);
    }
    let best = Math.max(...points.map((p) => p[1]));
    for (let i = 0; i < points.length - 1; i++) {
        const [id1, h1] = points[i];
        const [id2, h2] = points[i + 1];
        best = Math.max(best, Math.floor((h1 + h2 + id2 - id1) / 2));
    }
    return best;
}
