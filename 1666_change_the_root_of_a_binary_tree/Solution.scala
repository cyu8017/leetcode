// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

class Node(var value: Int = 0, var left: Node = null, var right: Node = null, var parent: Node = null)

object Solution {
  def flipBinaryTree(root: Node, leaf: Node): Node = {
    var node = leaf
    while (node ne root) {
      val parent = node.parent
      if (parent.left eq node) parent.left = null
      else parent.right = null
      val originalLeft = node.left
      node.left = parent
      if (originalLeft != null) node.right = originalLeft
      node = parent
    }
    def fixParent(cur: Node, parent: Node): Unit = {
      if (cur == null) return
      cur.parent = parent
      fixParent(cur.left, cur)
      fixParent(cur.right, cur)
    }
    fixParent(leaf, null)
    leaf
  }
}
