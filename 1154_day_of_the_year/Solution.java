// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

class Solution {
    public int dayOfYear(String date) {
        String[] parts = date.split("-");
        int year = Integer.parseInt(parts[0]);
        int month = Integer.parseInt(parts[1]);
        int day = Integer.parseInt(parts[2]);
        boolean leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
        int[] days = {31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int ans = day;
        for (int i = 0; i < month - 1; i++) ans += days[i];
        return ans;
    }
}
