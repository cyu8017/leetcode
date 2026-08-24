// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def distanceK(root: TreeNode, target: TreeNode, k: Int): List[Int] = {
    val graph = scala.collection.mutable.Map.empty[TreeNode, scala.collection.mutable.ListBuffer[TreeNode]]
    def build(node: TreeNode, parent: TreeNode): Unit = {
      if (node == null) return
      if (parent != null) {
        graph.getOrElseUpdate(node, scala.collection.mutable.ListBuffer.empty) += parent
        graph.getOrElseUpdate(parent, scala.collection.mutable.ListBuffer.empty) += node
      }
      build(node.left, node)
      build(node.right, node)
    }
    build(root, null)
    val queue = scala.collection.mutable.Queue(target)
    val seen = scala.collection.mutable.Set(target)
    var dist = 0
    while (queue.nonEmpty) {
      if (dist == k) return queue.toList.map(_.value)
      val size = queue.size
      var i = 0
      while (i < size) {
        val node = queue.dequeue()
        graph.getOrElse(node, scala.collection.mutable.ListBuffer.empty[TreeNode]).foreach { nei =>
          if (seen.add(nei)) queue.enqueue(nei)
        }
        i += 1
      }
      dist += 1
    }
    Nil
  }
}
