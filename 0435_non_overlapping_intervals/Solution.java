// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int removed = 0;
        int end = Integer.MIN_VALUE;
        for (int[] interval : intervals) {
            if (interval[0] < end) {
                removed++;
            } else {
                end = interval[1];
            }
        }
        return removed;
    }
}
