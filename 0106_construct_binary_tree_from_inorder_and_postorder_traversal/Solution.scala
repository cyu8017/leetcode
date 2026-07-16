// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def buildTree(inorder: Array[Int], postorder: Array[Int]): TreeNode = {
    val index = inorder.zipWithIndex.toMap
    var postIndex = postorder.length - 1

    def build(left: Int, right: Int): TreeNode = {
      if (left > right) {
        null
      } else {
        val rootVal = postorder(postIndex)
        postIndex -= 1
        val mid = index(rootVal)
        val root = new TreeNode(rootVal)
        root.right = build(mid + 1, right)
        root.left = build(left, mid - 1)
        root
      }
    }

    build(0, inorder.length - 1)
  }
}