// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/

object Solution {
  def checkRecord(s: String): Boolean = {
    var absents = 0
    var lateStreak = 0
    for (i <- s.indices) {
      val ch = s.charAt(i)
      if (ch == 'A') {
        absents += 1
        if (absents >= 2) return false
        lateStreak = 0
      } else if (ch == 'L') {
        lateStreak += 1
        if (lateStreak >= 3) return false
      } else {
        lateStreak = 0
      }
    }
    true
  }
}
