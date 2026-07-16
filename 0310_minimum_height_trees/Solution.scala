// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

import scala.collection.mutable

object Solution {
  def findMinHeightTrees(n: Int, edges: Array[Array[Int]]): List[Int] = {
    if (n <= 2) {
      return (0 until n).toList
    }

    val graph = Array.fill(n)(mutable.ListBuffer.empty[Int])
    val degree = new Array[Int](n)
    edges.foreach { edge =>
      val left = edge(0)
      val right = edge(1)
      graph(left) += right
      graph(right) += left
      degree(left) += 1
      degree(right) += 1
    }

    var leaves = mutable.ListBuffer.empty[Int]
    for (node <- 0 until n if degree(node) == 1) {
      leaves += node
    }

    var remaining = n
    while (remaining > 2) {
      remaining -= leaves.length
      val newLeaves = mutable.ListBuffer.empty[Int]
      leaves.foreach { leaf =>
        graph(leaf).foreach { neighbor =>
          degree(neighbor) -= 1
          if (degree(neighbor) == 1) {
            newLeaves += neighbor
          }
        }
      }
      leaves = newLeaves
    }
    leaves.toList
  }
}
