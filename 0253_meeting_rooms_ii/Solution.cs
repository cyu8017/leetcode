// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

public class Solution {
    public int MinMeetingRooms(int[][] intervals) {
        int[] starts = new int[intervals.Length];
        int[] ends = new int[intervals.Length];
        for (int index = 0; index < intervals.Length; index++) {
            starts[index] = intervals[index][0];
            ends[index] = intervals[index][1];
        }
        Array.Sort(starts);
        Array.Sort(ends);

        int rooms = 0;
        int maxRooms = 0;
        int startIndex = 0;
        int endIndex = 0;
        while (startIndex < starts.Length) {
            if (starts[startIndex] < ends[endIndex]) {
                rooms += 1;
                maxRooms = Math.Max(maxRooms, rooms);
                startIndex += 1;
            } else {
                rooms -= 1;
                endIndex += 1;
            }
        }
        return maxRooms;
    }
}
