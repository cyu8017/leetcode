// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

class Solution {
    public int numberOfDays(int year, int month) {
        int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (month == 2 && isLeap(year)) return 29;
        return days[month - 1];
    }

    private boolean isLeap(int year) {
        return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
    }
}
