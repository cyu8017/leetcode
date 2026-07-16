// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

import java.util.Arrays;

class Solution {
    public int[] findRightInterval(int[][] intervals) {
        int n = intervals.length;
        int[][] indexed = new int[n][2];
        for (int i = 0; i < n; i++) {
            indexed[i][0] = intervals[i][0];
            indexed[i][1] = i;
        }
        Arrays.sort(indexed, (a, b) -> Integer.compare(a[0], b[0]));
        int[] starts = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = indexed[i][0];
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int end = intervals[i][1];
            int position = Arrays.binarySearch(starts, end);
            if (position < 0) {
                position = -position - 1;
            }
            result[i] = position == n ? -1 : indexed[position][1];
        }
        return result;
    }
}
