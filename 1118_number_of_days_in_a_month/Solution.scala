// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

object Solution {
  def numberOfDays(year: Int, month: Int): Int = {
    val days = Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if (month == 2 && ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)) 29
    else days(month - 1)
  }
}
