// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

/**
 * @param {number[][]} points
 * @param {number} w
 * @return {number}
 */
var minRectanglesToCoverPoints = function(points, w) {
    points = points.slice().sort((a, b) => a[0] - b[0]);
    let ans = 0, x1 = -1;
    for (const p of points) {
        if (p[0] > x1) {
            ans++;
            x1 = p[0] + w;
        }
    }
    return ans;
};
