// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(interval -> interval[0]));
        for (int index = 1; index < intervals.length; index++) {
            if (intervals[index][0] < intervals[index - 1][1]) {
                return false;
            }
        }
        return true;
    }
}
