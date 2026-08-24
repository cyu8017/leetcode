// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

object Solution {
  def asteroidsDestroyed(mass: Int, asteroids: Array[Int]): Boolean = {
    val sorted = asteroids.sorted
    var cur = mass.toLong
    sorted.foreach { a =>
      if (cur < a) return false
      cur += a
    }
    true
  }
}
