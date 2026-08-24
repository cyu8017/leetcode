// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def createBinaryTree(descriptions: Array[Array[Int]]): TreeNode = {
    val nodes = scala.collection.mutable.Map.empty[Int, TreeNode]
    val child = scala.collection.mutable.Set.empty[Int]
    descriptions.foreach { d =>
      val p = d(0)
      val c = d(1)
      val isLeft = d(2)
      if (!nodes.contains(p)) nodes(p) = new TreeNode(p)
      if (!nodes.contains(c)) nodes(c) = new TreeNode(c)
      if (isLeft == 1) nodes(p).left = nodes(c)
      else nodes(p).right = nodes(c)
      child += c
    }
    nodes.collectFirst { case (k, v) if !child.contains(k) => v }.orNull
  }
}
