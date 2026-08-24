// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

object Solution {
  def hardestWorker(n: Int, logs: Array[Array[Int]]): Int = {
    var ans = logs(0)(0)
    var best = logs(0)(1)
    var prev = 0
    var i = 0
    while (i < logs.length) {
      val log = logs(i)
      val dur = log(1) - prev
      if (dur > best || (dur == best && log(0) < ans)) {
        best = dur
        ans = log(0)
      }
      prev = log(1)
      i += 1
    }
    ans
  }
}
