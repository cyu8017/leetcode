// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

object Solution {
  def deleteTreeNodes(nodes: Int, parent: Array[Int], value: Array[Int]): Int = {
    val children = Array.fill(nodes)(scala.collection.mutable.ListBuffer.empty[Int])
    for (node <- 1 until nodes) children(parent(node)) += node
    def dfs(node: Int): (Int, Int) = {
      var total = value(node)
      var count = 1
      for (child <- children(node)) {
        val (childSum, childCount) = dfs(child)
        total += childSum
        count += childCount
      }
      if (total == 0) (0, 0) else (total, count)
    }
    dfs(0)._2
  }
}
