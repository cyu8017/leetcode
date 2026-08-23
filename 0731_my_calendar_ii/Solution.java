// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

import java.util.*;

class MyCalendarTwo {
    private final List<int[]> booked = new ArrayList<>();
    private final List<int[]> overlaps = new ArrayList<>();

    public MyCalendarTwo() {}

    public boolean book(int startTime, int endTime) {
        for (int[] o : overlaps) {
            if (o[0] < endTime && startTime < o[1]) return false;
        }
        for (int[] b : booked) {
            if (b[0] < endTime && startTime < b[1]) {
                overlaps.add(new int[] {Math.max(b[0], startTime), Math.min(b[1], endTime)});
            }
        }
        booked.add(new int[] {startTime, endTime});
        return true;
    }
}
