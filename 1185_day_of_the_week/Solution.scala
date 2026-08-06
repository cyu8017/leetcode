// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

object Solution {
  def dayOfTheWeek(day: Int, month: Int, year: Int): String = {
    val names = Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    val cal = java.util.Calendar.getInstance()
    cal.set(year, month - 1, day)
    names(cal.get(java.util.Calendar.DAY_OF_WEEK) - 1)
  }
}
