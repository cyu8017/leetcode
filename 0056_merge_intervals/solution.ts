// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

export function merge(intervals: number[][]): number[][] {
    intervals.sort((a, b) => a[0] - b[0]);
    const merged: number[][] = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const [start, end] = intervals[i];
        const last = merged[merged.length - 1];

        if (start <= last[1]) {
            last[1] = Math.max(last[1], end);
        } else {
            merged.push([start, end]);
        }
    }

    return merged;
}
