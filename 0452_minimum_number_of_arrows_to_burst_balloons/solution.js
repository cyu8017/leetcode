// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution {
    findMinArrowShots(points) {
        if (!points.length) return 0;
        points.sort((a, b) => a[1] - b[1]);
        let arrows = 1;
        let end = points[0][1];
        for (let i = 1; i < points.length; i += 1) {
            const [start, finish] = points[i];
            if (start > end) {
                arrows += 1;
                end = finish;
            }
        }
        return arrows;
    }
}

module.exports = { Solution };
