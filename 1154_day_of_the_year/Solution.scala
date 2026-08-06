// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

object Solution {
  def dayOfYear(date: String): Int = {
    val parts = date.split("-").map(_.toInt)
    val year = parts(0)
    val month = parts(1)
    val day = parts(2)
    val leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
    val days = Array(31, if (leap) 29 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days.take(month - 1).sum + day
  }
}
