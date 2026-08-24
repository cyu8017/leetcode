// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

object Solution {
  def minDistance(height: Int, width: Int, tree: Array[Int], squirrel: Array[Int], nuts: Array[Array[Int]]): Int = {
    var total = 0
    var bestSave = Int.MinValue
    nuts.foreach { nut =>
      val treeDist = dist(tree, nut)
      val squirrelDist = dist(squirrel, nut)
      total += 2 * treeDist
      val save = treeDist - squirrelDist
      if (save > bestSave) bestSave = save
    }
    total - bestSave
  }

  private def dist(a: Array[Int], b: Array[Int]): Int =
    math.abs(a(0) - b(0)) + math.abs(a(1) - b(1))
}
