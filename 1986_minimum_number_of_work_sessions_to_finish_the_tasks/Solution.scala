// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

object Solution {
  def minSessions(tasks: Array[Int], sessionTime: Int): Int = {
    val n = tasks.length
    val INF = (n + 1, 0)
    val dp = Array.fill(1 << n)(INF)
    dp(0) = (1, 0)
    for (mask <- 0 until (1 << n)) {
      val (sessions, used) = dp(mask)
      if (sessions <= n) {
        for (i <- 0 until n if (mask & (1 << i)) == 0) {
          val t = tasks(i)
          val nmask = mask | (1 << i)
          val cand = if (used + t <= sessionTime) (sessions, used + t) else (sessions + 1, t)
          if (cand._1 < dp(nmask)._1 || (cand._1 == dp(nmask)._1 && cand._2 < dp(nmask)._2)) {
            dp(nmask) = cand
          }
        }
      }
    }
    dp((1 << n) - 1)._1
  }
}
