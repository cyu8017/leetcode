// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

object Solution {
  def sumOfDistancesInTree(n: Int, edges: Array[Array[Int]]): Array[Int] = {
    val graph = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    edges.foreach { e =>
      graph(e(0)) += e(1)
      graph(e(1)) += e(0)
    }
    val count = Array.fill(n)(1)
    val ans = Array.ofDim[Int](n)
    def post(node: Int, parent: Int): Unit = {
      graph(node).foreach { child =>
        if (child != parent) {
          post(child, node)
          count(node) += count(child)
          ans(node) += ans(child) + count(child)
        }
      }
    }
    def reroot(node: Int, parent: Int): Unit = {
      graph(node).foreach { child =>
        if (child != parent) {
          ans(child) = ans(node) - count(child) + (n - count(child))
          reroot(child, node)
        }
      }
    }
    post(0, -1)
    reroot(0, -1)
    ans
  }
}
