// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

/**
 * @param {number[][]} points
 * @return {number}
 */
var minAreaFreeRect = function(points) {
    const n = points.length;
    const groups = new Map();
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const cx = points[i][0] + points[j][0];
            const cy = points[i][1] + points[j][1];
            const dx = points[i][0] - points[j][0];
            const dy = points[i][1] - points[j][1];
            const dist = dx * dx + dy * dy;
            const key = cx + "#" + cy + "#" + dist;
            if (!groups.has(key)) groups.set(key, []);
            groups.get(key).push([i, j]);
        }
    }
    let ans = 1e300;
    for (const pairs of groups.values()) {
        for (let a = 0; a < pairs.length; a++) {
            for (let b = a + 1; b < pairs.length; b++) {
                const p1 = pairs[a][0], p2 = pairs[b][0], q2 = pairs[b][1];
                const d1 = Math.hypot(points[p1][0] - points[p2][0], points[p1][1] - points[p2][1]);
                const d2 = Math.hypot(points[p1][0] - points[q2][0], points[p1][1] - points[q2][1]);
                const area = d1 * d2;
                if (area > 0) ans = Math.min(ans, area);
            }
        }
    }
    return ans >= 1e299 ? 0.0 : ans;
};
