// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

object Solution {
  def earliestTime(tasks: Array[Array[Int]]): Int = {
    var ans = 200
    for (task <- tasks) ans = math.min(ans, task(0) + task(1))
    ans
  }
}
