"use strict";
// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Solution = void 0;
class Solution {
    eraseOverlapIntervals(intervals) {
        intervals.sort((a, b) => a[1] - b[1]);
        let removed = 0;
        let end = Number.NEGATIVE_INFINITY;
        for (const [start, finish] of intervals) {
            if (start < end) {
                removed += 1;
            }
            else {
                end = finish;
            }
        }
        return removed;
    }
}
exports.Solution = Solution;
