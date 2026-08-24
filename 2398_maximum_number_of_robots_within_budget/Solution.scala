// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

object Solution {
  def maximumRobots(chargeTimes: Array[Int], runningCosts: Array[Int], budget: Long): Int = {
    val n = chargeTimes.length
    var left = 0
    var sum = 0L
    val dq = scala.collection.mutable.ArrayDeque.empty[Int]
    var ans = 0
    var right = 0
    while (right < n) {
      while (dq.nonEmpty && chargeTimes(dq.last) <= chargeTimes(right)) dq.removeLast()
      dq.append(right)
      sum += runningCosts(right)
      while (left <= right && chargeTimes(dq.head).toLong + (right - left + 1).toLong * sum > budget) {
        if (dq.head == left) dq.removeHead()
        sum -= runningCosts(left)
        left += 1
      }
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
