// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findClosestLeaf(root: TreeNode, k: Int): Int = {
    val graph = scala.collection.mutable.HashMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    val leaves = scala.collection.mutable.HashSet.empty[Int]
    def build(node: TreeNode, parent: TreeNode): Unit = {
      if (node == null) return
      graph.getOrElseUpdate(node.value, scala.collection.mutable.ArrayBuffer.empty[Int])
      if (parent != null) {
        graph.getOrElseUpdate(parent.value, scala.collection.mutable.ArrayBuffer.empty[Int])
        graph(node.value) += parent.value
        graph(parent.value) += node.value
      }
      if (node.left == null && node.right == null) leaves += node.value
      build(node.right, node)
      build(node.left, node)
    }
    build(root, null)
    val q = scala.collection.mutable.Queue[Int]()
    val seen = scala.collection.mutable.HashSet(k)
    q.enqueue(k)
    while (q.nonEmpty) {
      val value = q.dequeue()
      if (leaves.contains(value)) return value
      if (graph.contains(value)) {
        for (neighbor <- graph(value) if seen.add(neighbor)) q.enqueue(neighbor)
      }
    }
    -1
  }
}
