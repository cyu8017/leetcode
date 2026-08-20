// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

function maxPoints(points: number[][]): number {
    const m = points.length, n = points[0].length;
    let prev = points[0].slice();
    for (let r = 1; r < m; r++) {
        const left = new Array(n), right = new Array(n), cur = new Array(n);
        left[0] = prev[0];
        for (let c = 1; c < n; c++) left[c] = Math.max(left[c - 1] - 1, prev[c]);
        right[n - 1] = prev[n - 1];
        for (let c = n - 2; c >= 0; c--) right[c] = Math.max(right[c + 1] - 1, prev[c]);
        for (let c = 0; c < n; c++) cur[c] = points[r][c] + Math.max(left[c], right[c]);
        prev = cur;
    }
    return Math.max(...prev);
}
