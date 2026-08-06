// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

object Solution {
  def reformatDate(date: String): String = {
    val months = Array("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
    val parts = date.split(" ")
    val day = parts(0).dropRight(2).toInt
    val month = months.indexOf(parts(1)) + 1
    f"${parts(2)}-$month%02d-$day%02d"
  }
}
