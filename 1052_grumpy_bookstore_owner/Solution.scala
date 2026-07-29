// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

object Solution {
  def maxSatisfied(customers: Array[Int], grumpy: Array[Int], minutes: Int): Int = {
    val base = customers.indices.filter(i => grumpy(i) == 0).map(customers).sum
    var gain = 0
    var best = 0
    for (i <- customers.indices) {
      if (grumpy(i) == 1) gain += customers(i)
      if (i >= minutes && grumpy(i - minutes) == 1) gain -= customers(i - minutes)
      best = math.max(best, gain)
    }
    base + best
  }
}
