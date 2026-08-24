// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def constructFromPrePost(preorder: Array[Int], postorder: Array[Int]): TreeNode = {
    val postIndex = postorder.zipWithIndex.toMap
    def build(preLo: Int, preHi: Int, postLo: Int, postHi: Int): TreeNode = {
      if (preLo > preHi) return null
      val root = new TreeNode(preorder(preLo))
      if (preLo == preHi) return root
      val leftVal = preorder(preLo + 1)
      val leftPost = postIndex(leftVal)
      val leftSize = leftPost - postLo + 1
      root.left = build(preLo + 1, preLo + leftSize, postLo, leftPost)
      root.right = build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1)
      root
    }
    val n = preorder.length
    build(0, n - 1, 0, n - 1)
  }
}
