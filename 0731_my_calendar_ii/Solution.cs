// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

using System;
using System.Collections.Generic;

public class MyCalendarTwo {
    private readonly List<(int start, int end)> booked = new List<(int, int)>();
    private readonly List<(int start, int end)> overlaps = new List<(int, int)>();
    public MyCalendarTwo() { }

    public bool Book(int startTime, int endTime) {
        foreach (var (start, end) in overlaps) {
            if (start < endTime && startTime < end) return false;
        }
        foreach (var (start, end) in booked) {
            if (start < endTime && startTime < end) {
                overlaps.Add((Math.Max(start, startTime), Math.Min(end, endTime)));
            }
        }
        booked.Add((startTime, endTime));
        return true;
    }
}
