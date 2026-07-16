"use strict";
// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Solution = void 0;
class Solution {
    findRightInterval(intervals) {
        const indexed = intervals
            .map(([start], index) => [start, index])
            .sort((a, b) => a[0] - b[0]);
        const starts = indexed.map(([start]) => start);
        const result = [];
        for (const [, end] of intervals) {
            let left = 0;
            let right = starts.length;
            while (left < right) {
                const mid = Math.floor((left + right) / 2);
                if (starts[mid] < end)
                    left = mid + 1;
                else
                    right = mid;
            }
            result.push(left === starts.length ? -1 : indexed[left][1]);
        }
        return result;
    }
}
exports.Solution = Solution;
