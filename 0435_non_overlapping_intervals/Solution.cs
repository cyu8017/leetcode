// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

using System;

public class Solution {
    public int EraseOverlapIntervals(int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[1].CompareTo(b[1]));
        int removed = 0;
        int end = int.MinValue;
        foreach (int[] interval in intervals) {
            if (interval[0] < end) {
                removed++;
            } else {
                end = interval[1];
            }
        }
        return removed;
    }
}
