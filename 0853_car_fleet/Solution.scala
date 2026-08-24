// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

object Solution {
  def carFleet(target: Int, position: Array[Int], speed: Array[Int]): Int = {
    val n = position.length
    val cars = Array.tabulate(n)(i => (position(i), speed(i)))
    scala.util.Sorting.quickSort(cars)(Ordering.by[(Int, Int), Int](_._1).reverse)
    var fleets = 0
    var maxTime = 0.0
    cars.foreach { case (pos, spd) =>
      val time = (target - pos).toDouble / spd
      if (time > maxTime) {
        fleets += 1
        maxTime = time
      }
    }
    fleets
  }
}
