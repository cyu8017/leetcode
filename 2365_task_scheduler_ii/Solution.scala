// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

object Solution {
  def taskSchedulerII(tasks: Array[Int], space: Int): Long = {
    val next = scala.collection.mutable.Map.empty[Int, Long]
    var day = 0L
    tasks.foreach { t =>
      day = math.max(day, next.getOrElse(t, 0L))
      day += 1
      next(t) = day + space
    }
    day
  }
}
