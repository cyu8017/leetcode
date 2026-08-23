// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

using System;

public class Solution {
    public int[] FindRightInterval(int[][] intervals) {
        int n = intervals.Length;
        (int start, int index)[] indexed = new (int, int)[n];
        for (int i = 0; i < n; i++) {
            indexed[i] = (intervals[i][0], i);
        }
        Array.Sort(indexed, (a, b) => a.start.CompareTo(b.start));
        int[] starts = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = indexed[i].start;
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int end = intervals[i][1];
            int position = Array.BinarySearch(starts, end);
            if (position < 0) {
                position = ~position;
            }
            result[i] = position == n ? -1 : indexed[position].index;
        }
        return result;
    }
}
