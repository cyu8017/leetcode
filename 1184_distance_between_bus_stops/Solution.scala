// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

object Solution {
  def distanceBetweenBusStops(distance: Array[Int], start: Int, destination: Int): Int = {
    val (a, b) = if (start > destination) (destination, start) else (start, destination)
    val clockwise = distance.slice(a, b).sum
    math.min(clockwise, distance.sum - clockwise)
  }
}
