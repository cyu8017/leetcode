// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

public class Solution {
    public bool CanAttendMeetings(int[][] intervals) {
        Array.Sort(intervals, (left, right) => left[0].CompareTo(right[0]));
        for (int index = 1; index < intervals.Length; index++) {
            if (intervals[index][0] < intervals[index - 1][1]) {
                return false;
            }
        }
        return true;
    }
}
