// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

object Solution {
  def getCollisionTimes(cars: Array[Array[Int]]): Array[Double] = {
    val n = cars.length
    val ans = Array.fill(n)(-1.0)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- (n - 1) to 0 by -1) {
      val pos = cars(i)(0)
      val speed = cars(i)(1)
      var done = false
      while (!done && stack.nonEmpty) {
        val j = stack.last
        if (speed <= cars(j)(1)) {
          stack.remove(stack.length - 1)
        } else {
          val t = (cars(j)(0) - pos).toDouble / (speed - cars(j)(1))
          if (ans(j) < 0 || t <= ans(j)) {
            ans(i) = t
            done = true
          } else {
            stack.remove(stack.length - 1)
          }
        }
      }
      stack += i
    }
    ans
  }
}
