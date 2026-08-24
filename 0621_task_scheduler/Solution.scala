// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

object Solution {
  def leastInterval(tasks: Array[Char], n: Int): Int = {
    val counts = Array.fill(26)(0)
    tasks.foreach(task => counts(task - 'A') += 1)
    var maxFreq = 0
    counts.foreach(count => maxFreq = math.max(maxFreq, count))
    var maxCount = 0
    counts.foreach(count => if (count == maxFreq) maxCount += 1)
    math.max(tasks.length, (maxFreq - 1) * (n + 1) + maxCount)
  }
}
