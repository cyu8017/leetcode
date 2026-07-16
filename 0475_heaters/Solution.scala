// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

import java.util.Arrays

object Solution {
  def findRadius(houses: Array[Int], heaters: Array[Int]): Int = {
    val sortedHeaters = heaters.sorted
    var radius = 0
    houses.foreach { house =>
      val position = Arrays.binarySearch(sortedHeaters, house)
      val insertionPoint = if (position >= 0) position else -(position + 1)
      val distances = scala.collection.mutable.ArrayBuffer.empty[Int]
      if (insertionPoint < sortedHeaters.length) {
        distances += math.abs(sortedHeaters(insertionPoint) - house)
      }
      if (insertionPoint > 0) {
        distances += math.abs(sortedHeaters(insertionPoint - 1) - house)
      }
      radius = math.max(radius, distances.min)
    }
    radius
  }
}
