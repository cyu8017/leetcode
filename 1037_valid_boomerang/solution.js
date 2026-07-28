// LeetCode 1037 - Valid Boomerang
// https://leetcode.com/problems/valid-boomerang/

/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function(points) {
    const [[x1, y1], [x2, y2], [x3, y3]] = points;
    return (x2 - x1) * (y3 - y1) !== (x3 - x1) * (y2 - y1);
};
