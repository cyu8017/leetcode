// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

/**
 * @param {number[][]} points
 * @param {string} s
 * @return {number}
 */
var maxPointsInsideSquare = function(points, s) {
    const g = new Map();
    const keys = [];
    for (let i = 0; i < points.length; i++) {
        const key = Math.max(Math.max(points[i][0], -points[i][0]), Math.max(points[i][1], -points[i][1]));
        if (!g.has(key)) {
            g.set(key, []);
            let lo = 0, hi = keys.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (keys[mid] < key) lo = mid + 1;
                else hi = mid;
            }
            keys.splice(lo, 0, key);
        }
        g.get(key).push(i);
    }
    const vis = new Array(26).fill(false);
    let ans = 0;
    for (const key of keys) {
        const list = g.get(key);
        for (const i of list) {
            const j = s.charCodeAt(i) - 97;
            if (vis[j]) return ans;
            vis[j] = true;
        }
        ans += list.length;
    }
    return ans;
};
