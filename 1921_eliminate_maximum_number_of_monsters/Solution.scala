// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

object Solution {
  def eliminateMaximum(dist: Array[Int], speed: Array[Int]): Int = {
    val arrival = dist.indices.map(i => (dist(i) + speed(i) - 1) / speed(i)).sorted
    for (i <- arrival.indices) {
      if (arrival(i) <= i) return i
    }
    arrival.length
  }
}
