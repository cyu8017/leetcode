// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

using System.Collections.Generic;

public class MyCalendar {
    private readonly List<(int start, int end)> bookings = new List<(int, int)>();
    public MyCalendar() { }

    public bool Book(int startTime, int endTime) {
        foreach (var (start, end) in bookings) {
            if (start < endTime && startTime < end) return false;
        }
        bookings.Add((startTime, endTime));
        return true;
    }
}
