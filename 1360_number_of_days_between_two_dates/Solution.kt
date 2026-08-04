// LeetCode 1360 - Number of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

import java.time.LocalDate
import java.time.temporal.ChronoUnit
import kotlin.math.abs

class Solution {
    fun daysBetweenDates(date1: String, date2: String): Int {
        return abs(ChronoUnit.DAYS.between(LocalDate.parse(date1), LocalDate.parse(date2))).toInt()
    }
}
