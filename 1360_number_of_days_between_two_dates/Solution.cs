// LeetCode 1360 - Number Of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

public class Solution {
    public int DaysBetweenDates(string date1, string date2) {
        return System.Math.Abs((int)(System.DateTime.Parse(date1) - System.DateTime.Parse(date2)).TotalDays);
    }
}
