// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

object Solution {
  def findDelayedArrivalTime(arrivalTime: Int, delayedTime: Int): Int =
    (arrivalTime + delayedTime) % 24
}
