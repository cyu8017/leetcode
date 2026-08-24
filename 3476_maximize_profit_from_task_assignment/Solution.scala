// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

object Solution {
  def maxProfit(workers: Array[Int], tasks: Array[Array[Int]]): Long = {
    java.util.Arrays.sort(workers)
    java.util.Arrays.sort(tasks, (a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(0), b(0)))
    var ans = 0L
    val used = new Array[Boolean](tasks.length)
    workers.foreach { w =>
      var best = -1
      var bi = -1
      var i = 0
      var stop = false
      while (i < tasks.length && !stop) {
        if (!used(i)) {
          if (tasks(i)(0) > w) stop = true
          else if (tasks(i)(1) > best) {
            best = tasks(i)(1)
            bi = i
          }
        }
        i += 1
      }
      if (bi >= 0) {
        used(bi) = true
        ans += best
      }
    }
    ans
  }
}
