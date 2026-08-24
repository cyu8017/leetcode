// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

object Solution {
  def nextClosestTime(time: String): String = {
    val digits = Set(time.charAt(0), time.charAt(1), time.charAt(3), time.charAt(4))
    val start = time.substring(0, 2).toInt * 60 + time.substring(3, 5).toInt
    var delta = 1
    while (delta <= 24 * 60) {
      val mins = (start + delta) % (24 * 60)
      val hh = mins / 60
      val mm = mins % 60
      val c0 = ('0' + hh / 10).toChar
      val c1 = ('0' + hh % 10).toChar
      val c2 = ('0' + mm / 10).toChar
      val c3 = ('0' + mm % 10).toChar
      if (digits.contains(c0) && digits.contains(c1) && digits.contains(c2) && digits.contains(c3)) {
        return s"$c0$c1:$c2$c3"
      }
      delta += 1
    }
    time
  }
}
