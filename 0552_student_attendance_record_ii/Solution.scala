// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

object Solution {
  def checkRecord(n: Int): Int = {
    val MOD = 1000000007
    var dp = Array(Array(1L, 0L, 0L), Array(0L, 0L, 0L))
    for (_ <- 0 until n) {
      val nxt = Array.ofDim[Long](2, 3)
      for (absences <- 0 until 2; lates <- 0 until 3) {
        val ways = dp(absences)(lates)
        if (ways != 0) {
          nxt(absences)(0) = (nxt(absences)(0) + ways) % MOD
          if (absences == 0) nxt(1)(0) = (nxt(1)(0) + ways) % MOD
          if (lates < 2) nxt(absences)(lates + 1) = (nxt(absences)(lates + 1) + ways) % MOD
        }
      }
      dp = nxt
    }
    var total = 0L
    for (absences <- 0 until 2; lates <- 0 until 3) {
      total = (total + dp(absences)(lates)) % MOD
    }
    total.toInt
  }
}
