// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var removeCoveredIntervals = function(intervals) {
    intervals.sort((a, b) => (a[0] - b[0]) || (b[1] - a[1]));
    let answer = 0;
    let farthest = -1;
    for (const [, end] of intervals) {
        if (end > farthest) {
            answer++;
            farthest = end;
        }
    }
    return answer;
};
