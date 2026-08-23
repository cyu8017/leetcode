// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    let total = 0;
    for (let i = 1; i < points.length; i++) {
        total += Math.max(
            Math.abs(points[i][0] - points[i - 1][0]),
            Math.abs(points[i][1] - points[i - 1][1]),
        );
    }
    return total;
};
