// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

import java.util.*;

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] != b[0] ? a[0] - b[0] : b[1] - a[1]);
        int answer = 0, farthest = -1;
        for (int[] interval : intervals) {
            if (interval[1] > farthest) {
                answer++;
                farthest = interval[1];
            }
        }
        return answer;
    }
}
