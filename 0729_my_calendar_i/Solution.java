// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

import java.util.*;

class MyCalendar {
    private final List<int[]> bookings = new ArrayList<>();

    public MyCalendar() {}

    public boolean book(int startTime, int endTime) {
        for (int[] b : bookings) {
            if (b[0] < endTime && startTime < b[1]) return false;
        }
        bookings.add(new int[] {startTime, endTime});
        return true;
    }
}
