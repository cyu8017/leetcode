// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

import java.time.LocalDate
import java.time.format.TextStyle
import java.util.Locale

class Solution {
    fun dayOfTheWeek(day: Int, month: Int, year: Int): String {
        return LocalDate.of(year, month, day).dayOfWeek.getDisplayName(TextStyle.FULL, Locale.US)
    }
}
