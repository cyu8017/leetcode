// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

import java.util.Arrays;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int[] starts = new int[intervals.length];
        int[] ends = new int[intervals.length];
        for (int index = 0; index < intervals.length; index++) {
            starts[index] = intervals[index][0];
            ends[index] = intervals[index][1];
        }
        Arrays.sort(starts);
        Arrays.sort(ends);

        int rooms = 0;
        int maxRooms = 0;
        int startIndex = 0;
        int endIndex = 0;
        while (startIndex < starts.length) {
            if (starts[startIndex] < ends[endIndex]) {
                rooms += 1;
                maxRooms = Math.max(maxRooms, rooms);
                startIndex += 1;
            } else {
                rooms -= 1;
                endIndex += 1;
            }
        }
        return maxRooms;
    }
}
