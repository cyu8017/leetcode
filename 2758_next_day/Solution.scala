// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

object Solution {
  def nextDay(date: String): String = {
    val parts = date.split("-")
    if (parts.length != 3) return date
    var y = parts(0).toInt
    var m = parts(1).toInt
    var d = parts(2).toInt
    val mdays = Array(0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if (isLeap(y)) mdays(2) = 29
    d += 1
    if (d > mdays(m)) {
      d = 1
      m += 1
    }
    if (m > 12) {
      m = 1
      y += 1
    }
    f"$y%04d-$m%02d-$d%02d"
  }

  private def isLeap(yy: Int): Boolean =
    (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0)
}
