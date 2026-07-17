// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

object Solution {
  def averageWaitingTime(customers: Array[Array[Int]]): Double = {
    var current = 0L
    var total = 0L
    for (customer <- customers) {
      current = math.max(current, customer(0).toLong) + customer(1)
      total += current - customer(0)
    }
    total.toDouble / customers.length
  }
}
