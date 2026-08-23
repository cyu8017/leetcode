// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var intersectionSizeTwo = function(intervals) {
    intervals = intervals.slice().sort((a, b) => a[1] !== b[1] ? a[1] - b[1] : a[0] - b[0]);
    let size = 0, first = -1, second = -1;
    for (const interval of intervals) {
        const left = interval[0], right = interval[1];
        if (left <= first) continue;
        if (left <= second) { size++; first = second; second = right; }
        else { size += 2; first = right - 1; second = right; }
    }
    return size;
};
