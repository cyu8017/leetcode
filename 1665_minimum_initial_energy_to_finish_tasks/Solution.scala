// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

object Solution {
  def minimumEffort(tasks: Array[Array[Int]]): Int = {
    val sorted = tasks.sortBy(t => -(t(1) - t(0)))
    var energy = 0
    var spent = 0
    for (t <- sorted) {
      val cost = t(0)
      val minimum = t(1)
      if (spent + minimum > energy) energy = spent + minimum
      spent += cost
    }
    energy
  }
}
