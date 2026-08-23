// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

using System;
using System.Collections.Generic;

public class MyCalendarThree {
    private readonly SortedDictionary<int, int> delta = new SortedDictionary<int, int>();
    public MyCalendarThree() { }

    public int Book(int startTime, int endTime) {
        if (!delta.ContainsKey(startTime)) delta[startTime] = 0;
        if (!delta.ContainsKey(endTime)) delta[endTime] = 0;
        delta[startTime]++;
        delta[endTime]--;
        int current = 0, best = 0;
        foreach (var change in delta.Values) {
            current += change;
            best = Math.Max(best, current);
        }
        return best;
    }
}
