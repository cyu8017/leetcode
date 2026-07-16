// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

import scala.collection.mutable

object Solution {
  def numberOfBoomerangs(points: Array[Array[Int]]): Int = {
    var total = 0
    for (anchor <- points) {
      val distances = mutable.Map.empty[Int, Int]
      for (other <- points) {
        val dx = anchor(0) - other(0)
        val dy = anchor(1) - other(1)
        val distance = dx * dx + dy * dy
        distances(distance) = distances.getOrElse(distance, 0) + 1
      }
      for (count <- distances.values) {
        total += count * (count - 1)
      }
    }
    total
  }
}
