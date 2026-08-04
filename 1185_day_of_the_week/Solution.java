// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

import java.time.*;
import java.util.Locale;

class Solution {
    public String dayOfTheWeek(int day, int month, int year) {
        return LocalDate.of(year, month, day).getDayOfWeek()
            .getDisplayName(java.time.format.TextStyle.FULL, Locale.US);
    }
}
