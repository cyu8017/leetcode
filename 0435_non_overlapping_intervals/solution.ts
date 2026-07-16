// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

export class Solution {
    eraseOverlapIntervals(intervals: number[][]): number {
        intervals.sort((a, b) => a[1] - b[1]);
        let removed = 0;
        let end = Number.NEGATIVE_INFINITY;
        for (const [start, finish] of intervals) {
            if (start < end) {
                removed += 1;
            } else {
                end = finish;
            }
        }
        return removed;
    }
}
