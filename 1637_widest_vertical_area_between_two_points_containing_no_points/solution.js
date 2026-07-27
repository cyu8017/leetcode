// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

/**
 * @param {number[][]} points
 * @return {number}
 */
var maxWidthOfVerticalArea = function(points) {
    const xs = points.map((p) => p[0]).sort((a, b) => a - b);
    let ans = 0;
    for (let i = 1; i < xs.length; i++) ans = Math.max(ans, xs[i] - xs[i - 1]);
    return ans;
};
