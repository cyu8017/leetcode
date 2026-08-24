// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

object Solution {
  def dateRangeGenerator(start: String, end: String, step: Int): List[String] = {
    val sp = start.split("-")
    val ep = end.split("-")
    if (sp.length != 3 || ep.length != 3) return List.empty
    var y = sp(0).toInt
    var m = sp(1).toInt
    var d = sp(2).toInt
    val ey = ep(0).toInt
    val em = ep(1).toInt
    val ed = ep(2).toInt
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    while (cmp(y, m, d, ey, em, ed)) {
      ans += f"$y%04d-$m%02d-$d%02d"
      val ymd = addDays(y, m, d, step)
      y = ymd(0)
      m = ymd(1)
      d = ymd(2)
    }
    ans.toList
  }

  private def isLeap(yy: Int): Boolean =
    (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0)

  private def addDays(yy0: Int, mm0: Int, dd0: Int, days0: Int): Array[Int] = {
    var yy = yy0
    var mm = mm0
    var dd = dd0
    var days = days0
    val mdays = Array(0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    while (days > 0) {
      mdays(2) = if (isLeap(yy)) 29 else 28
      dd += 1
      if (dd > mdays(mm)) {
        dd = 1
        mm += 1
      }
      if (mm > 12) {
        mm = 1
        yy += 1
      }
      days -= 1
    }
    Array(yy, mm, dd)
  }

  private def cmp(y: Int, m: Int, d: Int, ey: Int, em: Int, ed: Int): Boolean = {
    if (y != ey) y < ey
    else if (m != em) m < em
    else d <= ed
  }
}
