// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

/**
 * @param {number[][]} points
 * @param {number} angle
 * @param {number[]} location
 * @return {number}
 */
var visiblePoints = function(points, angle, location) {
    let same = 0;
    const a = [];
    for (const [x, y] of points) {
        const dx = x - location[0], dy = y - location[1];
        if (dx === 0 && dy === 0) same++;
        else a.push(Math.atan2(dy, dx));
    }
    a.sort((x, y) => x - y);
    const ext = a.concat(a.map((x) => x + 2 * Math.PI));
    const width = (angle * Math.PI) / 180 + 1e-12;
    let left = 0, best = 0;
    for (let right = 0; right < ext.length; right++) {
        while (ext[right] - ext[left] > width) left++;
        best = Math.max(best, Math.min(a.length, right - left + 1));
    }
    return best + same;
};
