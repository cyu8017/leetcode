// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

object Solution {
  def findMinimumTime(tasks: Array[Array[Int]]): Int = {
    val sorted = tasks.sortBy(_(1))
    val on = Array.fill(2001)(false)
    var ans = 0
    sorted.foreach { t =>
      val start = t(0)
      val end = t(1)
      val dur = t(2)
      var have = 0
      var i = start
      while (i <= end) {
        if (on(i)) have += 1
        i += 1
      }
      var need = dur - have
      i = end
      while (i >= start && need > 0) {
        if (!on(i)) {
          on(i) = true
          need -= 1
          ans += 1
        }
        i -= 1
      }
    }
    ans
  }
}
