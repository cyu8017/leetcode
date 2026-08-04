// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

class Solution {
    fun numberOfDays(year: Int, month: Int): Int {
        val days = intArrayOf(0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if (month != 2) return days[month]
        val leap = year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)
        return if (leap) 29 else 28
    }
}
