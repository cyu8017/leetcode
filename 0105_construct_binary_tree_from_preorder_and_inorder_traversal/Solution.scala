// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def buildTree(preorder: Array[Int], inorder: Array[Int]): TreeNode = {
    val index = inorder.zipWithIndex.toMap
    var preIndex = 0

    def build(left: Int, right: Int): TreeNode = {
      if (left > right) {
        null
      } else {
        val rootVal = preorder(preIndex)
        preIndex += 1
        val mid = index(rootVal)
        val root = new TreeNode(rootVal)
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        root
      }
    }

    build(0, inorder.length - 1)
  }
}