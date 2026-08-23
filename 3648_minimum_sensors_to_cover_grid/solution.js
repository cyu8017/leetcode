// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

var minSensors = function(n, m, k) {
    const cover = 2 * k + 1;
    return Math.ceil(n / cover) * Math.ceil(m / cover);
};
