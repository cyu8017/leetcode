// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

object Solution {
  def mostSimilar(n: Int, roads: Array[Array[Int]], names: Array[String], targetPath: Array[String]): List[Int] = {
    val graph = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (Array(a, b) <- roads) {
      graph(a) += b
      graph(b) += a
    }
    var dp = Array.tabulate(n)(node => (if (names(node) != targetPath(0)) 1 else 0, Vector(node)))
    for (i <- 1 until targetPath.length) {
      val next = Array.ofDim[(Int, Vector[Int])](n)
      for (node <- 0 until n) {
        val (cost, path) = graph(node).map(dp).minBy(_._1)
        next(node) = (cost + (if (names(node) != targetPath(i)) 1 else 0), path :+ node)
      }
      dp = next
    }
    dp.minBy(_._1)._2.toList
  }
}
