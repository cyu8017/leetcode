// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def bstFromPreorder(preorder: Array[Int]): TreeNode = {
    var i = 0
    def build(bound: Int): TreeNode = {
      if (i == preorder.length || preorder(i) > bound) return null
      val root = new TreeNode(preorder(i))
      i += 1
      root.left = build(root.value)
      root.right = build(bound)
      root
    }
    build(Int.MaxValue)
  }
}
