// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def increasingBST(root: TreeNode): TreeNode = {
    val dummy = new TreeNode(0)
    var cur = dummy
    def inorder(node: TreeNode): Unit = {
      if (node == null) return
      inorder(node.left)
      node.left = null
      cur.right = node
      cur = node
      inorder(node.right)
    }
    inorder(root)
    dummy.right
  }
}
