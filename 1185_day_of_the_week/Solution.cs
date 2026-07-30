// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

using System;

public class Solution {
    public string DayOfTheWeek(int day, int month, int year) {
        return new DateTime(year, month, day).DayOfWeek.ToString();
    }
}
