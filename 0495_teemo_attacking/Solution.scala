// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

object Solution {
  def findPoisonedDuration(timeSeries: Array[Int], duration: Int): Int = {
    if (timeSeries.isEmpty) return 0
    var total = duration
    for (index <- 1 until timeSeries.length) {
      total += math.min(duration, timeSeries(index) - timeSeries(index - 1))
    }
    total
  }
}
