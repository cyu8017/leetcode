// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

object Solution {
  def findSmallestSetOfVertices(n: Int, edges: Array[Array[Int]]): List[Int] = {
    val incoming = edges.map(_(1)).toSet
    (0 until n).filterNot(incoming.contains).toList
  }
}
