// LeetCode 1232 - Check If It Is A Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    const [x0, y0] = coordinates[0];
    const dx = coordinates[1][0] - x0;
    const dy = coordinates[1][1] - y0;
    for (let i = 2; i < coordinates.length; i++) {
        const [x, y] = coordinates[i];
        if ((x - x0) * dy !== (y - y0) * dx) return false;
    }
    return true;
};
