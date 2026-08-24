// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def amountOfTime(root: TreeNode, start: Int): Int = {
    val g = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]

    def build(node: TreeNode, parent: TreeNode): Unit = {
      if (node == null) return
      if (parent != null) {
        g.getOrElseUpdate(node.value, scala.collection.mutable.ArrayBuffer.empty[Int]) += parent.value
        g.getOrElseUpdate(parent.value, scala.collection.mutable.ArrayBuffer.empty[Int]) += node.value
      }
      build(node.left, node)
      build(node.right, node)
    }

    build(root, null)
    var ans = 0
    val vis = scala.collection.mutable.HashSet(start)
    val q = scala.collection.mutable.Queue((start, 0))
    while (q.nonEmpty) {
      val (cur, dist) = q.dequeue()
      ans = math.max(ans, dist)
      g.getOrElse(cur, scala.collection.mutable.ArrayBuffer.empty[Int]).foreach { nxt =>
        if (vis.add(nxt)) q.enqueue((nxt, dist + 1))
      }
    }
    ans
  }
}
